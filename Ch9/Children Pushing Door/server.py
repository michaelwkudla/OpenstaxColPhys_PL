import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the force and distance
    F1 = random.randint(20,90)
    r1 = round(random.uniform(0.1, 0.3), 2)
    r2 = round(random.uniform(0.1, 0.3), 2)
    data2["params"]["F1"] = F1
    data2["params"]["r1"] = r1
    data2["params"]["r2"] = r2

    # Compute the sum of these two integers
    F2 = F1*r1/r2

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = F2


    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass