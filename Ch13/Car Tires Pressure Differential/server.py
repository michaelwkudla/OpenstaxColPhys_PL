import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    T1 = random.randint(30,40)
    P1 = round(random.uniform(2,3)*100,0)
    T2 = random.randint(-45,-35)

    data2["params"]["T1"] = T1
    data2["params"]["T2"] = T2
    data2["params"]["P1"] = P1
    
    T1k = T1+273
    T2k = T2+273

    P2 = P1*T2k/T1k
    P2 = round(P2,0)

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = P2
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass