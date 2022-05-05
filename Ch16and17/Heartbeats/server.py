import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the bpm
    bpm = random.randint(150,200)

    data2["params"]["bpm"] = bpm

    # Compute the density
    bps = bpm/60
    T = 1/bps

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