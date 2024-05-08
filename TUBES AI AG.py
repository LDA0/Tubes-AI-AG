# ##############################   KNAPSACK   ############################################
# import random


# def sampel():
#     pass


# def generate_population(population, iteration):
#     #################################################  Generating population
#     population.clear()
#     for x in range(4):
#         chromosome = []
#         for x1 in range(7):
#             chromosome.append(random.choice([0, 1]))
#         population.append(chromosome)
#     ################################################# Population filtering
#     fitness_dummy = []
#     best_dummy = [0]
#     selected_dummy = []
#     fitness_check(population, selected_dummy, fitness_dummy, best_dummy, iteration)
#     y = 1
#     for x in fitness_dummy:
#         if x == 0:
#             y = 0
#     if y == 0:
#         population.clear()
#         generate_population(population, 0)


# def fitness_check(population, selected, fitness, best, iteration):
#     fitness.clear()
#     ############################################# Declare samples
#     berat = [5, 7, 3, 8, 1, 9, 4]
#     prioritas = [80, 200, 100, 300, 150, 100, 50]
#     ############################################# Evaluation
#     for chromosome in population:
#         beratnya = 0
#         prioritasnya = 0
#         sample_index = 0
#         for gene in chromosome:
#             if gene == 1:
#                 beratnya += berat[sample_index]
#                 prioritasnya += prioritas[sample_index]
#             sample_index += 1
#         if beratnya <= 20: ############################ Constraint
#             fitness.append(prioritasnya)
#         else:
#             fitness.append(0)
#     #############################################  Updating best chromosome
#     ####### best = [fitness_score, best_chromosome, chromosome_parents, iteration]
#     if max(fitness) > best[0]:
#         best.clear()
#         best.append(max(fitness))
#         best.append(list(population[fitness.index(max(fitness))]))
#         if selected:
#             if fitness.index(max(fitness)) % 2 != 0:
#                 best.append(list(selected[fitness.index(max(fitness))]))
#                 best.append(list(selected[fitness.index(max(fitness))-1]))
#             else:
#                 best.append(list(selected[fitness.index(max(fitness))]))
#                 best.append(list(selected[fitness.index(max(fitness))+1]))
#         best.append(iteration)


# def parent_selection(population, fitness, selected, iteration):
#     selected.clear()
#     ############################################# Creating Roulette Wheel
#     total = sum(fitness)
#     if total != 0:
#       main_color = [0]
#       selected.append(0)
#       chr_index = 1
#       for chromosome in fitness:
#         main_color.append(int(chromosome/total*1000+main_color[chr_index - 1]))
#         chr_index += 1
#       ############################################# Selecting
#       while len(selected) <= len(population):
#         random_num = random.randint(0, 1000)
#         for roulette_index in range(len(main_color)-1):
#           if random_num in range(main_color[roulette_index], main_color[roulette_index + 1]):
#             selected.append(population[roulette_index])
#       selected.remove(0)
#     else:
#       generate_population(population, iteration)

# def crossover(population, selected, mark, mode):
#     population.clear()
#     ############################################# Crossover Schema
#     i1 = 0
#     select = list(selected)
#     while i1 < (len(select)-1):
#         if random.randrange(0, 1000) < 800: ###### Crossover Dice
#             for x in range(len(select[i1]) - mark):
#                 select[i1][x + mark], select[i1 + 1][x + mark] = select[i1 + 1][x + mark], select[i1][x + mark]
#             if mode == 1:
#               print("CROSSOVER!!!")
#         population.append(list(select[i1]))
#         population.append(list(select[i1 + 1]))
#         i1 += 2
#      ############################################# Mutation Schema
#     for chromosome in population:
#       for gene in range(len(chromosome)):
#         if random.randint(0, 1000) < 100: ###### Mutation Dice
#             if chromosome[gene] == 1:
#                 chromosome[gene] = 0
#             else:
#                 chromosome[gene] = 1
#             if mode == 1:
#               print("MUTASI!!!!!!!!!!!!!!!!!!!!!!!!!!")


# def menu(population, fitness, selected, best, marker, iterasi, i):
#   print("Welcome to Genectic Algorithm for Knapsack Problem!")
#   print("Please Choose between the following option:")
#   print("1. Full Process Output")
#   print("2. Quick Output")
#   user_input = int(input('(1/2) ===> '))
#   if user_input == 1:
#     generate_population(population, i)
#     fitness_check(population, selected, fitness, best, i)
#     parent_selection(population, fitness, selected, i)
#     print("New Pop", population)
#     print("New fit", fitness)
#     print("New sel", selected)
#     print(best)
#     i += 1
#     while i in range(iterasi):
#         crossover(population, selected, marker, user_input)
#         fitness_check(population, selected, fitness, best, i)
#         parent_selection(population, fitness, selected, i)
#         print("New Pop", i, population)
#         print("New fit", fitness)
#         print("New sel", selected)
#         print(best)
#         # if marker < 6:
#         #     marker += 1
#         # else:
#         #     marker = 0
#         i += 1
#   elif user_input ==2:
#       generate_population(population, i)
#       fitness_check(population, selected, fitness, best, i)
#       parent_selection(population, fitness, selected, i)
#       i += 1
#       while i in range(iterasi):
#           crossover(population, selected, marker, user_input)
#           fitness_check(population, selected, fitness, best, i)
#           parent_selection(population, fitness, selected, i)
#           # if marker < 6:
#           #     marker += 1
#           # else:
#           #     marker = 0
#           i += 1
#       print("Last Pop", population)
#       print("Last fit", fitness)
#       print("Last sel", selected)
#       print("Last best", best)


# if __name__ == '__main__':
#     population1 = []
#     fitness1 = []
#     selected1 = []
#     best1 = [0]
#     marker1 = 3
#     iterasi1 = 100
#     i1 = 0
#     menu(population1, fitness1, selected1, best1, marker1, iterasi1, i1)


#############################   TRAVELLING MERCHANT   ############################################


import random


def sampel():
    pass


def generate_population(population, iteration):
    #################################################  Generating population
    population.clear()
    chromosome = []
    for x1 in range(7):
      chromosome.append(x1+1)
    for x in range(4):
      random.shuffle(chromosome)
      chromo = list(chromosome)
      population.append(chromo)


def fitness_check(population, selected, fitness, best, iteration):
    fitness.clear()
    ############################################# Declare samples
    jarak_relatif=[]
    jarak_relatif.append([0, 7, 3, 8, 1, 9, 4])
    jarak_relatif.append([5, 0, 3, 8, 1, 9, 4])
    jarak_relatif.append([5, 7, 0, 8, 1, 9, 4])
    jarak_relatif.append([5, 7, 3, 0, 1, 9, 4])
    jarak_relatif.append([5, 7, 3, 8, 0, 9, 4])
    jarak_relatif.append([5, 7, 3, 8, 1, 0, 4])
    jarak_relatif.append([5, 7, 3, 8, 1, 9, 0])
    ############################################# Evaluation
    for chromosome in population:
      jaraknya = 0
      i = 1
      for gene in chromosome:
        jaraknya += jarak_relatif[gene - 1][chromosome[i]-1]
        if i < 6:
          i += 1
        else:
          break
      fitness.append(jaraknya)
    #############################################  Updating best chromosome
    ####### best = [fitness_score, best_chromosome, chromosome_parents, iteration]
    if min(fitness) < best[0]:
        best.clear()
        best.append(min(fitness))
        best.append(list(population[fitness.index(min(fitness))]))
        if selected:
            if fitness.index(min(fitness)) % 2 != 0:
                best.append(list(selected[fitness.index(min(fitness))]))
                best.append(list(selected[fitness.index(min(fitness))-1]))
            else:
                best.append(list(selected[fitness.index(min(fitness))]))
                best.append(list(selected[fitness.index(min(fitness))+1]))
        best.append(iteration)


def parent_selection(population, fitness, selected, iteration):
    selected.clear()
    ############################################# Creating Roulette Wheel
    total = sum(fitness)
    if total != 0:
      main_color = [0]
      selected.append(0)
      chr_index = 1
      for chromosome in fitness:
        main_color.append(int((1000-chromosome/total*1000)+main_color[chr_index - 1]))
        chr_index += 1
      ############################################# Selecting
      while len(selected) <= len(population):
        random_num = random.randint(0, 1000)
        for roulette_index in range(len(main_color)-1):
          if random_num in range(main_color[roulette_index], main_color[roulette_index + 1]):
            selected.append(population[roulette_index])
      selected.remove(0)
    else:
      generate_population(population, iteration)

def crossover(population, selected, mark, mode):
    population.clear()
    ############################################# Crossover Schema
    i1 = 0
    select = list(selected)
    while i1 < (len(select)-1):
        buffer1 = []
        buffer2 = []
        if random.randrange(0, 1000) < 800: ###### Crossover Dice
            for x in range(len(select[i1]) - mark):
               buffer1.append(x+mark)
               buffer2.append(select[i1+1].index(select[i1][x + mark]))
            for isi1,isi2 in zip(buffer1,buffer2):
              select[i1][isi1],select[i1+1][isi2] = select[i1+1][isi2],select[i1][isi1] 
            if mode == 1:
              print("CROSSOVER!!!")
        population.append(list(select[i1]))
        population.append(list(select[i1 + 1]))
        i1 += 2
     ############################################# Mutation Schema
    for chromosome in population:
      for gene in range(len(chromosome)):
        if random.randint(0, 1000) < 100: ###### Mutation Dice
            x = random.randint(0,6)
            y = random.randint(0,6)
            while x == y:
              if x == y:
                y = random.randint(0,6)
            chromosome[x], chromosome[y] = chromosome[y], chromosome[x]
            if mode == 1:
              print("MUTASI!!!!!!!!!!!!!!!!!!!!!!!!!!")


def menu(population, fitness, selected, best, marker, iterasi, i):
  print("Welcome to Genectic Algorithm for Travelling Merchant Problem!")
  print("Please Choose between the following option:")
  print("1. Full Process Output")
  print("2. Quick Output")
  user_input = int(input('(1/2) ===> '))
  if user_input == 1:
    generate_population(population, i)
    fitness_check(population, selected, fitness, best, i)
    parent_selection(population, fitness, selected, i)
    print("New Pop", population)
    print("New fit", fitness)
    print("New sel", selected)
    print(best)
    i += 1
    while i in range(iterasi):
        crossover(population, selected, marker, user_input)
        fitness_check(population, selected, fitness, best, i)
        parent_selection(population, fitness, selected, i)
        print("New Pop", i, population)
        print("New fit", fitness)
        print("New sel", selected)
        print(best)
        # if marker < 6:
        #     marker += 1
        # else:
        #     marker = 0
        i += 1
  elif user_input ==2:
      generate_population(population, i)
      fitness_check(population, selected, fitness, best, i)
      parent_selection(population, fitness, selected, i)
      i += 1
      while i in range(iterasi):
          crossover(population, selected, marker, user_input)
          fitness_check(population, selected, fitness, best, i)
          parent_selection(population, fitness, selected, i)
          # if marker < 6:
          #     marker += 1
          # else:
          #     marker = 0
          i += 1
      print("Last Pop", population)
      print("Last fit", fitness)
      print("Last sel", selected)
      print("Last best", best)



if __name__ == '__main__':
    population1 = []
    fitness1 = []
    selected1 = []
    best1 = [1000]
    marker1 = 3
    iterasi1 = 100
    i1 = 0
    menu(population1, fitness1, selected1, best1, marker1, iterasi1, i1)
