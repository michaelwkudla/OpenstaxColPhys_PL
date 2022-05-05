import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    drop = random.randint(2,5) # mm
    V = random.randint(300,500) # cm3
    diameter = round(random.uniform(6, 8), 2) #cm
    T1 = random.randint(85,95) #degC
    T2 = random.randint(40,50) #degC

    data2["params"]["T1"] = T1
    data2["params"]["T2"] = T2
    data2["params"]["drop"] = drop
    data2["params"]["diameter"] = diameter
    data2["params"]["V"] = V

    betaw = 2.1*10**-4
    betag = 2.7*10**-5
    Vm = V/(100**3)
    dropmeters = drop/1000
    deltaT = T1-T2

    deltah = (betaw)*Vm*deltaT/(numpy.pi*(diameter/2/100)**2)*1000

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = deltah

    data2["params"]["part2"]["ans1"]["value"] = "No"
    data2["params"]["part2"]["ans1"]["correct"] = False
    data2["params"]["part2"]["ans2"]["value"] = "Yes"
    data2["params"]["part2"]["ans2"]["correct"] = True
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass