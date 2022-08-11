# MS开发笔记

#### 分支命名规范
- 正式分支示例： integration/official/1293m104
- 个人开发分支示例： user/zenye/2-decimal-places 

#### Telemetry
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
	- 


	





