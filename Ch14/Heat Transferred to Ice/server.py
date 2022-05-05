import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    T1 = random.randint(-35,-20) # degC
    T2 = random.randint(110, 130) # degC
    m = round(random.uniform(0.15,0.25),2) #kg
    ci = 2.09 #kJ/kg*K
    cw = 4.186 #kJ/kg
    cs = 1.52 #kJ/kg*K
    Lf = 334 #kJ/kg
    Lv = 2256 #kJ/kg*K

    dT1 = 0-T1
    dT2 = 100
    dT3 = T2-100

    data2["params"]["T1"] = T1 
    data2["params"]["T2"] = T2
    data2["params"]["m"] = m 

    Q1 = m*ci*dT1
    Q2 = m*Lf
    Q3 = m*cw*dT2
    Q4 = m*Lv
    Q5 = m*cs*dT3

    Qtotal = Q1 + Q2 + Q3 + Q4 + Q5

    # Put the answers into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = Q1
    data2["correct_answers"]["part2_ans"] = Q2
    data2["correct_answers"]["part3_ans"] = Q3
    data2["correct_answers"]["part4_ans"] = Q4
    data2["correct_answers"]["part5_ans"] = Q5
    data2["correct_answers"]["part6_ans"] = Qtotal
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass