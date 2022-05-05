import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the diameters
    d1 = random.randint(10,13) 
    d2 = random.randint(15,20)
    r = d2/d1

    data2["params"]["d1"] = d1
    data2["params"]["d2"] = d2

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = r

    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
