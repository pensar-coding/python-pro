# operador * -> desempaqueta listas

def suma(*numeros):
    suma= 0
    for num in numeros:
        suma += num
    print(suma)
    return suma

lista = [4,5,1,5]
suma(*lista)
print(*lista)
print(lista)

# operador ** -> desempaqueta diccionarios
mi_dic = {"nombre":"Tatiana","suscriptores":16000}
mi_dic2 = {"dni":12345678,"edad":24}
minuevodic= {**mi_dic,**mi_dic2}
print(minuevodic)