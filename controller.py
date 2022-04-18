from elevator import Elevator 

class Controller:
    
    def __init__(self,floors: int,elevators: int):
        """Create floors and elevators"""
        self.floors = floors
        self.elevators = list()
        self.queue = list()
        for elevator in range(elevators):
            newElevator = Elevator(len(self.elevators)+1)
            self.elevators.append(newElevator)
        
    
    def getElevators(self) -> 'list[Elevator]':
        """Return a list of elevators"""
        return self.elevators
    
    def outside_calls(self,floor :int,direction :str):
        """Create an outside operation and assign outside operation to an elevator """
        operation = {"go-to":floor, "direction":direction, "type": "out"} 
        if self.__assign_outside_call(operation) == False:
            self.queue.append(operation)
    
    def __assign_outside_call(self, operation) -> bool:
        """Assign operation to a better elevator"""
        for elevator in self.getElevators():
            if elevator.can_serve_in_current_operation(operation) == True:
                elevator.add_operation(operation)
                return True

        elevators = sorted(self.elevators, key=lambda elevator: abs(elevator.current_floor - operation["go-to"]))
        
        for elevator in elevators:
            if elevator.is_free() == True:
                print('operacion asignada a ' + str(elevator.id))
                elevator.add_operation(operation)
                return True 

        return False


    def inside_calls(self,elevator,floor):
        """Assign inside operation to an elevator"""
        selected_elevator = self.elevators[elevator - 1]
        if floor > selected_elevator.current_floor:
            direction = "up"
        else:
            direction = "down"
        operation = {"go-to":floor,"direction":direction, "type": "in"}
        selected_elevator.add_operation(operation)
        
    
    def call_move_elevator(self):
        """Call move elevator metod of all Elevators class"""
        for elevator in self.getElevators():
            elevator.move_elevator()
        for operation in self.queue:
            if self.__assign_outside_call(operation) == True:
                self.queue.remove(operation)
            

    def render(self):
        """Render controller"""
        for floor in reversed(range(self.floors)):    
            current_floor = floor+1 
            print(str(current_floor) + '|',end="")
            for elevator in self.getElevators():
                if elevator.current_floor == current_floor:
                    print('X|',end="")
                else:
                    print(' |',end="")
            
            print('\n',end="")
