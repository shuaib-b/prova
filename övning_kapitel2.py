#Kapitel 2
#Uppgift 1
"""def main () :
    print("Det här programmet omvandlar temperaturen från celsius till fahrenheit")
    celsius = float(input ("What is the Celsius temperature? ") )
    fahrenheit = 9/5 * celsius + 32
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.")
main ()

#Uppgift 3
def main () :
    print ("This program computes the average of three exam scores.")
    score1, score2, score3 = eval(input ("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3)/3
    print ("The average of the scores is: ", average)
main ()

#Uppgift 4
def main () :
    for i in range(5):
        celsius = eval (input ("What is the Celsius temperature? ") )
        fahrenheit = 9/5 * celsius + 32
        print ("The temperature is", fahrenheit, "degrees Fahrenheit.")
main ()

#Uppgift 5
print("celsius fahrenheit")
for celsius in range(0,101,10):
    fahrenheit = 9/5 * celsius + 32
    print(celsius,"℃",fahrenheit, "℉")"""

#Uppgift 6
def main () :
    print ("This program calculates the future value")
    print ("of an n-year long investment.")
    principal=eval (input ("Enter the initial principal: ") )
    apr=eval (input ("Enter the annual interest rate: ") )
    n=eval(input("Enter the amount of years you are investing: "))
    for i in range (n) :
        principal = principal * (1 + apr)
    print (f"The value in {n} years is:  {principal}")
main () 


    
