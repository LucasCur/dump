#   TEMPERATURE CALCULATOR   #

total = 0
for i in range(1,8):
  temp = int(input("Day " + str(i) + "'s Temp: "))
  total += temp
avg = total / 7
print(avg)

#
