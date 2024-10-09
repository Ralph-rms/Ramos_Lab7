name =input("enter your name")
age = int(input("enter your age"))
membership = input ("are you a member?")


if age <=18: 
    if membership == "yes":
        print ("your payment is 450.00 pesos")
    if membership == "no":
        print ("your payment is 650.00 pesos")
        
elif age >=18 and age <=65:
    if membership == "yes":
        print (" 550.00 pesos")
    if membership == "no":
        print (" 750 pesos") 
        
elif age >=65: 

    if membership == "yes":        
        print ("400")
    if membership == "no":
        print ("600")
        