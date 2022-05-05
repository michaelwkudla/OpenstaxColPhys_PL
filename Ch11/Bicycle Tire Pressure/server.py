import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()



    # Randomly generate the masses and pressure
    mrider = random.randint(50,100) #kg
    mbike = random.randint(10,20)
    P = random.randint(300, 400) #kpa

    data2["params"]["mrider"] = mrider
    data2["params"]["mbike"] = mbike
    data2["params"]["P"] = P

    # Compute the mass per tire and the area
    m_tire = (mrider + mbike)/2
    A = m_tire*9.81/(P*1000)*(100)**2 #area in cm^2

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = m_tire
    data2["correct_answers"]["part2_ans"] = A

    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass