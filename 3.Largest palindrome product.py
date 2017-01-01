# http://stackoverflow.com/questions/21286890/find-the-largest-palindrome-made-from-the-product-of-two-3-digit-numbers-javas

# three_digits_palindrome = []
#

import time
import timeit

def isPalindrome(num):
    return str(num) == str(num)[::-1]

# ---- My Way

def MyWayFuckSoPathic():
    def factors(n):
        return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

    maximum = 999 * 999
    minimum = 900 * 950

    listo = []
    for i in xrange(maximum, minimum, -1):
        if isPalindrome(i):
            print i
            all_factors = factors(i)
            first = [999 > x > 100 for x in all_factors][0]
            if first and i % first == 0 and i / first <= 999:
                return i


def FirstWayInPDF():
    largestPalindrome = 0
    a = 100
    while a <= 999:
        b = 100
        while b <= 999:
            if isPalindrome(a * b) and a * b > largestPalindrome:
                largestPalindrome = a * b
            b = b + 1
        a = a + 1
    return largestPalindrome

def SecondWayInPDF():
    largestPalindrome = 0
    a = 100
    while a <= 999:
         b = a
         while b <= 999:
              if isPalindrome(a*b) and a*b > largestPalindrome:
                   largestPalindrome = a*b
              b = b + 1
         a = a + 1
    return largestPalindrome


def ThirdWayInPDF():
    largestPalindrome = 0
    a = 999
    while a >= 100:
         b = 999
         while b >= a:
              if a*b <= largestPalindrome:
                   break #Since a*b is always going to be too small
              if isPalindrome(a*b):
                   largestPalindrome = a*b
              b = b - 1
         a = a - 1
    return largestPalindrome


def fastestwayinthepdf():
    largestPalindrome = 0
    a = 999
    while a >= 100:
        if a % 11 == 0:
            b = 999
            db = 1
        else:
            b = 990 # The largest number less than or equal 999 and divisible by 11
            db = 11

        while b >= a:
            if a * b <= largestPalindrome:
                break
            if isPalindrome(a * b):
                largestPalindrome = a * b
            b = b - db
        a = a - 1
    return largestPalindrome

start_time = time.clock()
largestPalindrome = FirstWayInPDF()
print time.clock() - start_time, "seconds --- " + str(largestPalindrome)

start_time = time.clock()
largestPalindrome = SecondWayInPDF()
print time.clock() - start_time, "seconds --- " + str(largestPalindrome)

start_time = time.clock()
largestPalindrome = ThirdWayInPDF()
print time.clock() - start_time, "seconds --- " + str(largestPalindrome)

start_time = time.clock()
largestPalindrome = fastestwayinthepdf()
print time.clock() - start_time, "seconds --- " + str(largestPalindrome)