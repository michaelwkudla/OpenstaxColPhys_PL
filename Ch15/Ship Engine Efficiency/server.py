import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    W = round(random.uniform(1.5, 2.5), 2)*10**8
    Q = round(random.uniform(5.5, 6.5), 2)*10**9
    e = random.randint(3,6)

    data2["params"]["W"] = W/10**8
    data2["params"]["Q"] = Q/10**9
    data2["params"]["e"] = e
    
    Qc = (1/(e/100)-1)*W
    N = (Qc+W)/Q

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = Qc
    data2["correct_answers"]["part2_ans"] = N
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass