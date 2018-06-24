from __future__ import print_function
import unittest
import numpy as np

from numpy.random import randint, seed
from ratcave import PhysicalGraph
from _transformations import inverse_matrix as inv

seed(100)
np.set_printoptions(suppress=True, precision=5)

class TestPhysicalGraph(unittest.TestCase):
    """
    Run tests from main project folder.
    """
    def test_child_update_model_matrix_transform_function(self):
        for _ in range(200):
            child =  PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3))
            parent = PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3))
            new_mm = np.dot(inv(parent.model_matrix), child.model_matrix)
            self.assertTrue( np.isclose(child.model_matrix, np.dot(parent.model_matrix, new_mm)).all())


    def test_add_child_connection(self):
        for _ in range(200):
            child =  PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3))
            parent = PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3))

            old_mm = child.model_matrix_global.copy()
            parent.add_child(child, modify=False)

            self.assertFalse(np.isclose(old_mm, child.model_matrix_global).all())


    def test_add_child_connection_modify(self):
        # N = P * O
        for _ in range(200):
            child =  PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3))
            parent = PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3))

            old_mm = child.model_matrix_global.copy()
            parent.add_child(child, modify=True)

            self.assertTrue(np.isclose(old_mm, child.model_matrix_global, atol=1.e-4).all())  # TODO: Improve numerical accuracy of parenting


    def test_add_child_connection_modify_scale(self):
        # N = P * O
        for _ in range(200):
            child =  PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3), scale=randint(1, 360))
            parent = PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3), scale=randint(1, 360))

            old_mm = child.model_matrix_global.copy()
            parent.add_child(child, modify=True)

            self.assertTrue(np.isclose(old_mm, child.model_matrix_global,atol=1.e-4).all())  # TODO: Improve numerical accuracy of parenting

    def test_set_parent_connection(self):
        for _ in range(2):
            child =  PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3))
            parent = PhysicalGraph(position=randint(0, 360, 3), rotation=randint(0, 360, 3))

            old_mm = child.model_matrix_global.copy()
            child.set_parent(child, modify=False)
            print('ch', child.model_matrix_global)
            print('old', old_mm)
            print('p', parent.model_matrix_global)

            self.assertFalse(np.isclose(old_mm, child.model_matrix_global).all())
