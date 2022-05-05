import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the diameters
    d1 = round(random.uniform(1, 1.5), 2)
    d2 = round(random.uniform(2.5, 3), 2)
    d3 = round(random.uniform(0.8, 1.2), 2)
    m = random.randint(60, 100)

    data2["params"]["d1"] = d1
    data2["params"]["d2"] = d2
    data2["params"]["d3"] = d3
    data2["params"]["m"] = m

    T = m*9.81*d3

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = T

    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
