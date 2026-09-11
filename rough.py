# how to import a particular class from different file, and use it
# syntax : from {file_name} import {class_name}

from oops_demo_project import chatbook

# creating object 
# user1 = chatbook()

# difference between function and method

lst=[1,2,3]

# function --> isme hume data structure/parameters ko pass karte hai manually
a1 = len(lst)
print(a1)

# method --> isme hum object ko pakadkar, dot lagakr method call karte hai directly
user1 = chatbook()
user1.sendmsg()