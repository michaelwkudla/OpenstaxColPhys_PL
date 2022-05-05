import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the force and area
    d = round(random.uniform(1, 1.5), 2) #mm
    F = random.randint(1500,2500)

    data2["params"]["d"] = d
    data2["params"]["F"] = F

    # Compute the pressure
    dm = d/1000
    A = numpy.pi*(dm/2)**2
    P = F/A

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