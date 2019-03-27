class StaticStateUpdater:
    def __init__(self, state, final, ramifications=[], transitions=[]):
        self.state = state
        self.ramifications = ramifications
        self.transitions = transitions
        self.final = final

    def addRamifications(self, ramification):
        self.ramifications.append(ramification)

    def isFinal(self):
        return self.state == self.final

    def getAllStates(self):
        states = []
        for i in range(len(self.ramifications)):
            nextState = self.ramifications[i](self.state, self.state.copy())
            if nextState is not None:
                nextTransitions = self.transitions.copy()
                nextTransitions.append(i)
                nextState = StaticStateUpdater(
                    nextState, self.final, self.ramifications, nextTransitions)
                states.append(nextState)
        return states

    def __eq__(self, value):
        return self.state == value.state

    def __str__(self):
        return self.state.__str__()
