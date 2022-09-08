# Git Tips

##### Git Fetch无法获取远程分支问题
编辑 .git/config 文件，把 fetch 改成下面第二种形式，不要写死master。
```
[remote "origin"]
        url = https://github.com/xxx/project.git
        fetch = +refs/heads/master:refs/remotes/origin/master
```

```
[remote "origin"]
        url = https://github.com/xxx/project.git
        fetch = +refs/heads/*:refs/remotes/origin/*
```

##### Commit Message Guideline
- feat：新功能（feature）
- fix：修补bug
- docs：文档（documentation）
- style： 格式（不影响代码运行的变动）
- refactor：重构（即不是新增功能，也不是修改bug的代码变动）
- test：增加测试
- chore：构建过程或辅助工具的变动

##### 丢弃指定Commit
1. 找到目前commit id 之前的id(commit id 2)
2. git rebase -i (commit id 2)