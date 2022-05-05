import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    m = random.randint(830,850) # kg
    mrotor = random.randint(6,10) # kg
    T1 = random.randint(300,500) # degC
    v = random.randint(250,300) # kph
    d = random.randint(80,120) # m
    c = 300 # J/(kg *K)

    vm = v/3.6
    KE = 1/2*m*vm**2 #J
    Tf = KE/(mrotor*4*c) + T1
    
    
    data2["params"]["m"] = m
    data2["params"]["mrotor"] = mrotor
    data2["params"]["T1"] = T1
    data2["params"]["v"] = v
    data2["params"]["d"] = d
    data2["params"]["c"] = c
    

    # Put the answer into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = KE
    data2["correct_answers"]["part2_ans"] = Tf
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass