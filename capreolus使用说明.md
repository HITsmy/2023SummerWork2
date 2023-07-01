capreolus v1.0.0 apk逆向工具使用说明（针对网址信息静态分析）
1.-url				提取全部url信息
2.-sni				提取全部sni信息
3.-f				分析上传的文件  xxx.apk
4.-d				分析文件夹  e.g. /home/xxx/test/
5.-u				下载并分析某一网站的apk文件	e.g. https://www.xx.com/test.apk
6.-notida			对android逆向后的.so文件不进行深度分析（消耗的时间可能会相对少一些，但是结果可能不全）
7.-notsave			删除apk逆向的中间文件（主要包括smali代码以及一些xml文件），否则默认会删除
8.-o				导出txt文件(夹)位置
9.-e1|-e2|-e3			结果优化的三个级别，根据功能需要具体选择(若需原始数据不建议优化)
10.-h				帮助

使用方法：./capreolus -提取内容 -参数1 提取文件类型 (-o -输出文件文本路径) -其他运行参数

使用示例一: ./capreolus  -url -d test/ -noida
提取/home/xxx/test下的全部apk中的url信息，.so文件不进行进一步分析，导出结果为默认当前路径下的与原apk同名的txt
使用示例二: ./capreolus  -sni -u https://www.xxxx.com/example.apk -o /home/xxx/test/outputs.txt
服务器去指定网站下载对应的apk并提取sni，.so文件不进行进一步分析，导出位置为/home/xxx/test下的outputs.txt

##以下为待开发功能：
11.-phone			获取app中全部的电话号码
12.-email			获取app中全部的email信箱网址
13.-auth			获取app所需的全部权限

##出于安全考虑-notsave功能暂时停止启用，如需删除请手动删除临时文件夹tempfiles
	逆向后文件夹预计大小在原apk文件的10倍以上，请注意分配空间
##优化的三个级别:
	-e1:删除一些常见的API网址或程序相关的域名，如：含github，java等字段的网址
	-e2:在-e1基础上删除一些提供第三方服务API的网址，如:qq，baidu，alipay等
	-e3:只保留自己所需要字段的结果信息，如：只保留含有bd、baidu等字段的url
	优化将导致部分可能相关的结果被删除，请确定后再执行
	需要删除的特征字段保存在目录下patterns.conf (-e1)和apis.conf (-e2)中，可自行修改需要删除的字段
	需要保留的特征字段保存在目录下appselected.conf中，通常不建议使用此选项

