import datetime
from datetime import datetime, timedelta

def oeWeek(startWeek, endWeek, mode):
    allWeek = range(startWeek, endWeek + 1)
    oddWeek = []; evenWeek = []
    for w in allWeek:
        if w % 2 == 0: evenWeek.append(w)
        else: oddWeek.append(w)
    if mode: return oddWeek
    else: return evenWeek


def rgWeek(startWeek, endWeek): return list(range(startWeek, endWeek + 1))


def timetable(maxWeek, classTime, starterDay, classes, oneClassTime=45):
    maxWeek += 1

    weeks = [None]
    for i in range(1, maxWeek):
        singleWeek = [None]
        for d in range(0, 7):
            singleWeek.append(starterDay)
            starterDay = starterDay + timedelta(days = 1)
        weeks.append(singleWeek)

    iCalHeader = 'BEGIN:VCALENDAR\n' \
        + 'METHOD:PUBLISH\n' \
        + 'VERSION:2.0\n' \
        + 'X-WR-CALNAME:课表\n' \
        + 'PRODID:-//Apple Inc.//Mac OS X 10.15.6//EN\n' \
        + 'X-WR-TIMEZONE:Asia/Shanghai\n' \
        + 'CALSCALE:GREGORIAN\n' \
        + 'BEGIN:VTIMEZONE\n' \
        + 'TZID:Asia/Shanghai\n' \
        + 'END:VTIMEZONE\n'

    createNow = datetime.now() - timedelta(hours = 8)
    
    allvEvent = ""
    for Class in classes:
        [Name, Teacher, Location, classWeek, classWeekday, classOrder] = Class[:]
        Title = Name + "@" + Location
        for timeWeek in classWeek:
            classDate = weeks[timeWeek][classWeekday]
            startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
            classStartTime = classDate + timedelta(minutes = startTime[0] * 60 + startTime[1])
            classEndTime = classDate + timedelta(minutes = endTime[0] * 60 + endTime[1] + oneClassTime)
            Description = " 任课教师: " + Teacher + "。"
            vEvent = "\nBEGIN:VEVENT"
            vEvent += "\nDTEND;TZID=Asia/Shanghai:" + classEndTime.strftime('%Y%m%dT%H%M%S')
            vEvent += "\nSUMMARY:" + Title
            vEvent += "\nDTSTART;TZID=Asia/Shanghai:" + classStartTime.strftime('%Y%m%dT%H%M%S')
            vEvent += "\nDESCRIPTION:" + Description
            vEvent += "\nEND:VEVENT"
            allvEvent += vEvent
    allvEvent += "\nEND:VCALENDAR"
    return iCalHeader + allvEvent


def main():
    maxWeek = 20
    classTime = [None, (8, 20), (9, 15), (10, 20), (11, 15), (14, 00), (14, 55), 
    (16, 00), (16, 55), (19, 0), (19, 55), (20, 50)]
    starterDay = datetime(2020, 8, 31)
    classes = [
        ['数据科学1班', '张兴兰/陆艳军', '5-508', rgWeek(12, 19), 1, [3, 4]],
        ['综合英语10班', '彭静', '1-603', rgWeek(4, 10), 2, [3, 4]],
        ['综合英语10班', '彭静', '1-603', rgWeek(12, 16), 2, [3, 4]],
        ['数据科学1班', '张兴兰/陆艳军', '5-508', rgWeek(12, 19), 2, [5, 6]],
        ['算法设计与分析1班', '陈媛', '5-508', rgWeek(4, 10), 2, [7, 8]],
        ['算法设计与分析1班', '陈媛', '5-508', rgWeek(12, 16), 2, [7, 8]],
        ['综合英语10班', '彭静', '4-512', rgWeek(4, 10), 3, [3, 4]],
        ['综合英语10班', '彭静', '4-512', rgWeek(12, 13), 3, [3, 4]],
        ['综合英语10班', '彭静', '1-603', rgWeek(14, 16), 3, [3, 4]],
        ['算法设计与分析1班', '陈媛', '5-508', rgWeek(4, 7), 3, [7, 8]],
        ['算法设计与分析1班', '陈媛', '4-314', rgWeek(8, 10), 3, [7, 8]],
        ['算法设计与分析1班', '陈媛', '4-314', rgWeek(12, 16), 3, [7, 8]],
        ['数据科学1班', '张兴兰/陆艳军', '4-310', rgWeek(12, 19), 4, [1, 2]],
        ['计算智能及应用1班', '石美凤', '5-508', rgWeek(6, 10), 4, [1, 2]],
        ['高等工程数学1班', '许安见/谢挺', '5-509', rgWeek(7, 10), 4, [3, 4]],
        ['高等工程数学1班', '许安见/谢挺', '5-509', rgWeek(12, 19), 4, [3, 4]],
        ['英语听说9班', 'Chris', '1-608', rgWeek(4, 9), 4, [5, 6]],
        ['学术规范与科技论文写作', '刘小洋', '5-508', rgWeek(6, 9), 4, [7, 8]],
        ['学术规范与科技论文写作', '刘小洋', '5-508', rgWeek(6, 9), 4, [9, 10]],
        ['计算智能及应用1班', '石美凤', '5-508', rgWeek(6, 10), 5, [1, 2]],
        ['计算智能及应用1班', '石美凤', '5-508', rgWeek(12, 17), 5, [1, 2]],
        ['高等工程数学1班', '许安见/谢挺', '5-508', rgWeek(7, 10), 5, [3, 4]],
        ['高等工程数学1班', '许安见/谢挺', '5-508', rgWeek(12, 19), 5, [3, 4]],
        ['机器学习及应用1班', '冯欣/龙建武', '5-508', rgWeek(6, 10), 5, [5, 6]],
        ['机器学习及应用1班', '冯欣/龙建武', '5-508', rgWeek(12, 19), 5, [5, 6]],
        ['中国特色社会主义理论与实践研究8班', '黎野', '1-605', rgWeek(4, 10), 5, [7, 8]],
        ['中国特色社会主义理论与实践研究8班', '黎野', '1-605', rgWeek(12, 16), 5, [7, 8]],
        ['机器学习及应用1班', '冯欣/龙建武', '5-508', rgWeek(6, 8), 5, [9, 10]],
    ]
    filename = 'timetable.ics'
    with open(filename, 'w') as f:
        f.write(timetable(maxWeek, classTime, starterDay, classes))


if __name__ == '__main__':
    main()
