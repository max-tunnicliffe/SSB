

import datetime
def ObtainDate():
    isValid=False
    while not isValid:
        userIn = raw_input("Type Date dd/mm/yyyy: ")
        try: # strptime throws an exception if the input doesn't match the pattern
            d = datetime.datetime.strptime(userIn, "%d/%m/%Y")
            isValid=True
        except:
            print "Doh, try again!\n"
    return d
#test the function

bday = ObtainDate()
delta = bday.now() - bday
days = delta.total_seconds()*60*60*24
print("The number of seconds since you were born is ", delta.total_seconds())