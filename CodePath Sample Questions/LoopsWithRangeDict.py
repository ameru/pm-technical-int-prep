range(1,7)
>>> [1,2,3,4,5,6]
# print range index 1 to 7

range(0,8,2)
>>> [0,2,4,6]
# print range indez 0 to 8, incrementing by 2

sum = 0
for i in range(10):
  sum = sum + 1
  print sum
>>> 0
1
3
6
10
15
21
28

a = ["mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
  print(i, a[i])
>>> 0. mary
1. had
2. a
3. little
4. lamb
# i prints out index of string
# a[i] prints out the string
