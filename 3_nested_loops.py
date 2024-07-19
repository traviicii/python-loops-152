# nested for loops

# a loop inside of a loop

nums = [1,2,3,4]
other = ['this', 'that', 'another thing']

for num in nums:
    print("this is my outer loop: ", num)
    for thing in other:
        print("This is my inner loop: ", thing)

print('='*50)

#-- Pizza topping combinations

pizza_type = ['deep dish', 'cicilian', 'NY stlye', 'Detroit']
toppings = ['pepperoni', 'sausage', 'ham', 'pineapple', 'olives']

for type1 in pizza_type:
    for topping in toppings:
        print("I have a ", type1, "pizza with", topping)

print('='*50)

for topping1 in toppings:
    for topping2 in toppings:
        if topping1 == topping2:
            print("Double", topping1)
        else:
            print(topping1, topping2)