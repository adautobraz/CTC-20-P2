import itertools
import GraphGenerator
import timeit
import time
import datetime

def solve(n,m, item):

    graph = GraphGenerator.generateGraph(n,m)

    if item=="a" :
        # ALGORITMO FORCA BRUTA
        #  O vertice de partida sera sempre o numero 1 (indice 0)
        indexes = [i for i in range(1,n)]
        auxPaths = itertools.permutations(indexes, n-1)

        #  Gerando todos os caminhos possiveis
        paths = []
        for i in auxPaths:
            paths.append([0] + list(i) + [0])

        #  Percorrendo todos os caminhos possiveis
        global minCost, minCostPath,existeCaminho
        minCost= 0
        minCostPath = 0
        existeCaminho = False

        for p in paths:
            auxCost = 0
            for step in range(0,n):
                i = p[step]
                j = p[step+1]
                if graph[i][j] == -1:
                    break
                auxCost = auxCost + graph[i][j]
                #  Quando encontramos um caminho valido, o armazenamos e calculamos o seu custo
                if p[j] == p[0]:
                    existeCaminho = True
                    if (minCost == 0 or minCost > auxCost):
                        minCost = auxCost
                        minCostPath = p

    # ALGORITMO HELD-KARP (PROGRAMACAO DINAMICA)
    hkTimeStart = timeit.default_timer()
    global memoria
    memoria = 0
    #Matriz de memoization
    M = [[-1 for i in range(0,pow(2,n))] for j in range(0,n)]
    memoria = pow(2,n)*n
    # Vertice de partida sendo o 1 (indice 0)
    v_inicial = 0
    # Setar a bitmask do noh final
    v_mask = 2**n - 2
    memoria += 2

    def tsp( c, b):
        if b == 0:
            return graph[c][v_inicial]

        if M[c][b] != -1:
            return M[c][b]

        result = 1000
        global memoria
        memoria += 2
        for i in range(0,n) :
            if (((b & (1 << i)) != 0) & (i != c) & (graph[c][i]!=-1)) :
                a = tsp(i, b & ~(1 << i))
                memoria += 1
                if (a != -1):
                    result = min(result, graph[c][i] + a)
        M[c][b] = result
        return result

    minCostHK = tsp(v_inicial,v_mask)
    memoria+=1
    hkTime = timeit.default_timer() - hkTimeStart

    #Retornando os resultados
    if item == "a":
        print "O grafo gerado eh"
        for i in range(0,n):
            print graph[i]
        print "Por forca bruta,",
        if existeCaminho:
            print "o caminho desejado eh:", minCostPath,
            print " e o custo minimo associado  eh:", minCost
        else:
            print "nao existe caminho minimo"
        print "Por Held-Karp",
        if minCostHK == 1000 :
            print "o grafo eh nao-hamiltoniano"
        else:
            print "o custo minimo associado eh:", minCostHK

    if item == "b":
        return hkTime

    if item == "c":
        return memoria




