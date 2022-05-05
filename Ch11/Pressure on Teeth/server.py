import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the force and area
    A = round(random.uniform(0.75, 1.25), 2) #mm^2
    F = random.randint(400,500)

    data2["params"]["A"] = A 
    data2["params"]["F"] = F

    # Compute the pressure
    P = F/(A/1000**2)

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = P


    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass