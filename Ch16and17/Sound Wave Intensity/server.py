import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the variables
    T = random.randint(15,30)
    P = round(random.uniform(0.4, 0.7), 2) 
    rho = 1.2
    
    # Compute the speed of sound in the air
    v_air = 331*numpy.sqrt((273+T)/273)

    # Compute the intensity
    I = P**2/(2*rho*v_air)

    # Compute the intensity level
    B = 10*numpy.log10(I/(10**(-12)))

    # Assign the variables to data
    data2["params"]["T"] = T
    data2["params"]["P"] = P
    data2["params"]["rho"] = rho


    # Put the answer(s) into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = I
    data2["correct_answers"]["part2_ans"] = B

    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass