
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

for i in range(1, len(nilai_uts)): 
        key = nilai_uts[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key['nilai'] < nilai_uts[j]['nilai'] : 
                nilai_uts[j+1] = nilai_uts[j] 
                j -= 1
        nilai_uts[j+1] = key 

print(nilai_uts)