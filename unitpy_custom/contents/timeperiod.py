import datetime
import calendar
from dateutil.relativedelta import relativedelta
'''
    timeperiod()    # 現時刻を基準に算出
    timeperiod(yyyy,MM,dd)    #指定日を基準に算出
'''


# UnitxTimeを文字列に変換
def convertToUnixTime(StringTime):
    date_format = '%Y-%m-%d %H:%M:%S'
    try:
        dt = datetime.datetime.strptime(StringTime, date_format)
        return int(dt.timestamp())
    except ZeroDivisionError:
        return 'Error'


# 文字列をUnixタイムに変換
def convertToStrginTime(UnixTime):
    date_format = '%Y-%m-%d %H:%M:%S'
    try:
        dt = datetime.datetime.fromtimestamp(UnixTime)
        return dt.strftime(date_format)
    except ZeroDivisionError:
        return 'Error'


# Unixタイムを日付と時間に分離
def convertToDayDate(UnixTime):
    day_format = '%Y-%m-%d'
    date_format = '%H:%M:%S'
    try:
        dt = datetime.datetime.fromtimestamp(UnixTime)
        return {
            'day': dt.strftime(day_format),
            'date': dt.strftime(date_format)
        }
    except ZeroDivisionError:
        return 'Error'


class timeperiod():
    now = None
    today = None
    date_format = '%Y-%m-%d %H:%M:%S'

    def __init__(self, *args):
        if len(args) != 3:
            self.now = datetime.datetime.now()
        else:
            self.now = datetime.datetime(args[0], args[1], args[2])
        # print(self.now)

    def __returnPeriod(self, period, dtTime_from, dtTime_till):
        return {
            "period": period,
            "dtTime_from": dtTime_from.strftime(self.date_format),
            "dtTime_till": dtTime_till.strftime(self.date_format),
            "unixTime_from": int(dtTime_from.timestamp()),
            "unixTime_till": int(dtTime_till.timestamp())
        }

    # 前日
    def Yesterday(self):
        yesterday = self.now - relativedelta(days=1)
        dtTime_from = datetime.datetime(yesterday.year, yesterday.month,
                                        yesterday.day)
        dtTime_till = datetime.datetime(yesterday.year, yesterday.month,
                                        yesterday.day, 23, 59, 59, 999999)
        # print(dt_time_from); print(dt_time_till)
        return self.__returnPeriod("yesterday", dtTime_from, dtTime_till)

    # 先月
    def LastMonth(self):
        lastmonth = self.now - relativedelta(months=1)
        print(lastmonth)
        Lastday_of_the_month = calendar.monthrange(lastmonth.year,
                                                   lastmonth.month)[1]
        dtTime_from = datetime.datetime(lastmonth.year, lastmonth.month, 1)
        dtTime_till = datetime.datetime(lastmonth.year, lastmonth.month,
                                        Lastday_of_the_month, 23, 59, 59,
                                        999999)
        # print(dt_time_from); print(dt_time_till)
        return self.__returnPeriod("lastDay", dtTime_from, dtTime_till)

    # 去年
    def LastYear(self):
        dtTime_from = datetime.datetime(self.now.year - 1, 1, 1)
        dtTime_till = datetime.datetime(self.now.year - 1, 12, 31, 23, 59, 59,
                                        999999)
        # print(dt_time_from); print(dt_time_till)
        return self.__returnPeriod("lastDay", dtTime_from, dtTime_till)

    # 先週
    def LastWeek(self):
        offsetDay = self.now.isoweekday()  #isoweekday:(Monday:1,SunDay: 7)
        lastMonday = self.now - relativedelta(days=(offsetDay + 6))
        lastSunDay = self.now - relativedelta(days=offsetDay)
        dtTime_from = datetime.datetime(lastMonday.year, lastMonday.month,
                                        lastMonday.day)
        dtTime_till = datetime.datetime(lastSunDay.year, lastSunDay.month,
                                        lastSunDay.day, 23, 59, 59, 999999)
        return self.__returnPeriod("lastWeek", dtTime_from, dtTime_till)

    # 先週の平日
    def LastWeekdays(self):
        offsetDay = self.now.weekday()  #weekday:(Monday:0,SunDay: 6)
        lastMonday = self.now - relativedelta(days=(offsetDay + 7))
        lastFriDay = self.now - relativedelta(days=(offsetDay + 3))
        dtTime_from = datetime.datetime(lastMonday.year, lastMonday.month,
                                        lastMonday.day)
        dtTime_till = datetime.datetime(lastFriDay.year, lastFriDay.month,
                                        lastFriDay.day, 23, 59, 59, 999999)
        return self.__returnPeriod("lastWeekdays", dtTime_from, dtTime_till)

    # 過去N日
    def LastNdays(self, offsetDays):
        periodString = "last" + str(offsetDays) + "days"
        offsetDay = self.now - datetime.timedelta(days=offsetDays)
        dtTime_from = datetime.datetime(offsetDay.year, offsetDay.month,
                                        offsetDay.day)
        dtTime_till = datetime.datetime(offsetDay.year, offsetDay.month,
                                        offsetDay.day, 23, 59, 59, 999999)
        return self.__returnPeriod(periodString, dtTime_from, dtTime_till)


## Test Code ##

    '''
def main():
        print(convertToStrginTime(1577969693))
        print(convertToDayDate(1577969693))
        print(convertToUnixTime("2020-01-02 21:54:53"))

        print("timeperiod Testcode")
        period = timeperiod()
        print("Yesterday")
        print(period.Yesterday())
        print("LastMonth")
        print(period.LastMonth())
        print("LastYear")
        print(period.LastYear())
        print("LastWeek")
        print(period.LastWeek())
        print("LastWeekdays")
        print(period.LastWeekdays())
        print("LastNdays")
        print(period.LastNdays(3))

if __name__ == '__main__':
    main()
    '''