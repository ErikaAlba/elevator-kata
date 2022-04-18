import unittest
from controller import Controller

class ControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = Controller(8,2)
    
    def test_constructor(self):
        self.assertEqual(8,self.controller.floors)
        self.assertEqual(2,len(self.controller.elevators))
        self.assertTrue(len(self.controller.queue) == 0)
    
    def test_get_elevators(self):
        self.assertTrue(len(self.controller.elevators) == 2)
    
    def test_outside_calls(self):
        self.controller.elevators[0].current_floor = 1
        self.controller.elevators[1].current_floor = 2
        self.controller.outside_calls(5,"up")
        self.assertTrue(len(self.controller.elevators[1].queue) == 1)
        self.assertTrue(len(self.controller.elevators[0].queue) == 0)
    
    def test_inside_calls(self):
        self.controller.inside_calls(2,5)
        self.assertTrue(len(self.controller.elevators[1].queue) == 1)
        self.assertTrue(len(self.controller.elevators[0].queue) == 0)
    
    


if __name__ == "__main__":
    unittest.main()