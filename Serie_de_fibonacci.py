
def serie_fibonacci(limite:int=None):
    if limite<0:
        return ("Ingrese numeros positivos")
    serie=[0,1]
    for i in range(0,limite):
        new_element=sum(serie[-2:])
        serie.append(new_element)
    
    return(serie[1:])
