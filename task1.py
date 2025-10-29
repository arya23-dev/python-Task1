def users_older_than_18(users):
    result = []
    for user in users:
        if user["age"] > 18:
            result.append(user["name"])
    return result

# Example list of users
users_list = [
    {"name": "Jaden", "age": 20},
    {"name": "Sam", "age": 17},
    {"name": "Alex", "age": 22}
]

print(users_older_than_18(users_list))
