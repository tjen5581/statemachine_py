import time
import random
from statemachine import StateMachine

input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def j0_transitions(input):
    print("start state")
    print("current state: j0\tinput: {}".format(input))
    if input == "1":
        newState = "j1"
    elif input == "#":
        newState = "j0"
    elif input in alphabet:
        newState = "j7"
    else:
        newState = "error_state"
    time.sleep(2)
    
    return newState, input

def j1_transitions(input):
    print("current state: j1\tinput: {}".format(input))
    if input == "4":
        newState = "j2"
    elif input == "#":
        newState = "j0"
    elif input in alphabet:       
        newState = "j8"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j2_transitions(input):
    print("current state: t2\tinput: {}".format(input))
    if input == "7":
        newState = "j3"
    elif input == "#":
        newState = "j0"
    elif input in alphabet: 
        newState = "j9"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j3_transitions(input):
    print("current state: j3\tinput: {}".format(input))
    if input == "2":
        newState = "j4"
    elif input == "#":
        newState = "j0"
    elif input in alphabet:  
        newState = "j10"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j4_transitions(input):
    print("current state: j4\tinput: {}".format(input))
    if input == "5":
        newState = "j5"
    elif input == "#":
        newState = "j0"
    elif input in alphabet:   
        newState = "j11"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j5_transitions(input):
    print("current state: j5\tinput: {}".format(input))
    if input == "8":
        print("UNLOCKED")
        time.sleep(2)
        newState = "j12"
    elif input == "#":
        newState = "j0"
    elif input in alphabet:  
        print("INCORRECT COMBINATION.")
        newState = "j0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j7_transitions(input):
    print("current state: j7\tinput: {}".format(input))
    if input in alphabet: 
        newState = "j8"
    elif input == "#":
        newState = "j0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j8_transitions(input):
    print("current state: j8\tinput: {}".format(input))
    if input in alphabet: 
        newState = "j9"
    elif input == "#":
        newState = "j0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j9_transitions(input):
    print("current state: j9\tinput: {}".format(input))
    if input in alphabet: 
        newState = "j10"
    elif input == "#":
        newState = "j0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j10_transitions(input):
    print("current state: j10\tinput: {}".format(input))
    if input in alphabet: 
        newState = "j11"
    elif input == "#":
        newState = "j0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j11_transitions(input):
    print("current state: j11\tinput: {}".format(input))
    if input in alphabet: 
        print("INCORRECT COMBINATION.")
        newState = "j0"
    else:
        newState = "error_state"
    time.sleep(2)
    return newState, input

def j12_transitions(input):
    print("current state: final state\tinput: {}".format(input))
    

if __name__ == "__main__":
    m = StateMachine()
    m.add_state("j0", j0_transitions)
    m.add_state("j1", j1_transitions)
    m.add_state("j2", j2_transitions)
    m.add_state("j3", j3_transitions)
    m.add_state("j4", j4_transitions)
    m.add_state("j5", j5_transitions)
   
  #m.add_state("j6", j6_transitions) #, end_state=1)
    m.add_state("j7", j7_transitions)
    m.add_state("j8", j8_transitions)
    m.add_state("j9", j9_transitions)
    m.add_state("j10", j10_transitions)
    m.add_state("j11", j11_transitions)
    m.add_state("j12", j12_transitions, end_state = 1)
    m.set_start("j0")

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
    
