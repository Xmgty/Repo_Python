# a = int(input("Введите число a:"))
# b = int(input("Введите число b: (a < b)"))
#
# for q in range (a, b+1):
#     print(q)


# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# if a < b:
#     for q in range(a, b + 1):
#         print(q)
# elif a > b:
#     for q in range(a, b - 1, -1):
#         print(q)

# a = int(input("Введите число a:"))
# b = int(input("Введите число b: (a > b)"))
# for q in range (a + (a%2-1), b - 1, -2):
#     print(q)

# summa = 0
# for q in range(0, 10, 1):
#     num = int(input("Enter a number "))
#     summa += num
# print(summa)


# N=int(input("Введите количество чисел "))
# num = int(input("Enter a number "))
# for q in range(0, N-1, 1):
#     num += int(input("Enter a number "))
# print(num)

# sum = 0
# N=int(input("Введите конечное число "))
# for q in range(1, N+1, 1):
#     z = q**3
#     sum = sum + z
# print(sum)

# N=int(input("Введите N "))
# fact=1
# for q in range(1, N+1, 1):
#     fact *= q
# print(fact)


# N=int(input("Введите конечное N "))
# fact = 1
# sum = 0
# for q in range(1, N+1, 1):
#     fact *= q
#     sum = fact + sum
# print(sum)

# N=int(input("Введите n "))
# sum=0
# for q in range(1, N+1, 1):
#     a = int(input("Enter number "))
#     if a==0:
#         sum+=1
# print(sum)

# N=int(input("Введите n (n<=9)"))
# f=0
# for q in range(1, N+1):
#     f = f*10+q
#     print(f)

# for q in range(10, 99):
#     if 2*((q//10)*(q%10)) == q:
#         print(q)


# for q in range(100, 999):
#     if (q*q)%1000==q:
#         print(q)

# n = int(input("Type n: "))
# for q in range(1, n+1):
#     print("+____", end=' ')
# for q in range(1, n+1):
#     print("|",q,"\b/", end=' ')
#     # print("|__\\")
#     # print("|   ")
