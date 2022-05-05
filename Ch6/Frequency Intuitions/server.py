import random
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()
    
    # Part 1 possible answers
    data2["params"]["part1"]["ans1"]["value"] = "The period is halved and the length is quartered."
    data2["params"]["part1"]["ans1"]["correct"] = True
    
    data2["params"]["part1"]["ans2"]["value"] = "The period is doubled and the length is quartered"
    data2["params"]["part1"]["ans2"]["correct"] = False
    
    data2["params"]["part1"]["ans3"]["value"] = "The period is halved and the length is quadrupled."
    data2["params"]["part1"]["ans3"]["correct"] = False
    
    data2["params"]["part1"]["ans4"]["value"] = "The period is doubled and the length is quadrupled."
    data2["params"]["part1"]["ans4"]["correct"] = False
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
