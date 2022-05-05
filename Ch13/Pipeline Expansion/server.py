import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    L0 = 90 #m
    T0 = 20 # deg C
    alpha = 0.000011
    
    T1 = random.randint(30,40)
    T2 = random.randint(-20,-10)
    
    L1 = L0*(1+alpha * (T1-T0))
    L1 = round(L1,3)
    
    L2 = L0*(1+alpha * (T2-T0))
    L2 = round(L2,3)

    data2["params"]["T1"] = T1
    data2["params"]["T2"] = T2
    data2["params"]["L1"] = L1
    data2["params"]["alpha"] = alpha
    
    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = L2
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass