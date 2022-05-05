import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Generate m and v
    v = round(random.uniform(0.6, 1.60), 2)
    m = random.randint(1100,2000)


    data2["params"]["m"] = m
    data2["params"]["v"] = v

    E = 1/2*m*v**2

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = E
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass