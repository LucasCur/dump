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

#   
