import pandas as pd
province = pd.read_csv('~/Projects/titipbeliin/doc/province.csv')
province["negara"] = "Indonesia"  
province.to_csv("~/Downloads/province-modify.csv")
print(province)