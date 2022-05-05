import random
import problem_bank_helpers as pbh
import numpy

def generate(data):
    data2 = pbh.create_data2()
    # store phrases etc    
    
    r = random.randint(15,25)
    rpm = random.randint(26, 35)

    T = 60/rpm
    omega = 2*numpy.pi/T
    ac = r*omega**2

    
    data2["params"]["r"] = r
    data2["params"]["rpm"] = rpm
    
    ## Part 1
    # define correct answers
    data2["correct_answers"]["part1_ans"] = T
    
    ## Part 2
    
    # define correct answers
    data2["correct_answers"]["part2_ans"] = omega
    
    ## Part 3 
    
    # define correct answers
    data2["correct_answers"]["part3_ans"] = ac
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
