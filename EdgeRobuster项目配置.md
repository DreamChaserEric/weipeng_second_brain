# Edge Robuster项目配置

## Clone项目
## 安装virtualenv
- pip3 install --user virtualenv(基于python3版本）
- 创建virtualenv:
	+ python3 -m venv edge_robuster_server_env(基于python3版本）
- 激活virtualenv:
	+ source edge_robuster_server_env/bin/activate
- 关闭virtualenv:
	+ deactivate

# 安装Flask
	pip3 install Flask(基于python3)

# 安装依赖
	pip3 install flask_cors
	pip3 install pymongo
	pip3 install requests
	

# 安装mongodb
- 安装HomeBrew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- mongodb
```
brew tap mongodb/brew
brew install mongodb-community@6.0

brew services start mongodb-community@6.0
brew services stop mongodb-community@6.0
```

- 可视化工具
	https://www.mongodb.com/try/download/compass

# 安装Node.js
https://nodejs.org/en/

# 运行Vue项目
	npm install

# Docker (Mac)
- 安装Docker
```
brew install --cask --appdir=/Applications docker
```

- Docker Image for Mongo
```
docker pull mongo:latest
```






