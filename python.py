#   TEMPERATURE CALCULATOR   #

total = 0
for i in range(1,8):
  temp = int(input("Day " + str(i) + "'s Temp: "))
  total += temp
avg = total / 7
print(avg)

#   ISOCELES TRIANGLE TEST   #

Length1 = float(input("Length 1: "))
Length2 = float(input("Length 2: "))
Length3 = float(input("Length 3: "))
if Length1 == Length2 or Length1 == Length3 or Length2 == Length3:
  print("Isoceles")
else:
  print("Not Isoceles")

#   MATHMATICAL OPERATORS   #

addition = int(input("Add 1 to: ")) + 1
print(addition)
subtraction = int(input("Subtract 1 from: ")) - 1
print(subtraction)
multiplication = int(input("Multiply 10 by: ")) * 10
print(multiplication)
division1 = 5 / float(input("Divide 5: "))
print(division1)
division2 = 5 // int(input("Integer Divide 5: "))
print(division2)
remainder = int(input("Remainder of 7 and: ")) % 7
print(remainder)
exponential = int(input("Exponential of 3 and: ")) ** 3
print(exponential)
