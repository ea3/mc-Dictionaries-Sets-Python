fruit = {"orange": 'a sweet orange citrus fruit', "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

print(fruit["lemon"])


fruit["pear"] = "an odd shape apple"
fruit["mango"] = "a sweat pleasure"
fruit["zapote"] = "red inside"
# fruit[4] = "A number"
# fruit[("a car", "a house")] = "this is a tuple"
# print(fruit)
# del fruit[4]
# fruit.clear()
# print(fruit)
print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    #
    # description = fruit.get(dict_key,"We don't have a " + dict_key )
    # print(description)
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)

for snack in fruit:
    print(fruit[snack])

for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print("-"*40)

ordered_key = list(fruit.keys())
print(ordered_key)
ordered_key.sort()
print(ordered_key)
for i in ordered_key:
    print(i + " - " + fruit[i])




