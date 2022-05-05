import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the diameter of the bubble.
    d = random.randint(5,20)

    data2["params"]["d"] = d

    # Compute the pressure inside the bubble
    P = 4*0.037/(d/2/1000)*(1/133)

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