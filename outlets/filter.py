import pandas as pd

df=pd.read_csv("result.csv")

filteredOutlets=df.drop_duplicates(["LINK"])
#Quiero eliminar los outlets con el mismo LINk sin importar nada
filteredOutlets=filteredOutlets[filteredOutlets["LINK"].notna()]

filteredOutlets.to_csv("result1.csv", index=False)

print(filteredOutlets)