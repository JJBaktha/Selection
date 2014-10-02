#Jeeson Baktha
#Selection Development 2
#1 October 2014

water_temp = float(input("Please enter the temperature of the water in centigrade to see if it is frozen, boiling or neither: "))

if water_temp < 100 > 0:
    print("The water is still liquid.")
if water_temp < 0:
    print("The water is solid. It is frozen.")
if water_temp > 100:
    print("The water is boiling. It is becoming a gas")
