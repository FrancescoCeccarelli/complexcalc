from statistics import mean
import math
import time

class operations():
    def pi(num):
        return math.pi * num
    def sen(num, deg):
        return num * math.sin(math.radians(deg))
    def cos(num, deg):
        return num * math.cos(math.radians(deg))
    def tan(num1, deg):
        return num1 * math.tan(math.radians(deg))
    def sqared(num1):
        return math.sqrt(num1)
    def pythagoras(num1, num2):
        return math.sqrt(pow(num1, 2) + pow(num2, 2))
    def pow(num, exp):
        return pow(num, exp)

def start():
   operation = input("1)espression\n2)num*pi\n3)num*sin(x)\n4)num*cos(x)\n5)num*tan(x)\n6)sqrt of a number\n7)power\n8)pythagoras\n(1-8): ")

   if operation == "1":
       esp = input("esp: ")
       print(eval(esp))

       time.sleep(3)
       start()

   if operation == "2":
       num1 = float(input("num: "))
       pi = str(operations.pi(num1))
       print(str(num1) + " * 3.14... = " + pi)
       
       time.sleep(3)
       start()

   if operation ==  "3":
       num1 = float(input("num: "))
       deg = float(input("deg: "))
       print(str(num1) + "sin(" + str(deg) + ") = " + str(operations.sen(num1, deg)))

       time.sleep(3)
       start()

   if operation == "4":
       num1 = float(input("num: "))
       deg = float(input("deg: "))
       print(str(num1) + "cos(" + str(deg) + ") = " + str(operations.cos(num1, deg)))

       time.sleep(3)
       start()

   if operation == "5":
       num = float(input("num: "))
       deg = float(input("deg: "))
       print(str(num) + "tan(" + str(deg) + ") = " + str(operations.tan(num, deg)))

       time.sleep(3)
       start()
   
   if operation == "6":
       num = float(input("num: "))
       print("sqrt = " + str(operations.sqared(num)))
       
       time.sleep(3)
       start()
   
   if operation == "7":
       num1 = float(input("num: "))
       exp = float(input("exp: "))
       print(str(operations.pow(num1, exp)))

       time.sleep(3)
       start()

   if operation == "8":
       num = float(input("num1: "))
       num1 = float(input("num2: "))
       print(str(operations.pythagoras(num, num1)))
       
       time.sleep(3)
       start()

print("-it wont give the correct result with 90deg on sin, cos, tan. I am working on it-")

if __name__ == "__main__":
    start()
