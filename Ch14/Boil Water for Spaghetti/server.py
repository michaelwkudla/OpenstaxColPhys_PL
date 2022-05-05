import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    T1 = random.randint(20,30) # degC
    m = round(random.uniform(1,1.5),2) #kg
    cw = 4.186 #kJ/kg
    Lv = 2256 #kJ/kg*K

    dT = 100-T1

    data2["params"]["T1"] = T1 
    data2["params"]["m"] = m

    Q1 = m*cw*dT
    Q2 = m*Lv

    Qtotal = Q1 + Q2

    # Put the answers into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = Qtotal
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass