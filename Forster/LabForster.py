import Algoritmos

print "Menor caminho para Forca bruta e Held-Park"
for i in range (0,10):
   Algoritmos.solve(6,10,"a")

print "Tempo x Numero de vertices"
for n in range(3,20):
    tempoMedio =0
    for i in range(0,10):
        tempoMedio += Algoritmos.solve(n, n * (n - 1) / 2,"b")
    tempoMedio = tempoMedio/10
    print tempoMedio, "para", n, "vertices"

print "Memoria x Numero de vertices"
for n in range(3,20):
    memoriaMedia =0
    for i in range(0,10):
        memoriaMedia += Algoritmos.solve(n, n * (n - 1) / 2,"c")
    memoriaMedia = memoriaMedia/10
    print memoriaMedia

print "Tempo x Numero de arestas, n=10"
for m in range(0,45):
    tempoMedio =0
    for i in range(0,10):
        tempoMedio += Algoritmos.solve(10, m,"b")
    tempoMedio = tempoMedio/10
    print tempoMedio, "para", m, "arestas"