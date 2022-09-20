# TTI

[交接文档](https://microsoftapc-my.sharepoint.com/:w:/r/personal/banl_microsoft_com/_layouts/15/doc2.aspx?sourcedoc=%7B08AB4AAD-91B6-493E-A4AB-DCC775107072%7D&file=Bang.docx&action=default&mobileredirect=true&share=IQGtSqsItpE-SaSr3Md1EHByAV8lwRahOtjrSVPnmzTvPls&cid=da1d066e-144e-49df-a5d4-833a6d4e786d)
- [Edge iOS Startup Performance ](https://microsoftapc-my.sharepoint.com/:w:/g/personal/stonedong_microsoft_com/EejQ9BaiLB5Go-TYG1HA7hMBsPFuEMduHUxtuEfMNlkNrw?e=Q78LcE)
- [Edge iOS Snapshot for PPLT optimization ](https://microsoftapc-my.sharepoint.com/:w:/g/personal/stonedong_microsoft_com/EdBwSw8nG7xGpXPxuMuAUxABjNhddUQr4-8-fj-Ee8WYag?e=tu3Fyg)
- [Perf and Metrics](https://microsoft.visualstudio.com/Edge/_wiki/wikis/Edge.wiki/73123/Perf-and-Metrics)

## TTI

#### Android: Jiang Yu

#### 做了什么
TTI PLT PPLT(目前最关注)
- Pre-main优化
	+ 动态库，[已完成](https://microsoft.visualstudio.com/Edge/_wiki/wikis/Edge.wiki/73128/Convert-Dynamic-Libraries-to-Static-Ones)。但是需要code review关注新增动态库，如果需求条件允许，一律不链接，采取feature被用户用到才进行dlopen的策略。需求条件不允许，就测量启动数据，看是否能接受带来的影响。
	+ 静态初始化代码，[已完成](https://microsoft.visualstudio.com/Edge/_wiki/wikis/Edge.wiki/59041/Static-Initializers)。Instruments可以分析这一块的启动耗时。暂时没有需要跟进的内容，后续可以考虑增加静态代码检查，从CI上保证大家不会不小心写了这样的代码。 
 
- Post-main优化
	+  启动任务，已完成。后续需要关注code review，
		+ 可以延后（任务型）加到 -[MainControllerEdge runDeferredTasks]
		+ 把启动时的upsell（可以延后，UI弹窗）加到 -[SceneControllerEdge scheduleFeatureUpsells] 
		+ RunEagerTasks中放不可延迟操作。 
	+ PPLT和截图，进行中。参考上面的文档和[代码](https://microsoft.visualstudio.com/Edge/_git/chromium.src/pullrequest/7765874)。Stone对这个事情也比较了解。 

#### 代码
```
PPLT
// The snapshot shows.  
void RecordSnapshotShow();

TTI
// The real omnibox shows. 
void RecordAddressBarShow();

TTI
// The fake omnibox in NTP shows.  
void RecordSearchBoxShow();

PLT
// News feed web page commits navigation.  
void RecordWebPageFirstDraw();
```

#### 数据
- [大盘](https://grafana-corp.bingviz.microsoftapp.net/d/82gnhikVz/edge-mobile-stability-and-perf?orgId=1)
- [区分版本](https://grafana-corp.bingviz.microsoftapp.net/d/T8kfD-j7z/edge-performance?orgId=1)
- 目前主要是Yu Jiang在做一些和Android共用的dashboard。现在BingViz数据已经带上了设备型号，后面可以再分型号、系统版本等进行分析。 
- BingViz数据格式相关主要联系Yu Jiang。Wiki在SA的project里，[链接](https://msasg.visualstudio.com/SAN%20SA/_wiki/wikis/SAN%20SA%20Scaffolding%20Wiki/85618/Perf-Quality-integration)。Histogram和AppCenter的数据目前代码还在发，但是dashboard里已经不使用了。 





