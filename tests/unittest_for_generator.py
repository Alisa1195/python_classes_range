import unittest
import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import range_generator
from range_generator import *


class TestGenerator(unittest.TestCase):

    def test_MyRange(self):
        generator = range_generator.MyRange(0, 10, 2)
        self.assertEqual(0, next(generator))
        self.assertEqual(2, next(generator))
        self.assertEqual(4, next(generator))
        self.assertEqual(6, next(generator))
        self.assertEqual(8, next(generator))

        generator = range_generator.MyRange(0, 100, 10)
        a = 0
        for i in range(10):
            a = next(generator)
        self.assertEqual(90, a)



unittest.main()


