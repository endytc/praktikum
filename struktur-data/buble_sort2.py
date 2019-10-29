data = [72,42,35,12,101,5,3,4,4,3,2,3,4,5,6,7,8,6,5,4,3,3,1,23,44,32,2,1,2,3,4,5]
n = len(data)
total_loop = 0 

for i in range(n):
  for j in range(n-1):
    total_loop +=1 
    if data[j] > data[j+1] :
        data[j], data[j+1] = data[j+1], data[j]

print(data)
print(total_loop)



data = [72,42,35,12,101,5,3,4,4,3,2,3,4,5,6,7,8,6,5,4,3,3,1,23,44,32,2,1,2,3,4,5]
n = len(data)
total_loop = 0

for i in range(n):
  for j in range(n-i-1):
    total_loop +=1
    if data[j] > data[j+1] :
        data[j], data[j+1] = data[j+1], data[j]

print(data)
print(total_loop)

data = [72,42,35,12,101,5,3,4,4,3,2,3,4,5,6,7,8,6,5,4,3,3,1,23,44,32,2,1,2,3,4,5]
n = len(data)
ditukar = True
total_loop = 0
i = -1
while ditukar:
  i += 1
  ditukar = False
  for j in range(n-i-1):
    total_loop +=1
    if data[j] > data[j+1] :
      ditukar = True
      data[j], data[j+1] = data[j+1], data[j]
    

print(data)
print(total_loop)