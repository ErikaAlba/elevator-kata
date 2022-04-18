
import unittest
from elevator import *

class ElevatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.elevator = Elevator(1)

    def test_create_elevator(self):
        self.assertEqual(1,self.elevator.current_floor)
        self.assertTrue(len(self.elevator.queue) == 0)
        self.assertEqual(1,self.elevator.id)
    
    def test_add_operation(self):
        go_to = 1
        direction = "up"
        type = "in"
        operation = {"go-to":go_to,"direction":direction, "type": type}
        self.elevator.add_operation(operation)
        self.assertTrue(len(self.elevator.queue) == 1)
        self.assertEqual(
            go_to,
            self.elevator.queue[0]["go-to"]
        )
        self.assertEqual(
            direction,
            self.elevator.queue[0]["direction"]
        )
        self.assertEqual(
            type,
            self.elevator.queue[0]["type"]
        )
    
    def test_elevator_is_free(self):
        self.assertTrue(self.elevator.is_free())
        operation = {"go-to":1,"direction":"up", "type": "in"}
        self.elevator.add_operation(operation)
        self.assertFalse(self.elevator.is_free())


    def test_given_freeElevatorInFloorOne_when_moveElevator_then_noMove(self):
        self.elevator.move_elevator()
        self.assertEqual(1,self.elevator.current_floor)

    def test_given_freeElevatorInOtherFloor_when_moveElevator_then_move(self):
        self.elevator.current_floor = 3
        self.elevator.move_elevator() 
        self.assertEqual(2,self.elevator.current_floor)
    
    def test_sameCurrentFloor_sameOperationFloor(self):
        operation = {"go-to":3,"direction":"up", "type": "in"}
        self.elevator.add_operation(operation)
        self.elevator.current_floor = 3
        self.elevator.move_elevator()
        self.assertEqual(3,self.elevator.current_floor)
        self.assertTrue(len(self.elevator.queue) == 0)
    
    def test_operation_in_queue(self):
        self.elevator.current_floor = 5
        operation1 = {"go-to":3,"direction":"down", "type": "in"}
        self.elevator.add_operation(operation1)
        operation2 = {"go-to":5,"direction":"down", "type": "in"}
        self.elevator.add_operation(operation2)
        self.elevator.move_elevator()
        self.assertEqual(5,self.elevator.current_floor)
        self.assertTrue(len(self.elevator.queue) == 1)
    
    def test_move_elevator_up(self):
        self.elevator.current_floor = 2
        operation = {"go-to":3,"direction":"up", "type": "out"}
        self.elevator.add_operation(operation)
        self.elevator.move_elevator()
        self.assertEqual(3,self.elevator.current_floor)
    
    def test_move_elevator_down(self):
        self.elevator.current_floor = 3
        operation = {"go-to":2,"direction":"down", "type": "out"}
        self.elevator.add_operation(operation)
        self.elevator.move_elevator()
        self.assertEqual(2,self.elevator.current_floor)
    

    def test_can_serve_in_current_operation_and_differentDirection(self):
        self.elevator.current_floor = 2
        operation = {"go-to":3,"direction":"down", "type": "out"}
        self.elevator.add_operation(operation)
        self.assertFalse(self.elevator.can_serve_in_current_operation(operation))
    
    def test_can_serve_down_operation_with_smallerDestination(self):
        self.elevator.current_floor = 5
        operation = {"go-to":3,"direction":"down", "type": "out"}
        operationA = {"go-to":2,"direction":"down", "type": "out"}
        self.elevator.add_operation(operation)
        self.assertFalse(self.elevator.can_serve_in_current_operation(operationA))
    
    def test_can_serve_up_operation_with_biggerDestination(self):
        self.elevator.current_floor = 2
        operation = {"go-to":3,"direction":"up", "type": "out"}
        operationA = {"go-to":4,"direction":"up", "type": "out"}
        self.elevator.add_operation(operation)
        self.assertFalse(self.elevator.can_serve_in_current_operation(operationA))
    
    def test_can_serve_in_current_operation(self):
        self.elevator.current_floor = 2
        operation = {"go-to":5,"direction":"up", "type": "out"}
        operationA = {"go-to":3,"direction":"up", "type": "out"}
        self.elevator.add_operation(operation)
        self.assertTrue(self.elevator.can_serve_in_current_operation(operationA))
    
    def test_destination_floor(self):
        operation = {"go-to":5,"direction":"up", "type": "out"}
        self.elevator.add_operation(operation) 
        self.assertEqual(operation["go-to"],self.elevator.destination_floor())
    
    def test_current_direction_up(self):
        self.elevator.current_floor = 2
        operation = {"go-to":3,"direction":"up", "type": "out"}
        self.elevator.add_operation(operation)
        self.assertEqual("up",self.elevator.current_direction())
    
    def test_current_direction_down(self):
        self.elevator.current_floor = 3
        operation = {"go-to":2,"direction":"up", "type": "out"}
        self.elevator.add_operation(operation)
        self.assertEqual("down",self.elevator.current_direction())
    
    def test_current_direction_None(self):
        self.assertEqual(None,self.elevator.current_direction())

if __name__ == "__main__":
    unittest.main()