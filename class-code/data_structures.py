
colors = ["red", "yellow", "green"]

print(colors)

# accessing elements: arr[index]

print(colors[2])


# we can also go backwards

print(colors[-1])



colors[0] = "purple"

print(colors)


# push == append()
# add to the end
colors.append("pink")

print(colors)


students = ["Sayed","Yusef","Israa"]
# append() only adds 1 value.
# if i want to add more than 1 value I use extend

students.extend(['nooreen','sara'])

print(students)


# we can also insert at an index with insert() method
# insert(): adds an element at an index
students.insert(0,"Ahmad")

print(students)


print(len(students))


# pop(): removes the last element

students.pop()

print(students)


# pop can take an arguement. the index
students.pop(3)

print(students)