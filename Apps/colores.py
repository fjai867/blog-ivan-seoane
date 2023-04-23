lista=[]
elementos=["marino","cobalto","celeste","blanco"]
contador=0
for i in elementos:
    for j in elementos:
        for k in elementos:
            elemLista=i+j+k
            if i != j:
                if j != k:

                
                   
                    combi=i+"-"+j+"-"+k
                    lista.append(combi)
for i2 in lista:                   
    print(i2)