import random
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()
    # store phrases etc
    data2["params"]["vars"]["title"] = "Force, Acceleration, and Friction"
    
    # Variables
    m = random.randint(5,10) #kg
    mu_s = round(random.uniform(0.41, 0.6),2)
    mu_k = round(random.uniform(0.2, 0.4),2)
    a1 = round(random.uniform(3,8),2)
    
    # store the variables in the dictionary "params"
    data2["params"]["m"] = m
    data2["params"]["mu_s"] = mu_s
    data2["params"]["mu_k"] = mu_k
    data2["params"]["a1"] = a1
    
    F1 = m*a1
    F2 = mu_s*m*9.81
    F3 = round(F2 + 30, 2)
    a2 = (F3 - mu_k*m*9.81)/m

    data2["params"]["F3"] = F3
    
    
    ## Part 1
    # define correct answers
    data2["correct_answers"]["part1_ans"] = F1
    
    ## Part 2
    
    # define correct answers
    data2["correct_answers"]["part2_ans"] = F2
    
    ## Part 3 
    
    # define correct answers
    data2["correct_answers"]["part3_ans"] = a2
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
