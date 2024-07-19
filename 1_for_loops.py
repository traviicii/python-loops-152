# Intro to For Loops 

# for loops allow us to execute a code block for every item in an iterable (strings, lists, ...)

# they allow us to repeat code a limited number of times (number of times is determined by the size of the iterable)

# Syntax of for loops
# for item in iterable:
#       Code block

flavors = ['vanilla', 'chocolate', 'cookies n cream', 'caramel', 'orange sherbet']

for flavor in flavors:
    # print("running this code block")
    # print(flavor)
    print("Tasting the", flavor, "flavor!")

# as we loop over an iterable we get to isolate each item and can choose to do something with that item or not

print('='*50)

guest_list = ['Dylan', 'Travis', 'Christian', 'Sarah', 'Shoha']

line = ['Adam', 'Craig', 'Dylan', 'Travis', 'Christian', 'Billy Bob']

# door man for loop

for person in line:
    print("*", person, "walks up to the bouncer *")
    if person in guest_list:
        print("Welcome to the party!!")
    else:
        print("Get outta here!! You're not on the guest list tonight!")
    print('='*50)


print('='*50)

submitted = ['Alice', 'Bob', 'Charlie', 'David']
attended = ['Charlie', 'Eve', 'Alice', 'Frank']

for student in submitted:
    if student in attended:
        print(student, "submitted their HW and attended class.")
    else:
        print(student, "submitted their HW but didn't attend class. :(")

print('='*50)

nums = [12, 234, 567, 98, 34, 1234567, 246, 178, 15326]

for num in nums:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

print('='*50)

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

above_100 = []

for temp in temperatures:
    if temp > 100:
        above_100.append(temp)

print(above_100)