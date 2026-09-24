from http.client import responses

books = {'Lev Tolstoy': 'Anna Karenina',
         'Anton Chekhov': 'The Cherry Orchard',

         }
books2 = {
    'Lev Tolstoy',
    'Anton Chekhov'
}
print(books2)

response = {
    'statusCode': '200',
    'user': {
        'id':1, 'name':'Kristina'
    }
}
print(response['user']['name'])

data = [1,2,33]
print(isinstance(data,list))

value = 22
print(isinstance(value,int))
print(isinstance(value,float))

team_age = {
    "Kristina": 39,
    "Alex": 40,
    "Tatiana": 44,
    "vladimir": 65
}
print(
    team_age.keys()
)
print(team_age.values())

team_names = "Kristina","Alex","Tatiana","Andrey","Vladimir"
team_num = [39,40,54,44,65]
team_age ={name:age for name ,age in zip(team_names,team_num)}
print(team_age)
