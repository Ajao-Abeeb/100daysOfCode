# import datetime
# import random
# def getBirthdays(numberofBirthdays):
#     "Returns a list of number random date objects for birthdays."
#     birthdays=[]
#     for i in range(numberofBirthdays):
#         startOfYear = datetime.date(2001,1,1)
#         #get a random day into the year
#         randomNumberOfDays = datetime.timedelta(random.randint(0,36))
#         birthday = startOfYear + randomNumberOfDays
#         birthdays.append(birthday)
#     return birthdays
def birthdayParadox(num_people):
    '''Function that calculates the probability of two people 
    in a given group of num_people having the same birthday.
    
    Parameters:
        :num_people int: The number of people in the group
        
    Returns:
        float: The probability that at least two people in the group have the same birthday 
    '''
    prob = 1
    for i in range(num_people):
        prob *= (365-i)/365
    prob = 1-prob

    print(int(prob))

birthdayParadox(234)
