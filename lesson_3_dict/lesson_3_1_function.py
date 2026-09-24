def  greet(name):
    return f"Hello,{name}!"
result = greet("Andrey")
print(result)


# result2 =  greet()
# print(result2)

def create_user(name,role ="user"):
    return {"name":name,"role":role}
print(create_user("Alex"))
print(create_user("Kristina","admin"))

print()
def cal_discount(price,discount = 20):
    return price - (price*discount/100)
print(cal_discount(2000))
print(cal_discount(2000,25))

# def foo(a=2,b=5):
#     return  a+b
# print(foo(5))

def add_tests(name,results=None):
    if results is None:
        results = []
    results.append(name)
    return results
print(add_tests("test_registration"))
print(add_tests("test_login"))

def create_user2(username,email,role):
    return f"{username}-({email})-{role}"
print(create_user2("Kris","test@gm.com","TeamLead"))

print(create_user2(role="Project",email="test2@gm.com",username="Alex"))

print(create_user2(username="Kristina",email="qa@gm.com",role="QA"))








