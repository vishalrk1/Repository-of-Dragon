print("Enter the number: ")
x = int(input())
y=1
if x > 0 :
    while x != 0:
        y = y * x
        x = x - 1
elif x==0:
    y=1
print(y)
