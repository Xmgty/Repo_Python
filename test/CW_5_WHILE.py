# x=1
# while x <=10:
#     if x%2==0:
#         print(x)
#     x+=1

#
# count_access = 1
# while count_access <=3:
#     login = input("Enter login: ")
#     passwd = input("Enter password: ")
#
#     if login == 'st' and passwd == "102":
#         print("Access is granted")
#         break
#     else:
#         print("Access is denied")
#     count_access+=1
#


#
# N = int(input("Введите число:"))
# a = 1
# while a < N:
#     print(a**2)
#     a+=1
#

#############################################################

# n=int(input('Enter number (n>=2) '))
# x=2
# while x<=n:
#     if n%x==0:
#         print(x)
#         break
#     else:
#         x+=1

#####################################################################


# N = int(input("Введите число:"))
# count = 0
# a = 2
# if N < 2:
#     print(count)
# while a <= N:
#     N = N//a
#     count+=1
# print(count)

#################################################################


# x = float(input("Введите число:"))
# y = float(input("Введите число:"))
# days = 1
#
# while x <= y:
#     x= x+x*0.1
#     days+=1
#     print(x)
# print(days)

#######################################################

# a = 1
# count = 0
# while a != 0:
#     N = int(input("Введите число:"))
#     if N == 0:
#         a = 0
#         break
#     count+=1
# print(count)

####################################################

# a = 1
# count = 0
# sum = 0
# average = 0
# max = 0
# index = 0
# maxin = 0
# count_f = 0
# temp = 100000000
# count_b = 0
# max2 = 0
# count_max = 0
# while a != 0:
#     N = int(input("Введите число:"))
#     if temp < N:
#        count_b+=1
#     temp = N
#     if N == 0:
#         a = 0
#         break
#     if max < N:
#         max = N
#         maxin = index
#     if max2 < max and max2 < N and max > N:
#         max2 = N
#     count+=1
#     index +=1
#     sum = sum + N
#     average = sum/count
#     if N%2 == 0:
#         count_f+=1
#     if max == N:
#         count_max+=1
# print(count)
# print(sum)
# print(average)
# print("MAX:", max)
# print("MAX2:", max2)
# print(maxin)
# print(count_f)
# print(count_b)
# print("MAXCOUNT", count_max)

####################################################

# n = int(input("Enter num: "))
# a = n
# x = 1
# count = 0
# while count < n:
#     a += n - x
#     x+=1
#     count+=1
# print(a)



# n = int(input("Enter num: "))
# A = int(input("Enter num: "))
# a = n
# x = 1
# count = 0
# count2 = 1
# want = 0
# while count < n:
#     a += n - x
#     x+=1
#     count+=1
#     if A == a:
#         print(count)
#         want = 1
#     else:
#         count2 = -1
# if want == 0:
#     print(count2)


n = int(input("Enter num: "))
MAX = n
count_a = 1
count_b = 1

while n!= 0:
    if MAX == n:
        count_a+=1
    elif count_a > count_b:
        count_b = count_a
        count_a = 1
    else:
        count_a = 1
    n = int(input("Enter num: "))
if count_a > count_b:
    print(count_a)
else:
    print(count_b)











