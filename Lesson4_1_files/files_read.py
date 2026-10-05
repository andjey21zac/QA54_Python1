with open("user.txt","w",encoding="utf-8") as file:
    file.write("Andrey\n ")
    file.write("Alex\n ")

with open("user.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(len(content))

with open("user.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    print()
    for line in lines:
        print(line.strip())


with open("user.txt","r",encoding="utf-8") as file:
    for line in file:
        print(line.strip())




