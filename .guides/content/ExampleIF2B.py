#Note - for the purpose of this example driving age is assumed at 16 years

age = 14

# mulitple condition statment 
if age ==16:
    print ('you can get your license')
elif age < 16:
    print ('you are too young to get your license')
else:
    print ('you already have your license')

    
age = 15    
# nested if statment
# this may not be as simple as one above but is for demonstration purposes
# main if statment just checks if 16 or not
# if not 16 then the nested checks for less than or greater
if age ==16:
    print ('you can get your license')
else:
     if age < 16:
        print ('you are too young to get your license')
     else:
        print ('you already have your license')   