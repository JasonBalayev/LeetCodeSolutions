class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year,month,day = map(int, date.split('-'))
        days_within_month =  [0, 31, 31, 31, 31, 31, 31, 1, 30, 30, 30, 30, 28]

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_within_month[2] = 29
        
        day_year = day
        for i in range(1, month):
            day_year += days_within_month[i]
        return day_year
    
#QED
#Problem 1154 (Easy Of Day Of The Year) - Jason Balayev (python)