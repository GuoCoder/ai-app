## Getting started

### Prerequisites

Node 14+

### Git clone the example code repo

```bash
git clone https://github.com/zilliztech/cloud-vectordb-examples
```

### Go to milvus-node folder

```bash
  cd cloud-vectordb-examples
  cd node
```

### Install sdk

```bash
npm install
```

#### Dedicated cluster

##### Modify uri, user name and user password in configuration file.(config.js)

```javascript
{
  uri: " https://in01-XXXXXXXXXXXXX.aws-us-west-2.vectordb.zillizcloud.com:XXXXX",
  token: "username:password",
};
```

#### Serverless cluster

##### Modify uri, token in configuration file.(config.js)

```javascript
{
  uri: "https://in03-XXXXXXXXXXXXX.api.gcp-us-west1.cloud-uat3.zilliz.com",
  token: "api-key",
};

```

### Run HelloZillizCloud.js

```shell
npm install
node HelloZillizCloud.js
```
