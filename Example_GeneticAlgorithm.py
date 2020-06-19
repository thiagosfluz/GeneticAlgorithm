import numpy
import ga
import random
import gc
import time
import numpy as np

start_time = time.time()
gc.collect()

iteration = 0
iterationlist = []
sumpoplist = []
iterationsng = 0
iterationlistng = []

print("Entre com a potência máxima: ")
power = int(input())

print("Entre com o número de máquinas: ")
machine = int(input())

# Inputs of the equation.
equation_inputs = machine

# Number of the weights we are looking to optimize.
num_weights = machine

sol_per_pop = []
population = int(100)

# Defining the population size.
pop_size = (population,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.

# new_population = numpy.random.uniform(low=300, high=1000, size=pop_size)

new_population = random.sample(range(300, 1001), machine)

for i in range(0, population):
    new_population = random.sample(range(300, 1001), machine)

    while sum(new_population) != power:
        iteration += 1
        iterationlist.append(iteration) # coleta número de iterações até a soma ficar igual a potência
        new_population = random.sample(range(300,1001), machine)
        print(new_population)
        print(sum(new_population))
        sumpoplist.append(sum(new_population)) # coleta soma de cada individuo até dar a potência inicial
    sol_per_pop.append(new_population)

for i in range(len(sol_per_pop)):
    print(sol_per_pop[i])

i = 1
j = 1
print(pop_size)
print(sol_per_pop[i][j])

best_outputs = []
num_generations = 100
for generation in range(num_generations):
    print("Generation : ", generation)
    # Measuring the fitness of each chromosome in the population.
    fitness = ga.cal_pop_fitness(sol_per_pop, machine,power)
    print("Fitness")
    print(fitness)

    # Selecting the best parents in the population for mating.
    bestparents = ga.select_mating_pool(fitness, sol_per_pop)
    print(bestparents)


    # Generating next generation using crossover.
    ga.crossover(sol_per_pop, power, population, machine) # atualiza a sol_per_pop com os melhores pais e os filhos gerados

    # Adding some variations to the offspring using mutation.
    ga.mutation(sol_per_pop, machine)


    # Best solution
    bestng = ga.bestsolution(sol_per_pop, machine, power)
    iterationlistng.append(bestng) # cria uma lista com os melhores NGs

    print("IMprimindo poulation")
    print(sol_per_pop)
    print("Tempo de execução %s seconds " % (time.time() - start_time))


# importing the required module
import matplotlib.pyplot as plt



# axis values
x1 = []
for i in range(1, int(population*0.8)+1):
    x1.append(i)
y1 = fitness

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('Elementos da última população gerada')
plt.xlabel('Iterações')
plt.ylabel('Melhores NGs')


# gráfico melhores NGs x geração

x2 = []
for i in range(1, num_generations+1):
    x2.append(i)
y2 = iterationlistng

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xscale("linear")
plt.title('Evolução do rendimento global por gerações')
plt.ylabel('Melhores NGs')
plt.xlabel('Gerações')

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.4,wspace=0.5)

# function to show the plot
plt.show()

