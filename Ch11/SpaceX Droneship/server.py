import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the dimensions 
    L1 = random.randint(90,100)
    L2 = random.randint(45,55) 
    h1 = random.randint(5,7) 
    m1 = random.randint(4000000, 4500000)
    m2 = random.randint(25000, 26000)
    rho = 1025

    data2["params"]["L1"] = L1
    data2["params"]["L2"] = L2
    data2["params"]["h1"] = h1
    data2["params"]["m1"] = m1
    data2["params"]["m2"] = m2
    data2["params"]["rho"] = rho

    # Compute the sinking distance
    h = (m2)/(L1*L2*rho)

    # Put the height
    data2["correct_answers"]["part1_ans"] = h

    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass