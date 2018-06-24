from __future__ import print_function
import unittest
import numpy as np

from ratcave import coordinates, Physical

class TestCoordinates(unittest.TestCase):
    """
    Run tests from main project folder.
    """

    def test_position_from_matrix(self):
        # if you input an array instead of 4x4 matrix the if statement is false
        pos = coordinates.Translation(0., 0., 0.)

        matrix = np.zeros((4, 4))
        pos_fm = coordinates.Translation.from_matrix(matrix)

        self.assertTrue(pos.x == pos_fm.x)
        self.assertTrue(pos.y == pos_fm.y)
        self.assertTrue(pos.z == pos_fm.z)

        pos = coordinates.Translation(1., 1., 1.)
        matrix = np.ones((4, 4))
        pos_fm = coordinates.Translation.from_matrix(matrix)

        self.assertTrue(pos.x == pos_fm.x)
        self.assertTrue(pos.y == pos_fm.y)
        self.assertTrue(pos.z == pos_fm.z)

        pos = coordinates.Translation(1., 1., 1.)
        matrix = np.ones((4, 4))
        pos_fm = coordinates.Translation.from_matrix(matrix)

        self.assertTrue(pos.x == pos_fm.x)
        self.assertTrue(pos.y == pos_fm.y)
        self.assertTrue(pos.z == pos_fm.z)


    def test_scale(self): # TODO
        S = coordinates.Scale(1)

    def test_scale_from_matrix(self):
        phys = Physical(position=(1,1,1), rotation=(1,1,1))
        scale = 1, 2, 3.2
        phys.scale = scale
        scale_fm = coordinates.Scale.from_matrix(phys.model_matrix)

        scale_fm_matrix = scale_fm.to_matrix()
        scale_matrix = np.diag((scale[0], scale[1], scale[2], 1.))
        self.assertTrue(np.isclose(scale_matrix, scale_fm_matrix).all())

        for scale in (5, 6, 7):
            phys = Physical()
            phys.scale = scale
            scale_fm = coordinates.Scale.from_matrix(phys.model_matrix)
            scale_fm_matrix = scale_fm.to_matrix()
            scale_matrix = np.diag((scale, scale, scale, 1.))
            self.assertTrue(np.isclose(scale_matrix, scale_fm_matrix).all())

    # TODO:
    # def test_rotation(self):
    #     R = coordinates.RotationEulerDegrees(0., 0., 0.)
    #
    # def test_rotation_euler_degrees_from_matrix(self):
    #     matrix = np.identity(4)
    #     coordinates.RotationEulerDegrees.from_matrix(matrix)
    #
    # def test_rotation_euler_radains_from_matrix(self):
    #     matrix = np.identity(4)
    #     coordinates.RotationEulerRadians.from_matrix(matrix)
    #
    # def test_rotation_quaternions_from_matrix(self):
    #     matrix = np.identity(4)
    #     coordinates.RotationQuaternion.from_matrix(matrix)
