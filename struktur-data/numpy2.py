import numpy as np

a = np.arange(6).reshape(2,3)
# print(a)

# for x in np.nditer(a, op_flags=['readwrite']):
#   x[...] = 2 * x

# print(a)
print(a)
i = 0
for baris in a:
  col = 0
  for kolom in baris:
    print("baris ke "+str(i)+","+str(col),kolom)
    col += col
  i += 1