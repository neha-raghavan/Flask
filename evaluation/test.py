import unittest
from .expression_evaluation import preTokenise, infix_evaluation
class Test_PreToken(unittest.TestCase):
    def test_pre_token(self):
        self.assertEqual(preTokenise('(5-1)'),['(','5','-','1',')'])
        self.assertEqual(preTokenise('(40*6)'),['(','40','*','6',')'])
        self.assertEqual(preTokenise('(4*6-(8+4))'),['(','4','*','6','-','(','8','+','4',')',')'])
        self.assertEqual(preTokenise('(-401*6-(8+4))'),['(','-401','*','6','-','(','8','+','4',')',')'])
        self.assertEqual(preTokenise('((-4*6)/(8+4))'),['(','(','-4','*','6',')','/','(','8','+','4',')',')'])
        self.assertEqual(preTokenise('(-4*6)-(-8+4)'),['(','-4','*','6',')','-','(','-8','+','4',')'])
        # for the case of simplicity the case when - comes at the very first is ignored.

class Test__infix_evaluatuon(unittest.TestCase):
    def test_infix_evaluation(self):
        self.assertEqual(infix_evaluation('5+6'),11)
        self.assertEqual(infix_evaluation('5*3+2'),17)