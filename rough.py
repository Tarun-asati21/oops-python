# how to import a particular class from different file, and use it
# syntax : from {file_name} import {class_name}

from oops_demo_project import chatbook

# creating object 
# user1 = chatbook()

# # difference between function and method

# lst=[1,2,3]

# # function --> isme hume data structure/parameters ko pass karte hai manually
# a1 = len(lst)
# print(a1)

# # method --> isme hum object ko pakadkar, dot lagakr method call karte hai directly
# user1 = chatbook()
# user1.sendmsg()


# encapsulation 
# user1 = chatbook()
# how to access a hidden encapsulated attribute 
# syntax : {object_name}._{class_name}__{attribute_name}
# print(user1._chatbook__name)

# getter and setter
# print(user1.get_name()) # accessing the hidden attribute by GETTER function
# user1.set_name("Yashu") # setting the hidden attribute by SETTER function
# print(user1.get_name())

# creating multiple users 
# user1 = chatbook()
# print(user1.id)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

# using static method directly from class name, rather than object
# user1 = chatbook()
# print(user1.id)

# chatbook.set_id(21) # manually setup id to 21

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)