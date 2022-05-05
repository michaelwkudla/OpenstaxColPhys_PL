import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the depth and diameter
    depth = 10984 #m
    L = 7.3 #m
    d = 2 #m
    density = round(997*random.uniform(1.04, 1.05), 2) #kg/m^3
    
    data2["params"]["density"] = density

    # Compute the pressure
    P = depth * (1.025*10**3) * 9.81

    # Compute the buoyant force
    V = L*numpy.pi*(d/2)**2
    F = density * V * 9.81

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