import numpy as np
import random


def cal_pop_fitness(sol_per_pop, machine, power):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function calculates the sum of products between each input and its corresponding weight.
    # array of N
    n = []
    m = []
    for i in range(len(sol_per_pop)):
        n = []
        for j in range(machine):
            if j == 0:
                n.append(-7 * 10 ** -7 * sol_per_pop[i][j] ** 2 + 0.0008 * sol_per_pop[i][j] + 0.6131)

            if j == 1:
                n.append(-9 * 10 ** -7 * sol_per_pop[i][j] ** 2 + 0.0011 * sol_per_pop[i][j] + 0.5393)

            if j == 2:
                n.append(-1 * 10 ** -6 * sol_per_pop[i][j] ** 2 + 0.0012 * sol_per_pop[i][j] + 0.4952)

            if j == 3:
                n.append(-9 * 10 ** -7 * sol_per_pop[i][j] ** 2 + 0.0012 * sol_per_pop[i][j] + 0.5152)

            if j == 4:
                n.append(-8 * 10 ** -7 * sol_per_pop[i][j] ** 2 + 0.0009 * sol_per_pop[i][j] + 0.5500)

        m.append(list(n))

    # print("IMPRIMINDO N")
    # for i in range(len(m)):
    #     print(m[i])

    ng = []
    for i in range(len(sol_per_pop)):
        if machine == 2:
            ng.append(power / ((sol_per_pop[i][0] / m[i][0]) + (sol_per_pop[i][1] / m[i][1])))
        if machine == 3:
            ng.append(power / (
                        (sol_per_pop[i][0] / m[i][0]) + (sol_per_pop[i][1] / m[i][1]) + (sol_per_pop[i][2] / m[i][2])))
        if machine == 4:
            ng.append(
                power / ((sol_per_pop[i][0] / m[i][0]) + (sol_per_pop[i][1] / m[i][1]) + (sol_per_pop[i][2] / m[i][2])
                         + (sol_per_pop[i][3] / m[i][3])))
        if machine == 5:
            ng.append(
                power / ((sol_per_pop[i][0] / m[i][0]) + (sol_per_pop[i][1] / m[i][1]) + (sol_per_pop[i][2] / m[i][2])
                         + (sol_per_pop[i][3] / m[i][3]) + (sol_per_pop[i][4] / m[i][4])))

    return ng


def select_mating_pool(fitness, sol_per_pop):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    for i in range(int(len(sol_per_pop) * 0.2)):  # removendo os 20% piores pais
        minpos = fitness.index(min(fitness))
        print("Imprimindo menor valor de fitness")
        print(minpos)
        del sol_per_pop[minpos]
        del fitness[minpos]
        print("Após remoção")

        print(fitness)
        for i in range(len(sol_per_pop)):
            print(sol_per_pop[i])


def crossover(sol_per_pop, power, population, machine):
    children = []
    offspringnumber = population - len(sol_per_pop)  # quantidade de filhos
    for i in range(0, offspringnumber - 1):
        children = []
        while sum(children) != power:
            # print("ESTOU NO LOOP, SOCORRO")
            # print(sum(children))
            rand1 = random.randint(0, len(sol_per_pop) - 1)
            rand2 = random.randint(0, len(sol_per_pop) - 1)
            crossover_point = random.randint(1, machine - 1)
            # crossover_point = int(machine/2)
            if rand1 != rand2:
                # Create children. np.hstack joins two arrays
                children = np.hstack((sol_per_pop[rand1][0:crossover_point],
                                      sol_per_pop[rand2][crossover_point:]))

                realchildren = list(children)
        print("Imprimindo  Filho")
        print(realchildren)
        sol_per_pop.append(realchildren)

    print("Imprimindo a matriz com os filhos")
    for i in range(len(sol_per_pop)):
        print(sol_per_pop[i])


def mutation(sol_per_pop, machine):
    for i in range(int(len(sol_per_pop) * 0.10)):
        randi = random.randint(0, len(sol_per_pop) - 1)
        randc1 = random.randint(0, machine - 1)
        randc2 = random.randint(0, machine - 1)
        mutpower = random.randint(50, 100)
        print("Elemento antes da mutação")
        print(sol_per_pop[randi])
        if randc1 != randc2:
            if (((sol_per_pop[randi][randc1] + mutpower) <= 1000) and ((sol_per_pop[randi][randc2] - mutpower) >= 300)):
                sol_per_pop[randi][randc1] = sol_per_pop[randi][randc1] + mutpower
                sol_per_pop[randi][randc2] = sol_per_pop[randi][randc2] - mutpower
        print("Elemento pós da mutação")
        print(sol_per_pop[randi])



def bestsolution(sol_per_pop, machine, power):
    ngNew = cal_pop_fitness(sol_per_pop, machine, power)
    maxpos = ngNew.index(max(ngNew))
    bestconfig = sol_per_pop[maxpos]
    bestng = ngNew[maxpos]
    print("Melhor Individuo")
    print(bestconfig)
    print(bestng)
    return bestng
