import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    height20 = 553.33 #m
    T0 = 20 # deg C
    T1 = random.randint(30,40)
    T2 = random.randint(-20,-10)
    h1 = height20*(1+(12*10**(-6)) * (T1-T0))
    h1 = round(h1,2)
    h2 = height20*(1+(12*10**(-6)) * (T2-T0))
    h2 = round(h2,2)

    data2["params"]["T1"] = T1
    data2["params"]["T2"] = T2
    data2["params"]["h1"] = h1

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = h2
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass