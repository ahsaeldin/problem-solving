# http://www.mathsisfun.com/prime-factorization.html

# n = 600851475143
# i = 2
#
# while i * i < n:
#     while n % i == 0:
#         n = n / i
#     i = i + 1
#
# print (n)

n = 4
factor = 2
lastFactor = 1
while n > 1:
    if n % factor == 0:
        lastFactor = factor
        n = n / factor
        while n % factor == 0:
            n= n / factor
    factor=factor + 1
print lastFactor


