import pandas as pd
dict = {
  "country":["Indonesia", "Singapura","Malaysia"],
  "capital":["Jakarta","Singapura","Malaysia"],
  "population":[250000000,1000000,20000000]
}
data = pd.DataFrame(dict,index=["ID","SG","MY"])
# data = pd.DataFrame(dict)
print(data.loc["ID"])