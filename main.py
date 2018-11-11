from fuzzywuzzy import fuzz
import random
import string


class Agent:

    def __init__(self, length):

        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length)) #creates a string with random letters withing the given str length
        self.fitness = -1 

    def __str__(self):

        return 'String: ' + str(self.string) + ' Fitness: ' + str(self.fitness)

in_str = None
in_str_len = None
population = 20
generations = 1000


def ga():

    agents = init_agents(population, in_str_len)

    for generation in range(generations):

        print ('Generation: ' + str(generation))

        agents = fitness(agents)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents)

        if any(agent.fitness >= 90 for agent in agents):

            print ('Threshold met!')
            exit(0)
            
def init_agents(population, length):

    return [Agent(length) for _ in range(population)]

def fitness(agents):

    for agent in agents:

        agent.fitness = fuzz.ratio(agent.string, in_str) # % of how close is the agent.string to the in_str
    
    return agents

def selection(agents):

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
    print ('\n'.join(map(str, agents))) #for each agent applying str func to it and it returns thr str representation of each agent, and join them together in bet new lines 

    agents = agents[:int(0.2 * len(agents))] #taking top 20% of the agents

    return agents

def crossover(agents):

    offspring = []

    for _ in range ((population - len(agents)) // 2):

        parent1 = random.choice(agents)
        parent2 = random.choice(agents)

        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)

        split = random.randint(0, in_str_len) #split can be any random value in bet 0 - in_str_len
                                                                                   # 2 possible crossovers 
        child1.string = parent1.string[0:split] + parent2.string[split:in_str_len] #splitting 1st half from parent1 [0 - split] + 2nd half from parent2 [split - in_str_len]
        child2.string = parent2.string[0:split] + parent1.string[split:in_str_len] #splitting 1st half from parent2 [0 - split] + 2nd half from parent1 [split - in_str_len]

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring) #extend is same as append except it takes only elements even if the elements are in lists, they don't attach the list like "append"

    return agents

def mutation(agents):  #mutation is required or else no change

    for agent in agents:

        for idx, param in enumerate(agent.string): #index,parameter [0:rojkal,1:rohax......]

            if random.uniform(0.0, 1.0) <= 0.1: #10% chance mutation occurs

                agent.string = agent.string[0:idx] + random.choice(string.ascii_letters) + agent.string[idx+1:in_str_len] #idx+1 since end up 1 val before just like "range"

    return agents

    
if __name__ == '__main__':

    in_str = 'Rohan'       #giving the str
    in_str_len = len(in_str) #len of the str
    ga()

