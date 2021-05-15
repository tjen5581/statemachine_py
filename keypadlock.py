import time
import random
from statemachine import StateMachine

input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def t0_transitions(input):
    print("start state")
    print("current state: q0\tinput: {}".format(input))
    if input == "1":
        newState = "t1"
    elif input == "#":
        newState = "t0"
    elif input in alphabet:
        newState = "t7"
    else:
        newState = "error_state"
    time.sleep(2)
    
    return newState, input

def t1_transitions(input):
    print("current state: q1\tinput: {}".format(input))
    if input == "4":
        newState = "t2"
    elif input == "#":
        newState = "t0"
    elif input in alphabet:       
        newState = "t8"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t2_transitions(input):
    print("current state: t2\tinput: {}".format(input))
    if input == "7":
        newState = "t3"
    elif input == "#":
        newState = "t0"
    elif input in alphabet: 
        newState = "t9"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t3_transitions(input):
    print("current state: t3\jinput: {}".format(input))
    if input == "2":
        newState = "t4"
    elif input == "#":
        newState = "t0"
    elif input in alphabet:  
        newState = "t10"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t4_transitions(input):
    print("current state: t4\jinput: {}".format(input))
    if input == "5":
        newState = "t5"
    elif input == "#":
        newState = "t0"
    elif input in alphabet:   
        newState = "t11"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t5_transitions(input):
    print("current state: t5\tinput: {}".format(input))
    if input == "8":
        print("UNLOCKED")
        time.sleep(2)
        newState = "t12"
    elif input == "#":
        newState = "t0"
    elif input in alphabet:  
        print("INCORRECT COMBINATION.")
        newState = "t0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t7_transitions(input):
    print("current state: t7\tinput: {}".format(input))
    if input in alphabet: 
        newState = "t8"
    elif input == "#":
        newState = "t0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t8_transitions(input):
    print("current state: t8\jinput: {}".format(input))
    if input in alphabet: 
        newState = "t9"
    elif input == "#":
        newState = "t0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t9_transitions(input):
    print("current state: t9\jinput: {}".format(input))
    if input in alphabet: 
        newState = "t10"
    elif input == "#":
        newState = "t0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t10_transitions(input):
    print("current state: t10\jinput: {}".format(input))
    if input in alphabet: 
        newState = "t11"
    elif input == "#":
        newState = "t0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t11_transitions(input):
    print("current state: t11\jinput: {}".format(input))
    if input in alphabet: 
        print("INCORRECT COMBINATION.")
        newState = "t0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def t12_transitions(input):
    print("current state: final state\tinput: {}".format(input))
    

if __name__ == "__main__":
    m = StateMachine()
    m.add_state("t0", t0_transitions)
    m.add_state("t1", t1_transitions)
    m.add_state("t2", t2_transitions)
    m.add_state("t3", t3_transitions)
    m.add_state("t4", t4_transitions)
    m.add_state("t5", t5_transitions)
   
  #m.add_state("t6", t6_transitions) #, end_state=1)
    m.add_state("t7", t7_transitions)
    m.add_state("t8", t8_transitions)
    m.add_state("t9", t9_transitions)
    m.add_state("t10", t10_transitions)
    m.add_state("t11", t11_transitions)
    m.add_state("t12", t12_transitions, end_state = 1)
    m.set_start("t0")

    #Test 1
    m.run("01#0010") 
    m.run("147259") # closest to actual answer but will fail
    m.run("14#7259174258")
    m.run("47258#")

  	#Test 2
    m.run("147258")

    #Random test 
    randTest = ""
    for i in range(random.choice([6])):
        randTest += str(random.choice([0, 10]))
    m.run(randTest)

    #User input 
    code = ""
    code += input("Enter code here.. press enter when complete: ")
    m.run(code)
    
