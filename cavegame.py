locations = {0: "You are sitting in the front of your computer",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are the top of the hill",
             3: "You are inside a building a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: " You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5,"S": 4, "Q": 0},
         {"N": 5, "Q":0},
         {"W": 1, "Q":0},
         {"N": 1, "W":2, "Q":0},
         {"W":2, "S":1, "Q":0}]

loc = 1

while True:
    available_exits = ""
    for direction in exits[loc].keys():
        available_exits += direction + ", "

    print(locations[loc])

    if loc ==0:
        break

    direction = input("Available exitst are " + available_exits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You can't go in that direction")