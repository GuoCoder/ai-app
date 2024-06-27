## Getting started

### Prerequisites
    Install Python 3.7+
    pip3


### Git clone the example code repo
    git clone https://github.com/zilliztech/cloud-vectordb-examples.git

### Install pymilvus
    pip3 install pymilvus==2.3.4

### Go to python folder
    cd cloud-vectordb-examples
    cd python

### Modify uri, token in the configuration file.(config_serverless.ini)
    uri = https://in01-XXXXXXXXXXXX.aws-us-west-2.vectordb.zillizcloud.com
    token = replace-this-with-your-token

### Run hello_zilliz_vectordb_serverless.py
    python3 hello_zilliz_vectordb_serverless.py

### It should print information on the console
    Connecting to DB: https://in01-xxxxxxxxxxxxx.aws-us-west-2.vectordb.zillizcloud.com
    Success!
    Creating example collection: book
    Schema: {...}
    Success!
    Inserting 2000 entities... 
    Succeed in 0.3021 seconds!
    Flushing...
    Succeed in 0.77 seconds!
    Building AutoIndex...
    Succeed in 18.9118 seconds!
    Loading collection...
    Succeed in 2.5229 seconds!
    Searching vector:[[...][...]...]
    search 0 latency: 0.0057 seconds!
    Searching vector:[[...][...]...]
    search 1 latency: 0.0049 seconds!
    Searching vector:[[...][...]...]
    search 2 latency: 0.0051 seconds!
    ...
    ...
    
