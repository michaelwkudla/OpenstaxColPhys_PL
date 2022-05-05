import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    T1 = random.randint(20,30) # degC
    T2 = random.randint(150,200) # degC
    m_cake = round(random.uniform(1,1.5),2) #kg
    m_air = round(random.uniform(0.8,1),2) #kg
    m_steel = round(random.uniform(4,6),2) #kg
    c_cake = 2.516 #kJ/kg
    c_air = 1.012
    c_steel = 0.446

    dT = T2-T1

    data2["params"]["T1"] = T1 
    data2["params"]["T2"] = T2

    data2["params"]["m_cake"] = m_cake
    data2["params"]["m_air"] = m_air
    data2["params"]["m_steel"] = m_steel

    data2["params"]["c_cake"] = c_cake
    data2["params"]["c_air"] = c_air
    data2["params"]["c_steel"] = c_steel

    Qcake = m_cake*c_cake*dT
    Qair = m_air*c_air*dT
    Qsteel = m_steel*c_steel*dT

    Qtotal = Qcake + Qair + Qsteel
    ratio = Qcake/Qtotal

    # Put the answers into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = Qcake
    data2["correct_answers"]["part2_ans"] = Qtotal
    data2["correct_answers"]["part3_ans"] = ratio

    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass