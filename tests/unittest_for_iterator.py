import unittest
import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import range_iterator
from range_iterator import *


class TestIterator(unittest.TestCase):

    def test_MyRange(self):
        iterator = range_iterator.MyRange(0, 10, 2)
        myrange_list = [0]
        for i in range(0, 8, 2):
            myrange_list.append(next(iterator))
        range_list = [i for i in range(0, 10, 2)]
        self.assertEqual(myrange_list, range_list)


unittest.main()