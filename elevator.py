
from typing import Union
from markupsafe import string


class Elevator:
    def __init__(self, id):
        """Create an elevator with current floor as one and an empty list of queue"""
        self.current_floor = 1
        self.queue = list()
        self.id = id
    
    def add_operation(self,operation):
        """Assign an operation to elevator"""
        self.queue.append(operation)
        

    def move_elevator(self):
        """moves elevator and check operation finished to removed of queue"""   
        if self.is_free() == True:
            if self.current_floor == 1:
                return
            else:
                self.current_floor -= 1
            return

        

        operation = self.queue[0]
         
        if self.current_floor == operation["go-to"]:
            print(str(self.id) + ' LIBERADO')
            self.queue.remove(operation)
            return
        
        for operation_in_queue in self.queue:
            if operation_in_queue["go-to"] == self.current_floor and operation_in_queue["direction"] == self.current_direction():
                print(str(self.id) + ' quitado')
                self.queue.remove(operation_in_queue)
                return

        if  self.current_floor < operation["go-to"]:
            self.current_floor += 1
        else:
            self.current_floor -= 1
        
        
    def is_free(self):
        """Check if an elevator has no operations"""
        return len(self.queue) == 0
    
    def can_serve_in_current_operation(self, operation) -> bool:
        """Check if an elevator can serve another operation"""
        if self.is_free():
            return False
        if self.current_direction() != operation["direction"]:
            return False
        if  self.current_direction() == operation["direction"]:
            if self.destination_floor() > operation["go-to"] and self.current_direction() == "down":
                return False
            if self.destination_floor() < operation["go-to"] and self.current_direction() == "up":
                return False
        return True
            
    def destination_floor(self) -> int:
        """Return current destination floor"""
        if self.is_free():
            return 1
        current_operation = self.queue[0]
        return current_operation["go-to"]
        
    
    def current_direction(self) -> string:
        """Return current direction"""
        if self.is_free():
            return None

        current_operation = self.queue[0]

        if self.current_floor < current_operation["go-to"]:
            return "up"
        elif self.current_floor > current_operation["go-to"]:
            return "down"
        else:
            return None


