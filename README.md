## 1安装python

## 2安装pip

## 3安装requests

pip install requests

##4 修改脚本并保存、把节点号修改成自己节点的

## 5运行

python3 autotalk.py

#下面的不要看

### 创建一个文档路径E://docker-data/qdrant_storage
### cuda>12.5使用cuda12尾缀，小于使用cuda11
docker run --name gaianet -p 8080:8080 --gpus all -v E://docker-data/qdrant_storage:/root/gaianet/qdrant/storage:z gaianet/phi-3-mini-instruct-4k_paris:cuda11

### 进入交互式容器
docker exec -it gaianet /bin/bash

### 重启一次容器内的节点
gaianet stop
gaianet start
