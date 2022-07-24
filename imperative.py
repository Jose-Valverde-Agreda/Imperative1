def increment(n):
    return n+1

def square(n):
    return n*n

"""
Debo commentar que usando el paradigma imperativo, pues
si parto de un estado inicial (al que llamare CANDIDATES) y tengo dos acciones. Mi siguiente estado tendrá 2 elementos (2 CANDIDATES), si a cada elemento le aplico acciones, mi siguiente estado tendrá (4 CANDIDATES) y así. En cada paso debo comparar si alguno de mis CANDIDATES
es la respuesta que buscaba
"""

def findSequence(initial, goal):
    # construimos una lista de candidatos de por ejemplo ('1 increment incremetn square, 9)
    candidates = [(str(initial), initial)]
    # creamos un bucle de 'goal - initial +1' pasos, ya que es lo máximo que podría haber si solo hacemos INCREMENT (ya que talvez ese era el procedmiento con el mínimo de pasos)
    for i in range(1, goal-initial +1):
        newCandidates = []
        # construimos un nuevo candidato por agregar una operación al candidato previo
        for (action,result) in candidates:
            # A cada candidato le aplicamos las dos acciones
            for (a,r) in [(' increment', increment),(' saquare', square)]:
                newCandidates.append((action +a, r(result)))
                print(f"{i} : {newCandidates[-1]}")
                if newCandidates[-1][1] == goal:
                    return newCandidates[-1]
        # Actualizo mis candidatos
        candidates = newCandidates

answer = findSequence(1,100)
print(f"answer : {answer}")