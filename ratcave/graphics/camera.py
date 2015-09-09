import numpy as np
import mixins as mixins


class Camera(mixins.Physical):
    """A convenient object for controlling the scene viewing angle."""

    def __init__(self, position=(0., 0., 0.), rotation=(0., 0., 0.), fov_y=60., aspect=16. / 9., z_near=.01, z_far=4.5,
                 x_shift=0., y_shift=0., ortho_mode=False):
        """
        My camera class.

        Args:
            position (tuple): (x,y,z)
            rotation (tuple): (x,y,z)
            fov_y (float): vertical field of view (degrees)
            aspect (float): screen width/height
            z_near (float): near clipping distance
            z_far (float): far clipping distance
            x_shift (float): horizontal lens shift
            y_shift (float): vertical lens shift
            ortho_mode (bool): Whether to use orthographic projection instead of perpective projection.

        Return:
            Camera instance
        """

        mixins.Physical.__init__(self, position=position, rotation=rotation)

        # Set intrinsic Camera attributes (must be manually applied using update() method during Scene.draw())
        self.fov_y = fov_y
        self.aspect = aspect
        self.zNear = z_near
        self.zFar = z_far
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.ortho_mode = ortho_mode



    @property
    def shift_matrix(self):
        """The Camera's lens-shift matrix."""
        return np.array([[1.,           0.,           self.x_shift, 0.],
                         [0.,           1.,           self.y_shift, 0.],
                         [0.,           0.,                     1., 0.],
                         [0.,           0.,                     0., 1.]])

    @property
    def projection_matrix(self):
        """The Camera's Projection Matrix.  Will be an Orthographic matrix if ortho_mode is set to True."""

        zn, zf = self.zNear, self.zFar

        # Use orthographic projection if enabled, else use a perspective projection.
        if self.ortho_mode == True:
            # replace glOrtho (https://www.opengl.org/sdk/docs/man2/xhtml/glOrtho.xml)

            persp_mat = np.array([[(2.)/(2),                  0.,         0., 0.], #  2/(right-left), x
                                  [      0., 2./(2./self.aspect),         0., 0.], #  2/(top-bottom), y
                                  [      0.,                  0., -2/(zf-zn), 0.], # -2/(zFar-zNear), z
                                  [      0.,                  0.,         0., 1.]])

        else:
            # replace gluPerspective (https://www.opengl.org/sdk/docs/man2/xhtml/gluPerspective.xml)
            ff = 1./np.tan(np.radians(self.fov_y / 2.)) # cotangent(fovy/2)
            persp_mat =  np.array([[ff/self.aspect,    0.,              0.,                 0.],
                                  [             0.,    ff,              0.,                 0.],
                                  [             0.,    0., (zf+zn)/(zn-zf), (2.*zf*zn)/(zn-zf)],
                                  [             0.,    0.,             -1.,                 0.]])
            persp_mat = np.dot(persp_mat, self.shift_matrix)  # Apply lens shift

        return persp_mat



