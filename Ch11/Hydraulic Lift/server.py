import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the diameters and maas
    d1 = round(random.uniform(1.5, 3), 1) 
    d2 = round(random.uniform(20, 30), 1) 
    m = random.randint(1500, 2500)

    data2["params"]["d1"] = d1
    data2["params"]["d2"] = d2
    data2["params"]["m"] = m

    # Compute the Force
    F = (d1/d2)**2*m*9.81 

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = F
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass