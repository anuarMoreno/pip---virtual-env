def sentence():
    name  = input('Ingresa tu nombre, probemos vsCode con WSL: ')
    result = "Hola {}, estamos ready.".format(name)
    return print(result)

sentence()