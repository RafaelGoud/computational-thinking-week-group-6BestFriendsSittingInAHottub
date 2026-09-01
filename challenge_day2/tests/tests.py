import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utility', 'edutest'))
import edutest

class Test_Exercise_Values(edutest.TestCase):
    def test(self):
        self.io_pair(('00:01', 5, '1990-01-01', 3, 1, 'Lora', 9, 'a+b'), 1.00544313459462e+16)
        self.io_pair(('00:02', 6, '1990-01-02', 4, 2, 'Iris', 8, 'b+c'), 4.827884479828662e+16)
        self.io_pair(('00:03', 7, '1990-01-03', 5, 3, 'Minseo', 7, 'd*e'), 6.07785634489743e+16)

class Test_Exercise(edutest.TestSuite):
    test_cases = [
        Test_Exercise_Values
    ]
