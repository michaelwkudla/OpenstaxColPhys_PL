import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the variables
    T = random.randint(15,30)
    v = random.randint(200,250)
    vms = v*1000/3600
    rpm = random.randint(8000, 12000)
    
    # Compute the speed of sound in the air
    v_air = 331*numpy.sqrt((273+T)/273)

    # Compute the period heard
    f = rpm/60
    period = 1/f

    # Compute the frequencies by the observer before and after the car passes
    rpm_actual = rpm*(v_air-vms)/v_air

    # Assign the variables to data
    data2["params"]["T"] = T
    data2["params"]["v"] = v
    data2["params"]["rpm"] = rpm

    # Put the answer(s) into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = period
    data2["correct_answers"]["part2_ans"] = rpm_actual

    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass