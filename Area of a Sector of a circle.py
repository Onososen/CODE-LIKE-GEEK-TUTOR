#PROGRAM TO CALCLULATE AREA OF A SECTOR
pi = 3.142
r = float(input("What is radius:\n"))
A = int(input("What is the Angle:\n"))
area = (A/260) *pi * r**2
answer = round(area,2)
print(answer)

