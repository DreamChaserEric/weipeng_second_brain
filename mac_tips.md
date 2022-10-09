# mac_tips

#### 设置文件默认打开方式
- 右键点击文件在下拉菜单中选择【显示简介】
- 在简介窗口中点击【打开方式】下拉框，软化在下拉菜单中选择默认打开的软件
- 点击下方【全部更改】即可生效

#### Mac展示隐藏文件
```
defaults write com.apple.Finder AppleShowAllFiles YES;KillAll Finder

defaults write com.apple.Finder AppleShowAllFiles NO;KillAll Finder
```

#### 查看mac是x86还是arm
```
uname -a
```

#### 查看MacOS使用的是什么样的Shell
```
// 回车执行如果输出的是：csh或者是tcsh，那么你用的就是C Shell
// 如果输出的是：bash，sh，zsh，那么你的用的可能就是Bourne Shell的一个变种
echo $SHELL
```

#### SSH配置
git使用SSH配置， 初始需要以下三个步骤
- 使用秘钥生成工具生成rsa秘钥和公钥
- 将rsa公钥添加到代码托管平台
- 将rsa秘钥添加到ssh-agent中，为ssh client指定使用的秘钥文件

###### 第一步：检查本地主机是否已经存在ssh key
```
cd ~/.ssh
ls
//看是否存在 id_rsa 和 id_rsa.pub文件，如果存在，说明已经有SSH Key
```
如下图所示，则表明已经存在

![img](https://github.com/DreamChaserEric/weipeng_second_brain/blob/main/imgs/wp_s_b_3.png)

如果存在，直接跳到第三步

###### 第二步：生成ssh key
如果不存在ssh key，使用如下命令生成
```
ssh-keygen -t rsa -C "xxx@xxx.com"
//执行后一直回车即可
```
生成完以后再用第二步命令，查看ssh key

###### 第三步：获取ssh key公钥内容（id_rsa.pub）

```
cd ~/.ssh
cat id_rsa.pub
```
如下图所示，复制该内容

![img](https://github.com/DreamChaserEric/weipeng_second_brain/blob/main/imgs/wp_s_b_4.png)

###### 第四步：Github账号上添加公钥
Profile->Settings->SSH and GPG keys->New SSH Key
把刚才复制的内容粘贴上去保存即可

###### 第五步：验证是否设置成功
```
ssh -T git@github.com
```
设置成功后，即可不需要账号密码clone和push代码.
注意之后在clone仓库的时候要使用ssh的url，而不是https！

[CSDN链接](https://blog.csdn.net/weixin_42310154/article/details/118340458)