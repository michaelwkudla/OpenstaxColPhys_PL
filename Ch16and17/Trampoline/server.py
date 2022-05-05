import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the variables
    k = random.randint(3000, 3200)
    m = random.randint(40, 50)
    h1 = round(random.uniform(1, 1.5), 2) 
    h2 = round(random.uniform(2.5, 3), 2) 
    g = 9.81
    
    # Compute the energy
    PE = m*g*(h2-h1)

    # Compute the distance
    x = (2*PE/k)**(1/2)

    # Assign the variables to data
    data2["params"]["k"] = k
    data2["params"]["m"] = m
    data2["params"]["h1"] = h1
    data2["params"]["h2"] = h2

    # Put the answer(s) into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = x

    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass