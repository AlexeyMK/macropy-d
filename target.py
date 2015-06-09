from macropy.d import macros, d

age = 5
name = "bob"

# lets make some dictionaries.
print {"age": "age", "name": name, "style": "literal"}
print dict(age=age, name=name, style="dict")

# and now with d
print d(age, name, style="short")
