# a=["1","2","3","4","5"]
# for i in range(len(a)):
#     a[i]=int(a[i])
#     print(a[i])

# v=["10","20","30","40"]
# b=list(map(int,v))
# print(b)

# def sq(y):
#     return y*y
# n=[2,3,4,5,6]
# s=list(map(sq,n))
# g=list(map(lambda x: x*x,n))
# print(s)
# print(g)

# def square(s): return s*s
# def cube(c): return c*c*c
# f=[square,cube]
# for i in range(1,6):
#     a=list(map(lambda x:x(i),f))
#     print(a)

# a=[1,2,3,4,5,6,7,8,9,10]
# def gr(n):
#     return n>5
# def ls(n):
#     return n<5
# v=list(filter(gr,a))
# b=list(filter(ls,a))
# print(v)
# print(b)

# from functools import reduce
# e=[5,10,15,20,25]
# n=reduce(lambda x,y: x+y,e)
# print(n)