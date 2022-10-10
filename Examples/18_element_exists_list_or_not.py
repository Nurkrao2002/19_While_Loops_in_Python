n1=[2,4,6,8,9,14]
f=int(input("Which element you want to find? :"))
for i in n1:
    if (f in n1):
        print("The Value is Found")
        break
    elif (f not in n1):
        print("The Value is Not Found")
        break