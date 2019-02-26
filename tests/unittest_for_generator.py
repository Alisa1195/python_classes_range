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

    def test_my_range(self):
        generator = range_generator.MyRange(0, 10, 2)
        self.assertEqual(0, next(generator))

unittest.main()


