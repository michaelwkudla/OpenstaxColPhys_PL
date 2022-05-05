import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    Tlava = random.randint(1100,1300) # degC
    Tair = random.randint(25,35) # degC
    A = random.randint(1,3) # m^2
    sigma = 5.67*10**-8 #J/s*m^2*K^4
    e=1

    data2["params"]["Tlava"] = Tlava
    data2["params"]["Tair"] = Tair
    data2["params"]["A"] = A
    
    TlavaK = Tlava+273 #Kelvin
    TairK = Tair+273

    Qrate = sigma*e*A*(TairK**4 - TlavaK**4)

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = Qrate
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass