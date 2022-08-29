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