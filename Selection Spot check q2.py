#Jeeson Baktha
#Selection Spot check
#8 October 2014

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
gender = input("Please enter your gender as M/F (male or female): ")

if gender == 'M':
    print("Mr {0} {1}".format(first_name, last_name))
elif gender == 'F':
    print("Ms {0} {1}".format(first_name, last_name))
else:
    print("The information you have entered is not valid")
