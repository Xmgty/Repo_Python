# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a > b:
#     print(b)
# elif b > a:
#     print(a)
#################################################

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if a >= b > c:
#     print(c)
# elif a >= c > b:
#     print(b)
# elif b >= c > a:
#     print(a)
# elif b >= a > c:
#     print(c)
# elif c >= a > b:
#     print(b)
# elif c >= b > a:
#     print(a)
# elif c == b == a:
#     print(a, "Все числа равны")

#######################################################

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)
#####################

a = int(input("Введите номер столбца от 1 до 8: "))
b = int(input("Введите число от 1 до 8: "))
c = int(input("Введите номер столбца от 1 до 8: "))
d = int(input("Введите число от 1 до 8: "))
if (a + b) % 2 == 0:
    numb1=1
else:
    numb1=0
if (c + d) % 2 == 0:
   numb2=1
else:
    numb2=0
if numb1 == numb2:
    print("yes")
else:
    print("no")
###################

# a = int(input("Введите год: "))
# if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
#     print("yes")
# else:
#     print("no")
################

# a = int(input("Введите номер столбца от 1 до 8: "))
# b = int(input("Введите число от 1 до 8: "))
# c = int(input("Введите номер столбца от 1 до 8: "))
# d = int(input("Введите число от 1 до 8: "))
# if a == c or b == d:
#     print("yes")
# else:
#     print("no")
##########################

# a = int(input("Введите номер столбца от 1 до 8: "))
# b = int(input("Введите число от 1 до 8: "))
# c = int(input("Введите номер столбца от 1 до 8: "))
# d = int(input("Введите число от 1 до 8: "))
# if (a + 1 == c and b == d) or (a - 1 == c and b == d):
#     print("yes")
# elif (a + 1 == c and b + 1 == d) or (a - 1 == c and b - 1 == d):
#     print("yes")
# elif (a == c and b + 1 == d) or (a == c and b - 1 == d):
#     print("yes")
# elif (a + 1 == c and b - 1 == d) or (a-1==c and b+1==d):
#     print("yes")
# else:
#     print("no")
#############################


# a = int(input("Введите номер столбца от 1 до 8: "))
# b = int(input("Введите число от 1 до 8: "))
# c = int(input("Введите номер столбца от 1 до 8: "))
# d = int(input("Введите число от 1 до 8: "))
# if (a==b and c==d):
#     print("yes")
# elif (a+b==c+d):
#     print("yes")
# elif (a+1==b and c+1==d):
#     print("yes")
# else :
#     print("no")



# km = float(input("Введите расстояние до дачи: "))
# r = float(input("Введите расход на 100 км: "))
# price = float(input("Введите цену 1 литра бензина: "))
# r1 = 2*km/r
# print(r1*price)

