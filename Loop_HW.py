## Problem 1: You work for a bakery that sells two items: muffins and cupcakes.
## The number of muffins and cupcakes in your shop at any given time is stored
## in the variables muffins and cupcakes which you will define, and the store
## has 10 muffins and 10 cupcakes.  Write a program that takes strings from
## standard input indicating what your customers are buying ("muffin" for a
## muffin, "cupcake" for a cupcake). If they buy a muffin, decrease muffins
## by one, and if they buy a cupcake, decrease cupcakes by 1. If there is no
## more of that baked good left, print ("Out of stock").  Once you are done
## selling, input "0", and have the program print out the number of muffins
## and cupcakes remaining, in the form "muffins: 9 cupcakes: 3" (if there were
## 9 muffins and 3 cupcakes left, for example).

# Start with 10 muffins and 10 cupcakes
muffins = 10
cupcakes = 10

# Keep asking the user what they want to buy
while True:
    item = input("What would you like to buy? (muffin or cupcake): ")

    # If the user types 0, stop the loop
    if item == "0":
        break

    # If the user wants a muffin
    if item == "muffin":
        if muffins > 0:
            muffins = muffins - 1  # reduce muffins by 1
        else:
            print("Out of stock")

    # If the user wants a cupcake
    elif item == "cupcake":
        if cupcakes > 0:
            cupcakes = cupcakes - 1  # reduce cupcakes by 1
        else:
            print("Out of stock")

    # If the input is not recognized
    else:
        print("Invalid item. Please enter 'muffin' or 'cupcake'.")

# After the loop ends, print how many are left
print("muffins:", muffins, "cupcakes:", cupcakes)
