def highest_number (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        highest = num1
    elif num2 >= num1 and num2 >= num3:
        highest = num2
    else:
        num3 = highest
return highest
numero1 = int(input ("enter the first number: "))
numero2 = int(input ("enter the second number: "))
numero3 = int(input ("enter the third number: "))
print ("el mayor numero es: " + str(highest_number(numero1, numero2, numero3)))