import requests
from pprint import PrettyPrinter

printer = PrettyPrinter()

response = requests.get("https://randomuser.me/api")
print(f"Status Code > {response.status_code}\n")
# printer.pprint(response.json())

results = response.json()['results']
# printer.pprint(results)

email = response.json()['results'][0]['email']
print(f"Eamil    : {email}")

id_name = response.json()['results'][0]['id']['name']
id_value = response.json()['results'][0]['id']['value']
id =id_name + " " + id_value
print(f"ID       : {id}")

gender = response.json()['results'][0]['gender']
print(f"Gender   : {gender}")

firstname = response.json()['results'][0]['name']['first']
lastname = response.json()['results'][0]['name']['last']
title = response.json()['results'][0]['name']['title']
name = title + "." + firstname + lastname
print(f"Name     : {name}")

username = response.json()['results'][0]['login']['username']
print(f"Username : {username}")