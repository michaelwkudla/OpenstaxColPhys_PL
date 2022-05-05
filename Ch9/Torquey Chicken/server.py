import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the force and distance
    m = round(random.uniform(1, 5), 2)
    d1 = round(random.uniform(0.16, 0.3), 2)
    d2 = round(random.uniform(0.05, 0.15), 2)

    data2["params"]["m"] = m
    data2["params"]["d1"] = d1
    data2["params"]["d2"] = d2

    # Compute the sum of these two integers
    w = m*9.81
    Fwind = w*d2/d1

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = Fwind
    data2["correct_answers"]["part2_ans"] = Fwind/w

    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
