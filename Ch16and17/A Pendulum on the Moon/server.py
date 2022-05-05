import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    TMTE = 2.45

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = TMTE
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass