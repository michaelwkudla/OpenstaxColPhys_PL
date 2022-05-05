import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the variables
    f1 = random.randint(30,40)
    f2 = random.randint(85,95)

    # Compute the overtones for the closed end instrument
    o1close = 3*f1
    o2close = 5*f1
    o3close = 7*f1

    # Compute the overtones for the open end instrument
    o1open = 2*f2
    o2open = 3*f2
    o3open = 4*f2

    # Assign the variables to data
    data2["params"]["f1"] = f1
    data2["params"]["f2"] = f2

    # Put the answer(s) into data['correct_answers']
    data2["correct_answers"]["part1_ans1"] = o1close
    data2["correct_answers"]["part1_ans2"] = o2close
    data2["correct_answers"]["part1_ans3"] = o3close

    data2["correct_answers"]["part2_ans1"] = o1open
    data2["correct_answers"]["part2_ans2"] = o2open
    data2["correct_answers"]["part2_ans3"] = o3open

    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass