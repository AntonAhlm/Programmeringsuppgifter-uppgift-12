enhet=int(input("Skriv 1 for att omvandla fran Celsius till Fahrenheit, och 2 for att omvandla fran Fahrenheit till Celsius :"))

if enhet==1:
    temp1=int(input("Temperatur i Celsius: "))
    temp2=9/5*temp1+32
    print(temp1,"grader celsius blir",temp2,"grader fahrenheit")

if enhet==2:
    temp1=int(input("Temperatur i Fahrenheit: "))
    temp2=(temp1-32)/(9/5)
    print(temp1,"grader fahrenheit blir",temp2,"grader celsius")
