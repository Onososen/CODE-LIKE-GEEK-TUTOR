#PROGRAM TO CALCLULATE AREA OF A Cylinder
pi = 3.142
h = float(input("What is height:\n"))
b = float(input("What is the breadth:\n"))
d = float(input("What is the diameter:\n"))
c = pi * d
area = (c * h)+ ( 2 * b)
answer = round(area,2)
print(answer)

