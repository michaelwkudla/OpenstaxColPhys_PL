import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the m, k, and E
    m = random.randint(2,10) #kg
    k = random.randint(20, 40) #N/m
    E = round(random.uniform(200, 500), 2) #J
    data2["params"]["m"] = m
    data2["params"]["k"] = k
    data2["params"]["E"] = E

    # Compute the other mass
    x = numpy.sqrt(E*2/k)
    v = numpy.sqrt(E*2/m)

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = x
    data2["correct_answers"]["part2_ans"] = v
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass