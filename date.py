'''
Created on 4/25/2020
@author:   ccalder
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
-Cameron Calder

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
            as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day

    def tomorrow(self):
        '''Represents the change of one calendar day after the date
            originally represented by changing the calling object.'''
        if self.isLeapYear() == False:
            if self.day == DAYS_IN_MONTH[self.month]:
                self.day = 1
                self.month += 1
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            else:
                self.day += 1
        else: #if not a leap year
            if self.month == 2:
                if self.day == 29:
                    self.day = 1
                    self.month += 1
                elif self.day == 28:
                    self.day += 1
                else:
                    self.day += 1
                    
            elif self.day == DAYS_IN_MONTH[self.month]:
                self.day = 1
                self.month += 1
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            else:
                self.day += 1
                
    def yesterday(self):
        '''Returns the date before the calling object.'''
        if self.isLeapYear() == False:
            if self.day == 1:
                if self.month == 1:
                    self.day = 31
                    self.month = 12
                    self.year -= 1
                else:
                    self.day = DAYS_IN_MONTH[self.month -1]
                    self.month -= 1
                    if self.month == 0:
                        self.month = 12
                        self.year -= 1
            else:
                self.day -= 1
        else: #if not a leap year
            if self.day == 1:
                if self.month == 3:
                    self.month -= 1
                    self.day = 29
                elif self.month == 1:
                    self.year -= 1
                    self.month = 12
                    self.day = 31
                else:
                    self.day = DAYS_IN_MONTH[self.month -1]
                    self.month -= 1
                    if self.month == 0:
                        self.month = 12
                        self.year -= 1
            else:
                self.day -= 1
        
    def addNDays(self, N):
        '''Changes the calling object to represent N calendar days after
            the date it originaly represented.'''
        if N >= 1:
            for i in range(0,N):
                print(self)
                self.tomorrow()
            print(self)
            
    def subNDays(self, N):
        '''Changes the calling object so that it represents N days before
            the original date.'''
        if N >= 1:
            for i in range(0,N):
                print(self)
                self.yesterday()
        print(self)

    def isBefore(self, d2):
        '''Tests id d2 before, after, or the same calendar date as the
            calling object. Self is: before = True, after/same = False.'''
        if self.year == d2.year and self.month == d2.month and \
           self.day < d2.day:
            return True
        if self.year == d2.year and self.month < d2.month:
            return True
        if self.year < d2.year:
            return True
            
    def isAfter(self, d2):
        '''Checks if the calendar date d2 is before, after, or the same
            as the calling object self. After returns true, the same or
            earlier date returns false.'''
        if self.year == d2.year and self.month == d2.month and \
           self.day > d2.day:
            return True
        if self.year == d2.year and self.month > d2.month:
            return True
        if self.year > d2.year:
            return True

    def diff(self, d2):
        '''Returns and integer representing the number of days between
            the dates self and d2.'''
        if self.equals(d2):
            return 0
        date1 = self.copy()
        date2 = d2.copy()
        days = 0
        while date1.equals(date2) == False:
            if date1.isBefore(date2):
                date1.tomorrow()
                days -= 1
            else:
                date2.tomorrow()
                days += 1
        return days 

    def dow(self):
        '''Returns a string indicating the day of the week of the object.'''
        weekday = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        day = self.diff(Date(11,9,2011))
        days = day % 7
        return weekday[days]
        
