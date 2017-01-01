
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

three_list = []

for i in xrange(1, 1000):

    x3 = i % 3

    x5 = i % 5

    if x3 == 0 or x5 ==0:
        three_list.append(i)

print sum(three_list)

total_sum = 0
for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
print total_sum