import os
import sys
import math

def clean():
    os.system('cls')

def calc(a, b, c):
    print (" x = (" + str(a) + "x²) + (" + str(b) + "x) + (" + str(c) + ") = 0 \n")
    print (" Δ = b² - 4 * a * c")
    print (" Δ = (" + str(b) + ")² - 4 * ("+ str(a) + ") * (" + str(c) + ") ")
    delta = ((b*b) - (4*a*c))
    print (" Δ = " + str(delta) + "\n")
    equation(a, b, c, delta)
    result(a, b, c, delta)

def equation(a, b, c, delta):
    print(" x   = (b ± √(Δ))/(2*a)\n")
    print(" x   = (" + str(b) + " ± √(" + str(delta) + "))/(2*" + str(a) + ")\n")

def result(a, b, c, delta):
    if(delta <= 0):
        aux_a = (2*a)
        print(" x'  = (" + str(b) + " + √(" + str(delta) + "))/(" + str(aux_a) + ")")
        print(" x'' = (" + str(b) + " - √(" + str(delta) + "))/(" + str(aux_a) + ")\n")

    else:
        aux_a = (2*a)
        r = math.sqrt(delta)
        aux_b1 = (b + r)
        aux_b2 = (b - r)
        result1 = (aux_b1/aux_a)
        result2 = (aux_b2/aux_a) 
        print(" x'  = (" + str(aux_b1) +")/(" + str(aux_a) + ") = " + str(result1))
        print(" x'' = (" + str(aux_b2) +")/(" + str(aux_a) + ") = " + str(result2)+ "\n")

clean()
i = 0
while (i == 0):
    clean()
    a = int(input(" Enter the value of A: "))
    b = int(input(" Enter the value of B: "))
    c = int(input(" Enter the value of C: "))
    clean()
    calc(a, b, c)
    q = (input(" Do you want to calculate again? (Y to YES/Any key to NO): "))
    q = q.upper()
    if ((q != "Y")):
        i = 1
        clean()

