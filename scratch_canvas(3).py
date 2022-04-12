def inputs():
    Name = input("Enter your name :")
    Surname = input("Enter your surname :")
    Mob_No = int(input("Enter the mobile number :"))
    a_string = str(Mob_No)
    length=len(a_string)
    
    if length == 10:
        print("a valid number")
    else:
        print("not a valid no")
    if length==10:
        Birth_Date =(input("Enter your birth date in dd-mm-yyyy format:"))
        Age = float(input("Enter your age with months after decimal point :"))#Convert the input such that it can accept float value)
        print("Form is submitted")
    else:    
        print("Not a valid number. Please enter a valid number")
        
    print(("\nThe details of the person are :\n","\nThe name is :\t", Name), ("\nThe surname is :\t",Surname) , ("\nThe mobile number is :\t",Mob_No) , ("\nThe birth date is :\t",Birth_Date ), ("\nThe age is :\t",Age))
   #print in line 19 is not working



inputs()       


