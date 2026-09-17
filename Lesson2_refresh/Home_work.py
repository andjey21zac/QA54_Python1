def clean_name(name):
    return name.strip().title()
print(clean_name(" anna smith  "))

def normalize_email(email):
    return email.strip().lower()
print(normalize_email("  Anna Smith@Exampel.COM"))

def is_python_file(filename):
    return filename.lower().endswith(".py")
print(is_python_file("lesson.py"))
print(is_python_file("HOMEWORK.PY"))
print(is_python_file("notes.txt"))

def fix_message(message):
    return message.replace("bad","good")
message = "bad weather, bad mood"
result = fix_message(message)
print(result)
print(message)

def count_letter(text,letter):
    return text.lower().count(letter.lower())
print(count_letter("Programing","g"))
print(count_letter("Missisipi","I"))

def create_login(first_name,last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    return f"{first_name.strip().lower()},{last_name.strip().lower()}"
print(create_login("  Anna Smith  "))

