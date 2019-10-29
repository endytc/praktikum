data = [1,2,3,4,5,6]
n = len(data)
total_loop = 0 

for i in range(n-1):
  for j in range(n-1):
    total_loop +=1 
    if data[j] > data[j+1] :
        data[j], data[j+1] = data[j+1], data[j]
  print('ke-'+str(i),data)

print(data)
print(total_loop)



data = [1,2,3,4,5,6]
n = len(data)
total_loop = 0

for i in range(n):
  for j in range(n-i-1):
    total_loop +=1
    if data[j] > data[j+1] :
        data[j], data[j+1] = data[j+1], data[j]
  print('ke-'+str(i),data)

print(data)
print(total_loop)

data = [1,2,3,4,5,6]
n = len(data)
ditukar = True
i = -1
total_loop=0
while ditukar:
  i += 1
  ditukar = False
  for j in range(n-i-1):
    total_loop +=1
    if data[j] > data[j+1] :
      ditukar = True
      data[j], data[j+1] = data[j+1], data[j]
  print('ke-'+str(i),data)
    

print(data)
print(total_loop)


nilai_uts = [
  {
    "nama":"Siti Azizah",
    "nilai": 85
  },{
    "nama":"Siti Aminah",
    "nilai": 95
  },{
    "nama":"Siti Fatimah",
    "nilai": 75
  },{
    "nama":"Siti Maimunah",
    "nilai": 70
  },{
    "nama":"Siti Komariah",
    "nilai": 90
  },
]