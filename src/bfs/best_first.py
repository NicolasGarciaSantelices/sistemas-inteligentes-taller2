
from collections import defaultdict

#Generamos la lista de nodos disponibles, con sus nodos adyacentes
def listaAdyacentes(edges):
    lista = defaultdict(list)
    for u, v in edges:
        lista[u].append(v)
        lista[v].append(u)
    return lista



#busqueda
def bestFirstSearch(listaCompleta, inicio):
    nodosVisitados = set()
    cola = []
    nodosVisitados.add(inicio)
    cola.append(inicio)
    
    result = []
    while cola:
        v = cola[0]
        result.append(v)
        #el primer valor es el nodo inicial
        cola = cola[1:]
        #para todo nodo en la lista
        for vecino in listaCompleta[v]:
            if vecino not in nodosVisitados:
                nodosVisitados.add(vecino)
                cola.append(vecino)
    return result