import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    density = 2700 #kg/m^3
    V = random.randint(4, 6)*10**5
    T1 = random.randint(1150, 1250)
    T2 = random.randint(25, 35)
    dT = T2-T1
    c = 840 #J/kg*K
    t = 1*24*60*60
    
    data2["params"]["density"] = density
    data2["params"]["V"] = V
    data2["params"]["T1"] = T1
    data2["params"]["T2"] = T2
    

    Qrate = density*V*c*dT/t/10**6
    # Put the solution into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = Qrate
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass