import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the dimensions of the mattress and the mass.
    d1 = random.randint(210,250)
    d2 = random.randint(125,200) 
    d3 = random.randint(20,35) 
    m = random.randint(1, 5)

    data2["params"]["d1"] = d1
    data2["params"]["d2"] = d2
    data2["params"]["d3"] = d3
    data2["params"]["m"] = m

    # Compute the mass of the person.
    W_displaced = d1*d2*d3*1000*9.81/(100**3) 
    W_person = W_displaced - m*9.81
    m_person = W_person/9.81

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = m_person
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass