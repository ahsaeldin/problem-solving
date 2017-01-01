import time

# https://projecteuler.net/problem=5

## really really really cute learning here

## the whole idea is to get a number that can be evenly divided by all the smaller number under this number

## there the stright way as in my_way by checking every number. this would help till number 16, then it takes minutes

## the second way is to use prime number, yeah, the fucken prime numbers that almost everywhere, I mean everywhere.

## the idea is simple, for number 10,
    # get all its prime factors
    # then, create another list contains the remaining non-prime numbers under this number (10 in this case)
    # then, get the prime factors for each one, if not the whole list of numbers in the main list is there then add them

    # for ex: Numeber 10:
    # Step 1: 2,3,4,5,6,7,8,9, 10
    # Step 2: loop through each one above and get prime factors or if prime already
    # Step 3: you have two lists now, one conatains list of lists compoiste number factored
    # and the second is the final required list (not ready yet) contains all prime numbers for the target number
    # Step 4: loop though each list of the second list, (list of lists)
    # Step 5: Make a set of each list in the list of lists
    # Step 6: Compare the count of each number in the set in both the final list and the list in the loop
    # Step 7: if the final list is less then


def my_way(number):

    a, base = number, number # change both to the number you want

    while True:

        #print a

        not_found = False

        for i in xrange(1, base + 1):
            if a % i != 0:
                not_found = True
                break

        if not not_found:
            print 'LCM: ' + str(a)

            break

        a += 1

# ----------------------------------------------------------------------------------

# like above with a few FUCKEN lines
def Bruteforce(number):

    from itertools import count
    for i in count(number):
        if all(map(lambda x: i % x == 0, range(1, number + 1))):
            print i
            break

# ----------------------------------------------------------------------------------


def is_prime(n):
    return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n > 1


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def math_way(number):

    c_list = []  # holds lists of primes factors of non prime numbers -- explain later
    p = [x for x in xrange(2, number + 1)]  # first get all the numbers under this number with this number in a list.
    f = []  # holds the target numbers

    for i in xrange(2, number + 1):  # loop through each number under the target number
        l = primes(i)  # check if prime
        if len(l) == 1:  # this is a prime number, remove from p list and add to the final list
            p.remove(i)
            f.append(i)
        else:
            c_list.append(l)  # No, this is a non prime number -- composite number

    for ll in c_list:  # for each list in the c_list:
        ll_set = set(ll)  # get a set of all unique number in every list
        for l in ll_set:  # then loop through every list
            # here is our line, the master scene...
            # using the set above (ll_set), check the count of every number inside
            # if the count of that number in the final list is less than the count
            # in factorized list (l), then append it to the final list.
            dd = ll.count(l)
            ddd = f.count(l)
            if f.count(l) < ll.count(l):
                f.append(l)

    print 'LCM: ' + str(reduce(lambda x, y: x*y, f))

# ----------------------------------------------------------------------------------

print ' '
start_time = time.clock()
math_way(20)
print 'Math Way:' + str(time.clock() - start_time), "seconds -- A7A"

print '\n#################################################\n'

start_time = time.clock()
my_way(15)
print 'My First Shot: ' + str(time.clock() - start_time), "seconds -- A7A2N"

