
def suma(a,b):
    return a+b

def suma_indefinida(a,b,*numeros):
    suma = a+b
    print(type(numeros))
    for num in numeros:
        suma += num
    return suma

def buildConfig(nombreApp,idApp,*config):
    body = {
        "nombreApp":nombreApp,
        "idApp":idApp,
        "roles":[],
        "permisos":[],
    }
    #for args in config:
        #print(args)
    
def buildConfig2(nombreApp,idApp,**config):
    print(type(config))
    body = {
        "nombreApp":nombreApp,
        "idApp":idApp,
        "roles":[],
        "permisos":[],
    }

    body['roles']=config.get('roles') if config.get('roles') else None
    body['permisos']=config.get('permisos') if config.get('permisos') else None

    print(body)


print(suma(4,5))
print(suma_indefinida(4,5,1,1,100))
buildConfig("1lugarparapensar",12,["admin","engineer"],["read","write","delete"])
buildConfig2("2lugarparapensar",2,roles=["admin","engineer"],permisos=["read","write","delete"])

