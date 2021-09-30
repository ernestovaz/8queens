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
    indiv = individual.copy()
    rand = random.SystemRandom().randint(0,100)/100
    if rand < m:
        pos = random.SystemRandom().randint(0,7)
        num = random.SystemRandom().randint(1,8)
        indiv[pos] = num
    return indiv


def random_indiv_list(n):
    lis = []
    for i in range(n):
        item = []
        for j in range(8):
            num = random.SystemRandom().randint(1,8)
            item.append(num)
        lis.append(item) 
    return lis

def selection(given_p,k):
    p = given_p.copy()
    k_items = [] 
    for i in range(k):
        rand = random.SystemRandom().randint(0,len(p)-1)
        k_items.append(p.pop(rand))
    p1 = tournament(k_items)
    k_items.remove(p1)
    p2 = tournament(k_items)
    return p1,p2


def run_ga(g, n, k, m, e):
    p = random_indiv_list(n)
    for i in range(g):
        if e: p_dash = [tournament(p)]  #elitismo, p_dash = p'
        else: p_dash = []  
        while len(p_dash)<n:
            p1,p2 = selection(p,k)
            cross_index = random.SystemRandom().randint(1,8)
            o1,o2 = crossover(p1,p2,cross_index)
            o1 = mutate(o1,m)
            o2 = mutate(o2,m)
            p_dash.extend([o1,o2])
        p = p_dash 
    return tournament(p)

