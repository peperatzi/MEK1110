import scipy.io as sio
import numpy as np


class DataSet():
    def __init__(self, filename):
        filedata = sio.loadmat(filename)

        self.data = {"x":filedata.get("x"), "y":filedata.get("y"), "u":filedata.get("u"), "v":filedata.get("v"), "xit":filedata.get("xit"), "yit":filedata.get("yit") }


    def get_matrices_sizes(self):
        for key, value in self.data.items():
            [a, b] = np.shape(value)
            print "Size of [", key, "]:", b, a

        return True


    def test_pixel_spread(self):
        x = self.data["x"]
        y = self.data["y"]

        for iy in range(201):
            prev_x = 0
            prev_y =0
            for ix in range(1,192):
                if x[iy][ix]-prev_x != 0.5:
                    return False
                prev_x = x[iy][ix]

                if y[iy][ix]-prev_y != 0.5:
                    return False
                prev_y = y[iy][ix]

        return True


        def test_y_range(self):
            yit = 


dataset = DataSet("data.mat")
dataset.test_matrices_sizes()
dataset.test_pixel_spread()
dataset.test_y_range()






