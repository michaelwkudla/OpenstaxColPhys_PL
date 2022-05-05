import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the power and heights
    P = round(random.uniform(8, 12), 2)
    h1 = round(random.uniform(1,1.5), 2)
    h2 = round(random.uniform(0.5, 0.9), 2)

    data2["params"]["P"] = P
    data2["params"]["h1"] = h1
    data2["params"]["h2"] = h2

    # Compute the power
    P2 = P*(h2/h1)**2

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = P2
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass