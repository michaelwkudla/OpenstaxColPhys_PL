import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the time delay
    t1 = random.randint(5, 15) #mm
    t2 = random.randint(5, 15) #mm
    vfat = 1450 #m/s
    vmuscle = 1540 #m/s

    data2["params"]["t1"] = t1
    data2["params"]["t2"] = t2
    data2["params"]["vfat"] = vfat
    data2["params"]["vmuscle"] = vmuscle

    # Compute the time
    t1m = t1/1000
    t2m = t2/1000

    T = t1m/vfat*2 + t2m/vmuscle*2

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = T
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass