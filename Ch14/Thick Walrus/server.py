import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    Qrate = random.randint(125,175)
    T1 = random.randint(-3,3)
    T2 = random.randint(33,39)
    A = round(random.uniform(1.5,2.5),2)
    k = 0.2
    d = k*A*(T2-T1)/Qrate*100

    data2["params"]["Qrate"] = Qrate
    data2["params"]["T1"] = T1
    data2["params"]["T2"] = T2
    data2["params"]["A"] = A

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = d
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass