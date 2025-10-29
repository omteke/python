fruits = ["cherry","Apple","pear"]
# Accessing Items in Lists
print(fruits[0])
# negative indices
print(fruits[-1])
# modifying items
fruits[0] = "Orange"
print(fruits)

# Adding items
fruits.append("mango")
print(fruits)

fruits.extend(["pineapple","banana",2])
print(fruits)

fruits.insert(1,"chiku")
print(fruits)

fruits.remove("Apple")
print(fruits)

fruits.pop(1)
print(fruits)

