#Input Outpout HW
# family size is 4
# whole pizza is 8 slices

a = 1
b = 2
c = 3
d = 3

# Calculate the total number of slices eaten, total whole pizzas needed, and leftovers.
total_slices_eaten = (a + b + c + d)
whole_pizzas = total_slices_eaten // 8
leftovers = total_slices_eaten % 8

print('Test Case 4 - The number of slices each family member eats is 1, 2, 3, 3')
print("Total number of slices that will be eaten:", total_slices_eaten)
print("Total whole pizza to order:", whole_pizzas)
print("There will be", leftovers,"slices left over.")
