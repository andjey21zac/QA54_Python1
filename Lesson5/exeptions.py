with open("user.json","r",encoding="utf-8") as file:
    print(file.read())

print("Hello World")
result = 10/0
print(result)
print("Bye World")

def  div_int(a,b):
    return a/b
print("start program")
result = div_int(10,0)
print(result)
print("end program")

# try/exept
print("Hello")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("An error occured: ",e)
print("BY")

try:
    number = int(input("enter a number: "))
    result = 100/number
    print("Result: ",result)
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")





