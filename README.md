# Python 生成课表(.ics)导入Mac日历

![image-20201](https://tva1.sinaimg.cn/large/007S8ZIlly1gjnpdhndsfj31970u0n4s.jpg)

## 简介

学校研究生没有本科待遇，课表没有录入系统😢，遂借鉴**[junyilou/python-ical-timetable](https://github.com/junyilou/python-ical-timetable)**适配了课程。项目生成ics文件导入Apple设备的日历应用，可以方便随时查看课表。

## 功能
* 支持录入课程名称，教师，上课地点，上课时间（也可以通过修改代码自己添加附加信息）

## 使用
请调整`main`函数中的以下内容来适配课表：

1. **maxWeek** 为本学期最大周数，可适当加大，但不可小于实际周数。

2. **classTime** 为每节课的**上课时间**（下课时间逻辑在`timetable`函数中）。直接填写每节课的 24 小时制上课时间：例如 8:00 上课，则录入`(8, 0)`；下午 7:50 上课，则录入`(19, 50)`。

3. 修改 **starterDay** 为本学期第一周星期一的日期。

4. 修改 **classes** 中的课程信息，由于不同学校课表可能含有不同信息，请参考源代码中的课表填写，并直接在后续定义中作出相应修改。

  **设置周数：**
单独周：请改为数组形式，例如 [2]；
  范围周：请使用`rgWeek`，例如 rgWeek(3, 7) 代表第三周到第七周；
  奇数周：请使用`oeWeek`，例如 oeWeek(2, 9, 1) 代表第二周到第九周的单数周，将 1 改为 0 即为偶数周。
  
  **设置课程节数：**
一节课：请改为数组形式，例如 [2]；
  范围课，请使用`rgWeek`，例如 rgWeek(3, 7) 代表第三节一直上到第七节；
5. 一节课的时间由`oneClassTime`表示，默认为45分钟，可自行修改。
6. 更改`filename`将ics文件保存在合适的位置。

### 导入方法

### [Mac导入日历(推荐)](https://support.apple.com/zh-cn/guide/calendar/icl1023/mac)

1. 在 Mac 上的“日历” App中，为日程[创建新日历](https://support.apple.com/zh-cn/guide/calendar/icl1005/11.0/mac/10.15)（如有需要）。
2. 选取“文件”>“导入”。
3. 选择带有日程的文件，然后点按“导入”。
4. 选择日历来添加日程。

导入Mac后，可通过共享供IOS设备使用。

<img src="https://tva1.sinaimg.cn/large/007S8ZIlly1gjnqf5nhc8j30i00aoqa5.jpg" alt="image-20201" style="zoom: 50%;" />

### [IOS导入日历](https://support.apple.com/zh-cn/guide/iphone/ipha0d932e96/ios)

1. 前往“设置” >“日历">“帐户">“添加帐户”。
2. 轻点“其他”，然后执行以下任一项操作：
    - *订阅 iCal (.ics) 日历：*轻点“添加已订阅的日历”，然后输入订阅的 .ics 文件的 URL；或导入来自“邮件”的 .ics 文件。

## 感谢

[@junyilou](https://github.com/junyilou)

### 项目地址

[TimetableInICalendar](https://github.com/Freder-chen/TimetableInICalendar)