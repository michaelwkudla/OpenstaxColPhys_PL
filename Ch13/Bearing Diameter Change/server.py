import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    d1 = round(random.uniform(5, 7), 2) #cm
    d2 = round(d1 + 0.05,2)  
    alpha = 11*10**-6

    d1m = d1/100
    d2m = d2/100

    C1m = numpy.pi*d1m
    C2m = numpy.pi*d2m
    dC = C2m - C1m
    dT = dC/alpha/C1m

    data2["params"]["d1"] = d1
    data2["params"]["d2"] = d2
    data2["params"]["alpha"] = alpha

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = dT
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass