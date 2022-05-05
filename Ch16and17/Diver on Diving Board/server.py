import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the mass and periods
    m1 = random.randint(45,60)
    T1 = round(random.uniform(0.5, 1.0), 2) 
    T2 = round(random.uniform(1.01, 1.25), 2) 
    data2["params"]["m1"] = m1
    data2["params"]["T1"] = T1
    data2["params"]["T2"] = T2

    # Compute the other mass
    m2 = m1*(T2/T1)**2

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = m2
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass