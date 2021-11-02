from src import *

edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'H'], ['D', 'I'], ['E', 'J'], ['E', 'K'], ['F', 'L'], ['F', 'M']]


def main():
    listaCompleta = listaAdyacentes(edges)
    dictionary_items = listaCompleta.items()
    #imprimimos en orden los nodos
    for data in dictionary_items:
        value = len(data[1]) 
        if value == 3 :
            print("Nodo:"+str(data[0]))
            print("padre <- "+str(data[1][0]))
            print("hijo1 -> "+str(data[1][1]))
            print("hijo2 -> "+str(data[1][2]))
        if value ==2 :
            print("Nodo:"+str(data[0]))
            print("hijo1 -> "+str(data[1][0]))
            print("hijo2 -> "+str(data[1][1]))
        if value == 1:
             print("Nodo:"+str(data[0]))
             print("hijo1 -> "+str(data[1][0]))
        print("-------------------------------------------------------------------------")
        #print("hijo2:"+str(data[1:1]))
    print("//////////////////////////////////////////////////////////////////////////////")
    #fin--
    

    #imprimimos en orden el camino
     
    bfs=bestFirstSearch(listaCompleta, 'A')
    print("Camino:",end="")
    for data in bfs:
        print(" -> ",end="")
        print(data,end="")

if __name__ == "__main__":
   main()