def calculator(a:float,b:float,operator:str):
    if operator =="+":
        return a+b
    elif operator =="-":
        return a-b
    elif operator =="*":
        return a*b
    elif operator =="/":
        return a/b
    raise ValueError("Invalid operator")

# parsing convert string into numbers
def pars(a_str:str,b_str:str,operator:str):
    a = float(a_str) #Value error
    b = float(b_str) #Value error
    return calculator(a,b,operator)

#dialog
# def run():
#   try:
#       a = input("Enter first number: ")
#       b = input("Enter second number: ")
#       operator = input("Enter Action operator (+,-,*,/):  ")
#       result = pars(a,b,operator)
#       print(f"Result: {result}")
#   except ValueError as e:
#       print(f"Invalid input: {e}")
#   except ZeroDivisionError:
#       print(f"Cannot divide by zero")
# run()

def is_number(text):
    try:
        float(text)
        return  True
    except (TypeError,ValueError):
        return False
print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Kris"))
print(is_number(None))

print()

try:
    value = int("39")
except ValueError:
    print("An error occurred: ")
else:
    print("An error occurred: ", value)
finally:
    print("End of try")



