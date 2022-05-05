import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the time delay
    t = round(random.uniform(0.1, 0.3), 2) #ms

    data2["params"]["t"] = t

    # Compute the distance
    x = (1450*t*10**-3)/2*100 # cm

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = x
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass