person = {
    "name": "Keenan",
    "age": 22,
    "hometown": "Omaha, NE"
}

print(f'''
Hi, my name is {person.get("name")}. I am {person.get("age")} years old and I come from {person.get("hometown")}.
''')
