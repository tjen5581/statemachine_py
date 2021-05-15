class KeypadLock:
	def __init__(self):
		self.handlers = {}
		self.startState = None
		self.endStates = []

	def add_state(self, j_state, handler, end_state=0):
		j_state = j_state.upper()
		self.handlers[j_state] = handler
		if end_state == 1:
		self.endStates.append(j_state)

	def set_start(self, j_state):
		self.startState = j_state.upper()

	def run(self, input): #, Iter):
		global handler
		try:
			#handler = self.handlers[self.start_transitions]
			
      			 handler = self.handlers[self.startState]
      
     			 #print('---------- run {} ----------'.format(input))
			
    		         str = "run " + input
			print(str.center(40, '-'))
		except:
			print("call set_start() before run()")
		if not self.endStates:
			print("one state must be an end_state")
		self.current_state = self.startState
		index = 0
		while index < len(input):
			keyEntry = input[index]
			#(newState, x) = handler(keyEntry)
			newState, x = handler(keyEntry)
			index += 1
			
      
			if newState.upper() in self.endStates:
        
				#print("entered end state") if the fsm enters end state
				break
			else:
				self.current_state = newState.upper()
				if newState.upper() in self.handlers.keys():
					handler = self.handlers[newState.upper()]
				else:
					break
		print('-'*40)
