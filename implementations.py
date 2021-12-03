# Complete exercises 1a, 1b, 1c, 2 HERE!

#1a: Tuple
months_of_the_year = ("January", "February", "March", "April", "June", "July", "August", "September", "October", "November", "December")
print(f"Pi Day exists in {months_of_the_year[2]}!")

#1b: Set
fruits_and_vegetables = {"Strawberry", "Grape", "Melon", "Celery", "Lemon"}
fruits_and_vegetables.update(["Orange", "Plum", "Carrot", "Cucumber"])
for item in fruits_and_vegetables:
    print(item)

#1c: Dictionary
user_profile = {
    "first_name": "John",
    "last_name": "Johnson",
    "email_address": "johnjohn@me.com",
    "phone_number": "414-414-4144"
}
print(user_profile["first_name"]) # or user_profile.get("first_name")

#2: Dictionary/list
family_members = []
member_one = {
    "first_name": "Lynn",
    "last_name": "Pavlic",
    "relation_to_me": "Mother"
}
member_two = {
    "first_name": "Greg",
    "last_name": "Pavlic",
    "relation_to_me": "Father"
}
member_three = {
    "first_name": "Megan",
    "last_name": "Pavlic",
    "relation_to_me": "Sister"
}
member_four = {
    "first_name": "Katie",
    "last_name": "Pavlic",
    "relation_to_me": "Sister"
}
member_five = {
    "first_name": "Tyler",
    "last_name": "Pavlic",
    "relation_to_me": "ME"
}
family_members.append(member_one)
family_members.append(member_two)
family_members.append(member_three)
family_members.append(member_four)
family_members.append(member_five)
print(family_members[4]["first_name"])