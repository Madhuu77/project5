import random                             #
def Generate_otp():                       #defining a function called Generate otp
    otp=""                                #naming the variable as string 
    for i in range(6):                    #using loop for 6 digit iteration 
        otp+=str(random.randint(0, 9))    #converted to string 
    return otp                            #after efter every single loop returning the Value

#i am playing here with you for guessing the generated otp
guess=input("guess the 6 digit otp.")   #gettinthe input from the user 
if guess==Generate_otp():               #conditional Statement
    print("!!you got it right")
else:                                   #else statement
    print("Betterluck next time.")
print("The Generatedd OTP is:",Generate_otp()) #actual generation of otp
