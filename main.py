arr = ['a','b']

def errores(lista):
    if lista  == []: #en el caso de que no haya ningun elemento
        return None

    # elif lista == : #en el caso que solo haya un solo elemento
    #     pass

    else:
        def ultimo_primer_carracter(lista):

               primer_ultimo = []
               primer_ultimo.append(lista[0])
               primer_ultimo.append(lista[-1])
               return primer_ultimo

    return ultimo_primer_carracter(lista)


print(errores(arr))
    

