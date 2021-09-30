import random

def evaluate(individual):
    count = 0
    for cur_x,cur_y in enumerate(individual[1::],1):    #começa no segundo elemento
        dist = 0
        for y in individual[cur_x-1::-1]:               #faz backtrack e procura conflitos com peças anteriores
            dist += 1
            if      y == cur_y:         count += 1
            elif    y == cur_y+dist:    count += 1
            elif    y == cur_y-dist:    count += 1
    return count


def tournament(participants):
    return min(participants, key=lambda x:evaluate(x))


def crossover(a,b,index): 
    return a[:index]+b[index:],b[:index]+a[index:]


def mutate(individual, m):
    rand = random.SystemRandom().randint(1,8)
    if rand < m:
        pos = random.SystemRandom().randint(0,7)
        num = random.SystemRandom().randint(1,8)
        individual[pos] = num
    return individual


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    raise NotImplementedError  # substituir pelo seu codigo
