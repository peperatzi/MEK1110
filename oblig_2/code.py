import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

class DataSet():
    def __init__(self, filename):
        filedata = sio.loadmat(filename)
        self.data = {"x":filedata.get("x"), "y":filedata.get("y"), "u":filedata.get("u"), "v":filedata.get("v"), "xit":filedata.get("xit"), "yit":filedata.get("yit") }


    def get_data(self):
        return (self.data["x"], self.data["y"], self.data["u"], self.data["v"], self.data["xit"], self.data["yit"])


    def get_matrices_sizes(self):
        for key, value in self.data.items():
            [a, b] = np.shape(value)
            print "Size of [", key, "]:", b, a

        return True


    def test_pixel_spread(self):
        [x, y, u, v, xit, yit] = self.get_data()

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
        yit = 0


    def plot_contours(self):
        [x, y, u, v, xit, yit] = self.get_data()

        c = np.sqrt(u**2 + v**2)

        plt.subplot(2,1,1)
        plt.contour(x, y, c, 15)
        plt.colorbar()
        dataset.render_plot("Fartsstruktur i luft", "x [mm]", "y [mm]")

        plt.subplot(2,1,2)
        plt.contour(x, y, c, 200)
        plt.colorbar()
        dataset.render_plot("Fartsstruktur i vann", "x [mm]", "y [mm]")

        plt.show()
 

    def plot_quiver(self, x_0, x_1, y_0, y_1, step):
        [x, y, u, v, xit, yit] = self.get_data()

        plt.quiver(x[x_0:x_1:step, y_0:y_1:step], y[x_0:x_1:step, y_0:y_1:step], u[x_0:x_1:step, y_0:y_1:step], v[x_0:x_1:step, y_0:y_1:step])
        dataset.render_plot("Vektorfelt av vaesken", "x [mm]", "y [mm]")

        self.plot_square()

        plt.show()


    def plot_square(x_0, y_0, x_1, y_1):
        self.plot_line(x_0, x_1, y_0, 160, 'r')
        self.plot_line(35, 70, 160, 160, 'g')
        self.plot_line(35, 70, 160, 160, 'b')
        self.plot_line(35, 70, 160, 160, 'c')


    def plot_line(self, x_0, x_1, y_0, y_1, col):
        plt.plot([x_0, x_1], [y_0, y_1], col)


    def render_plot(self, title, xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)


# Problem a)
dataset = DataSet("data.mat")
dataset.get_matrices_sizes()
dataset.test_pixel_spread()
dataset.test_y_range()

# Problem b)
#dataset.plot_contours()

# Problem c)
dataset.plot_quiver(0, 194, 0, 201, 5)
#dataset.plot_quiver(35, 160, 70, 170, 5)
#dataset.plot_quiver(35, 85, 70, 100, 5)
#dataset.plot_quiver(35, 50, 70, 60, 5)


# Problem d)

# Problem e)

# Problem f)

# Problem g)












