from __future__ import print_function
import unittest
import numpy as np
from numpy.random import randn, randint

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

        for scale in abs(randn(10)) * randint(1, high=100, size=10):
            phys = Physical(scale=scale)
            scale_fm = coordinates.Scale.from_matrix(phys.model_matrix)

            self.assertTrue(np.isclose(scale_fm.x, scale))
            self.assertTrue(np.isclose(scale_fm.y, scale))
            self.assertTrue(np.isclose(scale_fm.z, scale))

            phys = Physical(scale=scale, rotation=(1., 2., 3.))
            scale_fm = coordinates.Scale.from_matrix(phys.model_matrix)

            self.assertTrue(np.isclose(scale_fm.x, scale))
            self.assertTrue(np.isclose(scale_fm.y, scale))
            self.assertTrue(np.isclose(scale_fm.z, scale))

            # phys = Physical(scale=scale, rotation=(1., 2., 3.))
        # scale = abs(randn(3)) * randint(1, high=100)

    def test_scale_from_matrix_multi(self):
        for _ in range(1):
            scale = abs(randint(1, high=100, size=3))
            phys = Physical()
            phys.scale.x = scale[0]
            phys.scale.y = scale[1]
            phys.scale.z = scale[2]
            scale_fm = coordinates.Scale.from_matrix(phys.model_matrix)

            self.assertTrue(np.isclose(scale_fm.x, scale[0]))
            self.assertTrue(np.isclose(scale_fm.y, scale[1]))
            self.assertTrue(np.isclose(scale_fm.z, scale[2]))


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
