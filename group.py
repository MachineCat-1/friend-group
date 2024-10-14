rows = [{ "name": "Jason", "job": "students", "age": "21"}, 
        { "name": "Jenny", "job": "students", "age": "22"},
        ]

for row in rows:
    print(f"{row["name"]} is {row["age"]}, a {row["job"]}" )