import pandas as pd

df= pd.read_excel("ONTs.xlsx")

##print(df.head(5))
#print(len(df))
archivo = open("ont.txt","r+")
seriales = df["HW SERIAL NO."]
for i in seriales:
    if len(i) > 20:
        dato_compuesto = i.split(" ")
        for j in dato_compuesto:
            archivo.write("\n"+j)
            print("compuesto "+j + "\n" )    
    else:  
        if i:
            archivo.write("\n"+i)

archivo.close()

