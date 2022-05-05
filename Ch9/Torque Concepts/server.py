import random
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()
    
    # Part 1 possible answers
    data2["params"]["part1"]["ans1"]["value"] = "F1"
    data2["params"]["part1"]["ans1"]["correct"] = False
    
    data2["params"]["part1"]["ans2"]["value"] = "F2"
    data2["params"]["part1"]["ans2"]["correct"] = True
    
    data2["params"]["part1"]["ans3"]["value"] = "Both"
    data2["params"]["part1"]["ans3"]["correct"] = False
    
    data2["params"]["part1"]["ans4"]["value"] = "Neither"
    data2["params"]["part1"]["ans4"]["correct"] = False

    # Part 2 possible answers
    data2["params"]["part2"]["ans1"]["value"] = "Counter-Clockwise"
    data2["params"]["part2"]["ans1"]["correct"] = True
    
    data2["params"]["part2"]["ans2"]["value"] = "Clockwise"
    data2["params"]["part2"]["ans2"]["correct"] = False
    
    data2["params"]["part2"]["ans3"]["value"] = "There is no net torque."
    data2["params"]["part2"]["ans3"]["correct"] = False
    
    data2["params"]["part2"]["ans4"]["value"] = "Neither"
    data2["params"]["part2"]["ans4"]["correct"] = False

    # Part 3 possible answers
    data2["params"]["part3"]["ans1"]["value"] = "Quarted"
    data2["params"]["part3"]["ans1"]["correct"] = False
    
    data2["params"]["part3"]["ans2"]["value"] = "The Same"
    data2["params"]["part3"]["ans2"]["correct"] = False
    
    data2["params"]["part3"]["ans3"]["value"] = "Halved"
    data2["params"]["part3"]["ans3"]["correct"] = True
    
    data2["params"]["part3"]["ans4"]["value"] = "Doubled"
    data2["params"]["part3"]["ans4"]["correct"] = False
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
