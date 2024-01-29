# Función que dado una cantidad de vallas, sus extremos iniciales y tamanios,
# determina el conjunto maximal de vallas a colocar.
# Argumentos:
#   n: numero de vallas que solicitan permiso
#   inicios: arreglo con el punto inicial de cada valla
#   tamanios: arreglo que contiene el tamanio de cada valla
def planificador_permisos(n, inicios, tamanios) -> set:
    
    # se ordenan las vallas de menos a mayor con respecto a su extremo final (O(n*log(n)))
    vallas = sorted([[i, inicios[i], inicios[i] + tamanios[i]] for i in range(0, n)], key = lambda valla: valla[2])

    conjunto_maximal_vallas = {vallas[0][0] + 1}
    ultima_valla = vallas[0]

    # se seleccionan las vallas con menor extremo final que no se superpongan con las ya elegidas O(n)
    for i in range(1, n):  
        if ultima_valla[2] <= vallas[i][1]:
            conjunto_maximal_vallas.add(vallas[i][0] + 1)
            ultima_valla = vallas[i]

    return conjunto_maximal_vallas
    