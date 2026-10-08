#dumps() - python -> json str
#loads() - json -> python object
#dump () - save Python object -> file.json
#load() - file.json ->> Python (file)
import json

user ={"username":"kristina","age": 25,"is_admin":True}
json_str = json.dumps(user)
print(json_str)
print(type(json_str))


user ={"username":"kristina","age": 25,"is_admin":True}
user = json.loads(json_str)
print()
print(user)
print(type(user))
print(user["username"])
print()

test_config = {"url":"http://127.0.0.1:8000","username":"Kristina","password":"Aa123456","timeout":20}

with open("config.json","w",encoding="utf-8") as file:
    json.dump(test_config,file,indent=4,ensure_ascii = False)

with open("config.json","r",encoding="utf-8") as file:
    config = json.load(file)
    print(config)
    print(config["url"])
    print(config["username"])
    print(config["password"])
    print(config["timeout"])
print()

def save_profile(name,age,city):
    profile = {"name":name,"age":age,"city":city}
    
    with open("profile.json","w",encoding="utf-8") as file:
        json.dump(profile,file,indent=2)
save_profile("Kris",39,"Rishon")





