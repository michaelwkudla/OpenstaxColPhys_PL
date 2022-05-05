import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the masses
    m = random.randint(375,450)
    mapp = random.randint(300,360)

    data2["params"]["m"] = m
    data2["params"]["mapp"] = mapp

    # Compute the density
    m_displaced = m-mapp
    V = m/7.8
    rho = m_displaced/V

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = m_displaced
    data2["correct_answers"]["part2_ans"] = V
    data2["correct_answers"]["part3_ans"] = rho


    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass