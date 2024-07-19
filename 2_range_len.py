
# range(stop) : creates a sequence of numbers that we can iterate through

print(list(range(11)))

for num in range(11):
    print(num)

# range(start, stop) : creates a sequence of numbers from start (inclusive) to stop (non-inclusive)

print("Range of numbers from 5-10")
list_of_nums = []

for num in range(5, 11): # Creating a list on nums between 5-10 with a for loop
    # print(num)
    list_of_nums.append(num)

print(list_of_nums)


list_of_nums = list(range(5,11)) # creating a list on nums by type casting my range sequence into a list
print(list_of_nums)

print(type(range(5,11)))

# range(start, stop, step) : creates a range of numbers from start to stop every step-th number (nth number)

print("Printing a range of numbers from 10 to 100, every 10th digit")
for num in range(10, 101, 10):
    print(num)

print("Printing only the even numbers, from 0 to 20")
for num in range(0, 21, 2):
    print(num)

print("Printing only even numbers from 20 to 0")
for num in range(20, 0, -2):
    print(num)

print('='*50)

#-- range() in combination with len()

#indecies   0        1        2        3
alist = ['item1', 'item2', 'item3', 'item4']

print(len(alist))
length_of_list = len(alist)

# print(alist[2])

print('='*50)

for index in range(len(alist)):
    print(index, alist[index])

print('='*50)

food = ['tacos', 'tiramisu', 'pizza', 'sushi', 'burger', 'salad', 'burger', 'key lime pie']

for index in range(len(food)):
    if food[index] == 'burger':
        print("Burger position: ", index)

print('='*50)

students = ['John', 'Jim', 'Jane', 'Jill']
grades = [98, 84, 76, 100]
activities = ['Football', 'Woodshop', 'Art', 'Debate Team']

for index in range(len(students)):
    print(students[index], "has a grade of", grades[index], "and likes", activities[index])

print('='*50)

# grouped_info = zip(students, grades, activities)
# print(grouped_info)

for item in zip(students, grades, activities):
    # print(item)
    print(item[0], "has a grade of", item[1], "and likes", item[2])