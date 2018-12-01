Terms = int(input("How many terms? "))
#Assigns the variable Terms to an integer input.
OP = 1
#Assigns the variable OP to 1.
Series = 1-1/3
#Assigns the variable Series to the value of 1-1/3.
Den = 5
#Assigns the variable Den to the value of 5.
for i in range(Terms):
#Loops the following code the number of terms the user selects.
    if OP == 1:
    #If OP is equal to 1 the following code will execute.
        Fraction = 1/Den
        #The variable fraction is assigned to the value of one divided by Den.
        Series += Fraction
        #The variable fraction is added to the variable series.
        OP = 2
        #The variable OP is assigned the value of 2.
    elif OP == 2:
    #If OP is equal to 2 the following code will execute.
        Fraction = 1/Den
        #The variable Fraction is assigned to the value of one divided by Den.
        Series -= Fraction
        #The variable Fraction is subtracted fromthe variable Series.
        OP = 1
        #The variable OP is assigned to the value of 1.
    Den += 2
    #The variable Den is increased by 2.
print(Series*4)
#The value of the variable Series multiplied by 4 is outputed.


    

