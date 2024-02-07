print ("Hello world")
#for i in range(1,6):
#   print (i,"-", "0" *i)


# i=0
# n=0
# while i <=100:
#     n=n+i
#     i=i+1
# print (n)


# a=int(input())
# b=int(input())
# c=int(input())
# if a==b or a==c or b==c:
#     print ("yes")
# else:
#     print("error")



# num = int (input())
# maxs = 0
# while num:
#     if num > maxs and num % 5 == 0:
#         maxs = num
#     num = int(input())
# print(maxs)



# lst = [-11, 4, -2, 90, 400, 0, -5]
# new_lst = []
# for i in lst:
#     if abs(i) > 5:
#         new_lst.append(i)
# print (new_lst)



# lst = [-11, 4, -2, 90, 400, 0, -5]
# max = lst [0]
#
# for i in range (1, len(lst)):
#     if lst[i] > max:
#         max = lst [i]
# print (max)

#

#Таблица умножения на 5

#Вариант 1
# p = 5
# n=0
# for i in range(1, 11):
#     n=p*i
#     print('5 *',i, '=',n)

#Вариант 2 В этом примере переменная ST содержит массив данных по таблице
# умножения на 5

n=5
st = str()
for i in range(1, 11):
    z = n * i
    st = st + f'{n} * {i} = {z} \n'
print(st)



# name = 'Ivan'
# age = 23
# print ('Привет', name, age )