import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    g = 9.81
    g_pluto = 0.42
    T1 = round(random.uniform(2, 4), 2)
    L = (T1/(2*numpy.pi))**2 * g
    T2 = 2*numpy.pi*(L/g_pluto)**(1/2)

    data2["params"]["T1"] = T1
    data2["params"]["g_pluto"] = g_pluto

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