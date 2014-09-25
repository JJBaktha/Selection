# Jeeson Baktha
# 24 September 2014
# PythonSchool 'if'

print("This program will test to see if you are old enough to vote and caculate years remaining untl you can retire")
age = int(input("Please enter your age:"))

if age >=18:
    print("You are old enough to vote")
else:
    print("You are too young to vote")

retirement = 65 - age

print("You have {0} years remaining until retirement".format(retirement))

print("Thank you for using this program")
