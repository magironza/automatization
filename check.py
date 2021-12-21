import pandas as pd

df= pd.read_excel("ejemplo.xlsx")

##print(df.head(5))
#print(len(df))
archivo = open("seriales33H.txt","r+")
seriales = df["HW SERIAL NO."]
for i in seriales:
    if len(i) > 20 and i.startswith("2114260812NVL"):
        dato_compuesto = i.split(" ")
        for j in dato_compuesto:
            archivo.write("\n"+j)
            print("compuesto "+j + "\n" )    
    else:  
        if i.startswith("2114260812NVL"):
            archivo.write("\n"+i)

archivo.close()