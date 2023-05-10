import time

class StateMachine:
    # start in startUp state
    def __init__(self):
        self.state = 'startUp'
    
    def transition(self, action):
        if self.state == 'startUp' and action == 'toPassiveMode':
            print('Transitioning from startUp to passiveMode')
            self.state = 'passiveMode'

        # if passiveMode fails, it goes to activationFaliure state
        elif self.state == 'passiveMode' and action == 'failure':
            print('Transitioning from passiveMode to activationFaliure')
            self.state = 'activationFaliure'

        # if passiveMode succeeds, it goes to activeMode state
        elif self.state == 'passiveMode' and action == 'success': 
            print('Transitioning from passiveMode to activeMode')
            self.state = 'activeMode'

        # if in activation failure, it goes to activeMode state
        elif self.state == 'activationFaliure' and action == 'toPassiveMode':
            print('Transitioning from activationFaliure to passiveMode')
            self.state = 'passiveMode'

        elif self.state == 'activeMode' and action == 'deactivation':
            print('Transitioning from activeMode to deactivatedMode')
            self.state = 'deactivatedMode'

        elif self.state == 'deactivatedMode' and action == 'toPassiveMode':
            print('Transitioning from deactivatedMode to passiveMode')
            self.state = 'passiveMode'

        else:
            print('Invalid transition')

    def startUpChecks(self):
        status = True
        # put code to check during start up here

        print("startUpChecks Status:", status)
        return status

    def passiveModeCheck(self):
        status = True
        # put code to check during passive mode here
        # would be waiting for AV start signal
        # then once signal is recived, do all other checks and change status to false if any are wrong (maybe return part way through but that is kinda bad practice)

        print("passiveModeCheck Status:",status)
        return status
    
    def activationFaliureChecks(self):
        status = True
        # put code to check during this state here

        print("activationFaliureChecks Status:", status)
        return status
    
    def activeModeChecks(self):
        status = True
        # put code to check during this state here
        # maybe running whole car program in here?

        print("activeModeChecks Status:", status)
        return status
    
    def deactivatedModeChecks(self):
        status = True
        # put code to check during this state here

        print("deactivatedModeChecks Status:", status)
        return status


def main():
    print("Started Correctly\n")
    carStateMachine = StateMachine()
    machineStatus = True

    while True:
        if carStateMachine.state == 'startUp':
            # condition for if is checking code needed in start up is all good and for running nessecary internal code
            if carStateMachine.startUpChecks() == True:
                carStateMachine.transition('toPassiveMode')
            else:
                # throw error
                machineStatus = False
        
        elif carStateMachine.state == 'passiveMode':
            # calling all checking needed inside state and running nessecary internal code
            if carStateMachine.passiveModeCheck() == True:
                carStateMachine.transition('success')
            else:
                carStateMachine.transition('failure')

        elif carStateMachine.state == 'activationFaliure':
            # calling all checking needed inside state and running nessecary internal code
            if carStateMachine.activationFaliureChecks() == True:
                carStateMachine.transition('toPassiveMode')
            else:
                machineStatus  = False

        elif carStateMachine.state == 'activeMode':
            # calling all checking needed inside state and running nessecary internal code
            # i.e. maybe running whole car program in here?
            if carStateMachine.activeModeChecks() != True:
                carStateMachine.transition('deactivation')

        elif carStateMachine.state == 'deactivatedMode':
            # calling all checking needed inside state and running nessecary internal code
            if carStateMachine.deactivatedModeChecks() == True:
                carStateMachine.transition('toPassiveMode')

        else:
            # there is an error
            machineStatus = False

        if machineStatus == False:
            print("Big Goofy Error. Current state:", carStateMachine.state)
            break
        else:
            print('Working. \nCurrent state:', carStateMachine.state, "\n")
        
        # this is just so functionality is understandable when run
        time.sleep(1)
    

# call main to test
main()