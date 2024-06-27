package main

import (
	"context"
	"fmt"
	"log"
	"math/rand"
	"time"

	"github.com/milvus-io/milvus-sdk-go/v2/client"
	"github.com/milvus-io/milvus-sdk-go/v2/entity"
)

func main() {
	collectionName := "book"
	uri := "" // https://in01-xxxx.region.zillizcloud.com:port
	user := "username"
	password := "password"

	// connect to milvus
	fmt.Println("Connecting to DB: ", uri)
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	client, err := client.NewClient(ctx, client.Config{
		Address:  uri,
		Username: user,
		Password: password,
	})

	if err != nil {
		log.Fatal("fail to connect to milvus", err.Error())
	}
	fmt.Println("Success!")

	// delete collection if exists
	has, err := client.HasCollection(ctx, collectionName)
	if err != nil {
		log.Fatal("fail to check whether collection exists", err.Error())
	}
	if has {
		client.DropCollection(ctx, collectionName)
	}

	// create a collection
	fmt.Println("Creating example collection: book")
	schema := entity.NewSchema().WithName(collectionName).WithDescription("Medium articles published between Jan 2020 to August 2020 in prominent publications").
		WithField(entity.NewField().WithName("book_id").WithDataType(entity.FieldTypeInt64).WithIsPrimaryKey(true).WithDescription("customized primary id")).
		WithField(entity.NewField().WithName("word_count").WithDataType(entity.FieldTypeInt64).WithDescription("word count")).
		WithField(entity.NewField().WithName("book_intro").WithDataType(entity.FieldTypeFloatVector).WithDim(128))

	err = client.CreateCollection(ctx, schema, entity.DefaultShardNumber)
	if err != nil {
		log.Fatal("failed to create collection", err.Error())
	}
	fmt.Println("Success!")

	// insert data
	fmt.Println("Inserting 100000 entities... ")
	dim := 128
	num_entities := 100000
	idList, countList := make([]int64, 0, num_entities), make([]int64, 0, num_entities)
	vectorList := make([][]float32, 0, num_entities)
	for i := 0; i < num_entities; i++ {
		idList = append(idList, int64(i))
		countList = append(countList, int64(i))
		vec := make([]float32, 0, dim)
		for j := 0; j < dim; j++ {
			vec = append(vec, rand.Float32())
		}
		vectorList = append(vectorList, vec)
	}

	idData := entity.NewColumnInt64("book_id", idList)
	countData := entity.NewColumnInt64("word_count", countList)
	vectorData := entity.NewColumnFloatVector("book_intro", dim, vectorList)

	begin := time.Now()
	_, err = client.Insert(ctx, collectionName, "", idData, countData, vectorData)
	if err != nil {
		log.Fatal("fail to insert data", err.Error())
	}
	fmt.Println("Succeed in", time.Since(begin))

	// create index
	fmt.Println("Building AutoIndex...")
	index, err := entity.NewIndexAUTOINDEX(entity.L2)
	if err != nil {
		log.Fatal("fail to get auto index", err.Error())
	}
	begin = time.Now()
	err = client.CreateIndex(ctx, collectionName, "book_intro", index, false)
	if err != nil {
		log.Fatal("fail to create index", err.Error())
	}
	fmt.Println("Succeed in", time.Since(begin))

	// load collection
	fmt.Println("Loading collection...")
	begin = time.Now()
	err = client.LoadCollection(ctx, collectionName, false)
	if err != nil {
		log.Fatal("fail to load collection", err.Error())
	}
	fmt.Println("Succeed in", time.Since(begin))

	// search
	sp, _ := entity.NewIndexAUTOINDEXSearchParam(1)
	vectors := []entity.Vector{entity.FloatVector(vectorList[1])}
	fmt.Println("Search...")
	begin = time.Now()
	searchResult, err := client.Search(
		ctx,
		collectionName,      // collectionName
		nil,                 // partitionNames
		"",                  // expression
		[]string{"book_id"}, // outputFields
		vectors,             // vectors
		"book_intro",        // vectorField
		entity.L2,           // metricType
		10,                  // topK
		sp,                  // search params
	)
	if err != nil {
		log.Fatal("search failed", err.Error())
	}
	fmt.Println("Succeed in", time.Since(begin))

	for _, sr := range searchResult {
		fmt.Println("ids: ", sr.IDs)
		fmt.Println("Scores: ", sr.Scores)
	}
}
