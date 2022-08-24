# MS开发笔记

## 分支命名规范
- 正式分支示例： integration/official/1293m104
- 个人开发分支示例： user/zenye/2-decimal-places 

## Code

##### format & check & presubmit
```
git ms format --upstream=origin/main

gn check out/Debug-iphonesimulator

git ms presubmit main --force

```

##### 更新流程
```
git pull
gclient sync
ios/build/tools/setup-gn.py
```
##### build
```
cd $ROOT/src/out/Debug-iphonesimulator
autoninja chrome
```
```
cd $ROOT/src/out/build
open all.xcodeproj
```
##### 新增文件
- 修改文件名驼峰改成下划线
- 增加宏定义，防止include重复
- 修改lisence
- arc mrc def
- 修改gn


## Crash
##### DYSM下载
[下载地址](https://microsoft.visualstudio.com/Edge/_build?definitionScope=%5COfficial%5CPromotion)



## Telemetry
##### histogram（最终发出去都是直方图）
- 类型
	- Enum
	- BOOL 
	- event 次数
	- 毫秒
- edge_histogram.xml (其中存储了所有埋点)
	```
	<histogram name="Microsoft.Mobile.Accessibility.DailyStatus"
    	enum="BooleanEnabled" expires_after="2022-11-20">
  	<owner>huanglin@microsoft.com</owner>
  	<owner>edgemobiledevs@microsoft.com</owner>
  	<summary>
    	Records the daily status of whether accessiblity is turned on when Edge
    	starts up.
  	</summary>
	</histogram>
	```
- edge_metricsmetadata.json (标记隐私类型、组)
	```
	{
		"Name": "Microsoft.Mobile.Accessibility.DailyStatus",
		"PrivacyDataTypes": [
			"Privacy.DataType.ProductAndServiceUsage"
    		],
		"Team": "Edge\\Mobile"
	},
	```
- 打一个Tag，标记采样率，采样类型
	- 例如：FeatureSuccessMetrics
- 假如是枚举类型，需要配置在edge_enums.xml
- 在网页edge://histograms中看到
	- 可以看到代码形成的横向的直方图
- 后台数据查看连接：[link](https://aad.cosmos11.osdinfra.net/cosmos/edgedata.prod)
- 参考链接
	- [Adding Histograms walkthrough](https://microsoft.visualstudio.com/Edge/_wiki/wikis/Edge.wiki/103/Adding-Histograms-walkthrough)
	- [Adding Histograms](https://docs.edgeteam.ms/docs/dataset/histograms/create/)
	- [zeng zhuohan的视频解说](https://microsoftapc-my.sharepoint.com/personal/zhuohanzeng_microsoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fzhuohanzeng%5Fmicrosoft%5Fcom%2FDocuments%2FRecordings%2FEdge%5Fmobile%5Fhistograms%5Fand%5Fdata%5Fpipeline%5Fintro%2Emp4&parent=%2Fpersonal%2Fzhuohanzeng%5Fmicrosoft%5Fcom%2FDocuments%2FRecordings&ga=1)


	





