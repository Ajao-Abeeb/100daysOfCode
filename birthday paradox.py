import datetime
import random
def getBirthdays(numberofBirthdays):
    "Returns a list of number random date objects for birthdays."
    birthdays=[]
    for i in range(numberofBirthdays):
        startOfYear = datetime.date(2001,1,1)
        #get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0,36))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
 

