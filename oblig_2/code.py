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


    def test_grid_spread(self):
        [x, y, u, v, xit, yit] = self.get_data()

        print ""
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

        print ""
        print "Grid is eavenly spread, looks good!"

        return True


    def test_y_range(self):
        [x, y, u, v, xit, yit] = self.get_data()

        print ""
        print "Spread in y direction:"
        print y


    def plot_contours(self):
        [x, y, u, v, xit, yit] = self.get_data()

        c = np.sqrt(u**2 + v**2)

        plt.subplot(2,1,1)
        plt.contourf(x, y, c, 15)
        plt.colorbar()

        dataset.set_plot_desc("Fartsstruktur", "", "y [mm]")

        self.plot_line_of_seperation()

        plt.subplot(2,1,2)
        plt.contourf(x, y, c, 200)
        plt.colorbar()

        dataset.set_plot_desc("", "x [mm]", "y [mm]")

        self.plot_line_of_seperation()

        plt.show()


    def plot_line_of_seperation(self):
        plt.plot([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 96],[-3, -8, -11, -13, -14, -15, -15, -14, -14, -13, -13], linewidth=4, color="r")
 

    def plot_quiver(self, x_0, x_1, y_0, y_1, step, render_squares):
        [x, y, u, v, xit, yit] = self.get_data()

        plt.quiver(x[x_0:x_1:step, y_0:y_1:step], y[x_0:x_1:step, y_0:y_1:step], u[x_0:x_1:step, y_0:y_1:step], v[x_0:x_1:step, y_0:y_1:step])

        dataset.set_plot_desc("Hastighetsfelt av vaesken", "x [mm]", "y [mm]")

        if render_squares:
            self.plot_squares()

        plt.axis([0, 100, -50, 50])

        plt.show()


    def plot_square(self, c0, c1):
        [x, y, u, v, xit, yit] = self.get_data()

        x0 = x[c0[1]][c0[0]]
        y0 = y[c0[1]][c0[0]]

        x1 = x[c1[1]][c1[0]]
        y1 = y[c1[1]][c1[0]]

        plt.plot([x0, x1], [y1, y1], linewidth=2.0, color='b')
        plt.plot([x0, x0], [y0, y1], linewidth=2.0, color='g')
        plt.plot([x0, x1], [y0, y0], linewidth=2.0, color='r')
        plt.plot([x1, x1], [y0, y1], linewidth=2.0, color='c')


    def plot_squares(self):
        self.plot_square([35, 160],[70, 170])
        self.plot_square([35, 85],[70, 100])
        self.plot_square([35, 50],[70, 60])


    def plot_divergence(self):
        [x, y, u, v, xit, yit] = self.get_data()
        div = self.divergence([u, v])
        div = sio.divergence(u, v)
        plt.contourf(x, y, div)
        plt.colorbar()

        self.plot_squares()

        dataset.set_plot_desc("Divergensen", "x [mm]", "y [mm]")

        plt.show()


    def plot_zcomp(self, render_quiver):
        [x, y, u, v, xit, yit] = self.get_data()
        div = self.divergence([u, -v])
        plt.contourf(x, y, div)
        plt.colorbar()

        x0 = y0 = 0
        x1 = 191
        y1 = 201
        step = 5

        if render_quiver:
            plt.quiver(x[x0:x1:step, y0:y1:step], y[x0:x1:step, y0:y1:step], u[x0:x1:step, y0:y1:step], v[x0:x1:step, y0:y1:step])

        self.plot_squares()

        dataset.set_plot_desc("Divergensen", "x [mm]", "y [mm]")

        plt.show()


    def divergence(self, f):
        num_dims = len(f)
        return np.ufunc.reduce(np.add, [np.gradient(f[i], axis=i) for i in range(num_dims)])


    def divergence(self, f):
        num_dims = len(f)
        return np.ufunc.reduce(np.add, [np.gradient(f[i], axis=i) for i in range(num_dims)])


    def set_plot_desc(self, title, xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)


# Problem a)
dataset = DataSet("data.mat")
dataset.get_matrices_sizes()
dataset.test_grid_spread()
dataset.test_y_range()

# Problem b)
dataset.plot_contours()

# Problem c)
dataset.plot_quiver(0, 194, 0, 201, 8, False)
dataset.plot_quiver(0, 194, 0, 201, 8 ,True)

# Problem d)
#dataset.plot_divergence()

# Problem e)
#dataset.plot_zcomp(False)
#dataset.plot_zcomp(True)

# Problem f)

# Problem g)












