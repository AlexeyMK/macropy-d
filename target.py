from macro_module import macros, d# , ct

name = "bob"
# print d[ct(name, age=5)]

age = 5
name = "bob"

person = {age: age, name: name}
person = {age, name}
person = dict(age=age, name=name)
#person = d[ct(age, name)]

person = d(age, name,
    other="stuff")
print person
# person = dict(age, name, other=5)
