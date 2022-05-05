import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()



    # Randomly generate the depth and diameter
    depth = random.randint(20,90)
    d = round(random.uniform(0.35, 0.45), 2)

    data2["params"]["depth"] = depth
    data2["params"]["d"] = d

    # Compute the pressure and the force
    P = depth * (1.025*10**3) * 9.81
    F = P * 3.14159 * (d/2)**2

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = P
    data2["correct_answers"]["part2_ans"] = F

    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass