number = input()

integer=int(float(number))
float=float(number)-float(integer)

salida=""
while integer!=0:
     salida+=str(integer%2)
     integer=int(integer/2)

if float!=0:
    salida+="."

    while float!=1:
        float=float*2
        if float>1:
                salida=salida+"1"
                float=float-1
        elif float<1:
                salida=salida+"0"
        else:

            salida =salida+"1"


print(salida)
