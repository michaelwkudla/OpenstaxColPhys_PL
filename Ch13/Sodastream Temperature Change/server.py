import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    T1 = random.randint(20,30) #C
    P1 = random.randint(6900,7000) #kPa
    P2 = P1-300

    data2["params"]["T1"] = T1
    data2["params"]["P1"] = P1
    data2["params"]["P2"] = P2

    P1a = P1+101
    P2a = P2+101
    
    T1k = T1+273

    T2k = P2a*T1k/P1a
    T2 = T2k-273

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = T2
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass