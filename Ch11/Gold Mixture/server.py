import random, copy, numpy
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()

    # Randomly generate the masses
    gold = random.randint(17,20)
    silver = random.randint(4,7)
    copper = random.randint(1,3)

    data2["params"]["gold"] = gold
    data2["params"]["copper"] = copper
    data2["params"]["silver"] = silver

    # Compute the density
    p = (gold + copper + silver)/((gold/19.32 + copper/8.8 + silver/10.49)/10**3)

    # Put the sum into data['correct_answers']
    data2["correct_answers"]["part1_ans"] = p


    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass