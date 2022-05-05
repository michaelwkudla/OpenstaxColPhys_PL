import random
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()
    # store phrases etc
    data2["params"]["vars"]["title"] = "Sun Moon Mars Gravity"
    
    
    # Masses in kg
    m_Sun = 1989100000*10**21
    m_Moon = 73.5*10**21
    m_Mars = 641.71*10**21
    
    # radii in km
    r_Sun = 695508
    r_Moon = 1737.5
    r_Mars = 3389.5
    
    G = 6.67408*10**(-11)
    
    # store the variables in the dictionary "params"
    data2["params"]["m_Sun"] = m_Sun
    data2["params"]["m_Moon"] = m_Moon
    data2["params"]["m_Mars"] = m_Mars
    data2["params"]["r_Sun"] = r_Sun
    data2["params"]["r_Moon"] = r_Moon
    data2["params"]["r_Mars"] = r_Mars
    
    
    a1 = G*m_Sun/(r_Sun*1000)**2
    a2 = G*m_Moon/(r_Moon*1000)**2
    a3 = G*m_Mars/(r_Mars*1000)**2
    
    
    
    ## Part 1
    # define correct answers
    data2["correct_answers"]["part1_ans"] = pbh.roundp(a1, sigfigs=2)
    
    ## Part 2
    
    # define correct answers
    data2["correct_answers"]["part2_ans"] = pbh.roundp(a2, sigfigs=2)
    
    ## Part 3 
    
    # define correct answers
    data2["correct_answers"]["part3_ans"] = pbh.roundp(a3, sigfigs=2)
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
