import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the variables
    k = round(random.uniform(1.20, 1.60), 2) * 10000
    m = random.randint(80,120)
    d = round(random.uniform(1.7, 3.5), 2) 
    g = 9.81
    
    # Compute the frequency
    f = 1/(2*numpy.pi)*(k/m)**(1/2)

    # Compute the distance
    x = (2*m*g*d/k)**(1/2)

    # Assign the variables to data
    data2["params"]["k"] = k
    data2["params"]["m"] = m
    data2["params"]["d"] = d


    # Put the answer(s) into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = f
    data2["correct_answers"]["part2_ans"] = x

    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass