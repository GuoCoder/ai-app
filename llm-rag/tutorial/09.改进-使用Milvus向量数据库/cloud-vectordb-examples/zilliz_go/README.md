## Getting started

### Prerequisites
    go >= 1.18

### Git clone the example code repo
    git clone https://github.com/zilliztech/cloud-vectordb-examples.git

### Install milvus-sdk-go
    go get -u github.com/milvus-io/milvus-sdk-go/v2

### Go to milvus_go folder
    cd cloud-vectordb-examples
    cd milvus_go

### Modify uri, username and user password in the configuration file.(config.go)
```go
const (
	uri      = "https://in01-XXXXXXXXXXXXX.aws-us-east-2.vectordb.zillizcloud.com:XXXXX"
	user     = "db_admin"
	password = "XXXXXXXXXXXXX"
)
```

### Run HelloZillizCloud.go
    go run HelloZillizCloud.go

### It should print information on the console
```
Connecting to DB: https://in01-XXXXXXXXXXXXX.aws-us-east-2.vectordb.zillizcloud.com:XXXXX
Success!
Creating example collection: book
Success!
Inserting 100000 entities... 
Succeed in  2.391643208s
Building AutoIndex...
Succeed in  1.170188209s
Loading collection...
Succeed in  9.246094375s
Search...
Succeed in  584.865167ms
&{ [1 560 412 773 747 171 14 598 506 897]}
[0 14.840795 15.720606 16.305355 16.57472 16.69268 16.71979 16.856443 16.934048 17.061205]
```
    