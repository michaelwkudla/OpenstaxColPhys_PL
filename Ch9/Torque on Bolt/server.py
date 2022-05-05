import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()



    # Randomly generate the force and distance
    F = random.randint(20,90)
    d = round(random.uniform(0.1, 0.3), 2)

    data2["params"]["F"] = F
    data2["params"]["d"] = d

    # Compute the sum of these two integers
    T = F * d

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = T
    data2["correct_answers"]["part2_ans"] = T*0.7376

    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass