#Crash Analysis

参考链接： [掘金](https://juejin.cn/post/7030619552211795982)

## symbolicatecrash
首先通过终端找到 symbolicatecrash 路径, 通过 ./symbolicatecrash 结合 dsym 和提供的 crash/ips/beta 文件来进行符号化。
#### 路径
```
find /Applications/Xcode.app -name symbolicatecrash -type f

SharedFrameworks/DVTFoundation.framework/Versions/A/Resources
```
#### 使用
脚本 -> 产生崩溃文件路径 -> dsym 路径 > 输出符号化文件路径
```
./symbolicatecrash crashFilePath dsymPath > crashSymbolFilePath
```
#### 问题
- Error: "DEVELOPER_DIR" is not defined at ./symbolicatecrash line 69.
这是因为脚本有执行需要依赖环境宏定义
执行 export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer 即可

- No crash report version in file
最近在符号化 iOS 15 以上的崩溃时, 总是提示找不到崩溃版本, 很诡异, 最后查了一下原因是 iOS 15 crash log 格式做了更新, 需要用到下面的 CrashSymbolicator.py 来进行符号化。

- UUID 不一致
当不确定当前崩溃是否跟拿到的 dsym 是否为想对应的包时, 使用 dwarfdump --uuid dSYM文件路径
查看 dsym UUID: dwarfdump --uuid dSYM文件路径


## CrashSymbolicator.py
因为崩溃文件是 iOS 15 产生, 原来不知道 Apple 做了这一项调整, 一直在用 symbolicatecrash 进行解析, 终端报错 No crash report version in file, 查了下资料才发现新的文件格式得使用 CrashSymbolicator.py 解析

[xcode-13-release-notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes)

iOS 15 之后 Apple 对符号化文件格式进行了 JSON 支持, 所以针对 iOS 15 以上产生的崩溃文件, 写入方式应该是做了调整, 所以在对 iOS 15 以上崩溃文件进行符号化时, 直接使用 CrashSymbolicator.py 来解析, 否则会出现符号化失败, 报错 No crash report version in file 的问题。

## 路径
```
find /Applications/Xcode.app -name CrashSymbolicator -type f
```
和使用 symbolicatecrash 方式类似, 先找到其路径, 系统列出不同平台 sh, 切换到最后一个 /Applications/Xcode.app/Contents/SharedFrameworks/CoreSymbolicationDT.framework/Versions/A/Resources
稍微和 symbolicatecrash 不同的是, 其调用方式可以支持参数的方式来排列文件顺序,并且其是用 python 写的脚本, 所以要使用 python3 来进行调用, 否则会报错。
-d '符号表路径' -o '输出符号化路径' -p '苹果给的崩溃日志'

## 使用
```
python3 CrashSymbolicator.py -d /dSYMs -o /xxxSymbo.crash -p /xxxCrash.ips
```