from tkinter import *
import json


class Airtools:

    def __init__(self, master):
        self.master = master
        master.title("Airtools")
        master.geometry("640x480")
        master.configure(border=0, bg="black")

        # variables
        self.CL = 0.764  # lift coefficient
        self.CD = 0.016  # drag coefficient
        self.V = 23  # speed (m/s)
        self.S = 0.156  # wing area(m^2)
        self.ro = 1.225  # air density
        self.W = 1.8  # Weight (Kg)
        self.g = 9.81  # Gravity

        self.L = 0 # Lift /newton
        self.D = 0 # drag /newton
        self.Vs = 0# stall speed /m/s

        #texts
        self.cl_label = Label(master, text="CL")
        self.cl_label.place(x=25, y=50)

        self.cd_label = Label(master, text="CD")
        self.cd_label.place(x=25, y=75)

        self.v_label = Label(master, text="V")
        self.v_label.place(x=25, y=100)

        self.s_label = Label(master, text="S")
        self.s_label.place(x=25, y=125)

        self.ro_label = Label(master, text="ro")
        self.ro_label.place(x=25, y=150)

        self.w_label = Label(master, text="W")
        self.w_label.place(x=25, y=175)

        self.g_label = Label(master, text="g")
        self.g_label.place(x=25, y=200)

        self.lift_label = Label(master, text="Lift: "+str(self.L))
        self.lift_label.place(x=250, y=50)

        self.stall_speed_label = Label(
            master, text="Stall Speed: "+str(self.Vs))
        self.stall_speed_label.place(x=250, y=75)

        self.drag_label = Label(master, text="Drag: "+str(self.D))
        self.drag_label.place(x=250, y=100)

        # widgets
        self.lift_btn = Button(master, text="Lift", command=self.calculate)
        self.lift_btn.place(x=50, y=225)

        self.read_btn = Button(master, text="SAVE PARAM",
                               command=self.save_param)
        self.read_btn.place(x=50, y=300)

        self.clear_btn = Button(master, text="WRITE PARAM",
                                command=self.write_param)
        self.clear_btn.place(x=50, y=325)

        self.cl_text_box = Text(master,
                                height=1,
                                width=5)
        self.cl_text_box.place(x=50, y=50)

        self.cd_text_box = Text(master,
                                height=1,
                                width=5)
        self.cd_text_box.place(x=50, y=75)

        self.v_text_box = Text(master,
                               height=1,
                               width=5)
        self.v_text_box.place(x=50, y=100)

        self.s_text_box = Text(master,
                               height=1,
                               width=5)
        self.s_text_box.place(x=50, y=125)

        self.ro_text_box = Text(master,
                                height=1,
                                width=5)
        self.ro_text_box.place(x=50, y=150)

        self.w_text_box = Text(master,
                               height=1,
                               width=5)
        self.w_text_box.place(x=50, y=175)

        self.g_text_box = Text(master,
                               height=1,
                               width=5)
        self.g_text_box.place(x=50, y=200)

    def lift(self):#calculate lift
        self.L = (self.CL * self.ro * self.S * (self.V ** 2)) / 2
        print("Lift= ", self.L, "N =", self.L / self.g, "Kg")
        self.lift_label = Label(self.master, text="Lift: "+str(self.L))
        self.lift_label.place(x=250, y=50)

    def stallspeed(self):#calculate stallspeed
        self.Vs = ((2 * self.W * self.g) /
                   (self.ro * self.S * self.CL)) ** (1 / 2)
        print("stallspeed= ", self.Vs, "m/s")
        self.stall_speed_label = Label(
            self.master, text="Stall Speed: "+str(self.Vs))
        self.stall_speed_label.place(x=250, y=75)

    def drag(self):#calculate drag
        self.D = (self.ro * (self.V ** 2) * self.CD * self.S) / 2
        print("Drag= ", self.D, "N")
        self.drag_label = Label(self.master, text="Drag: "+str(self.D))
        self.drag_label.place(x=250, y=100)

    def calculate(self):
        airtools.lift()
        airtools.stallspeed()
        airtools.drag()

    def save_param(self):

        self.CL = float(self.cl_text_box.get(1.0, "end-1c"))
        self.CD = float(self.cd_text_box.get(1.0, "end-1c"))
        self.V = float(self.v_text_box.get(1.0, "end-1c"))
        self.S = float(self.s_text_box.get(1.0, "end-1c"))
        self.ro = float(self.ro_text_box.get(1.0, "end-1c"))
        self.W = float(self.w_text_box.get(1.0, "end-1c"))
        self.g = float(self.g_text_box.get(1.0, "end-1c"))

        self.param = {
            "CL": self.CL,
            "CD": self.CD,
            "V": self.V,
            "S": self.S,
            "ro": self.ro,
            "W": self.W,
            "g": self.g
        }

        print(self.param)

        with open("param.json", "w") as outfile:
            outfile.write(json.dumps(self.param, indent=4))

    def write_param(self):

        with open('param.json', 'r') as openfile:

            # Reading from json file
            self.param = json.load(openfile)

            self.cl_text_box.delete(1.0, END)
            self.cd_text_box.delete(1.0, END)
            self.v_text_box.delete(1.0, END)
            self.s_text_box.delete(1.0, END)
            self.ro_text_box.delete(1.0, END)
            self.w_text_box.delete(1.0, END)
            self.g_text_box.delete(1.0, END)

            self.cl_text_box.insert('end', str(self.param["CL"]))
            self.cd_text_box.insert('end', str(self.param["CD"]))
            self.v_text_box.insert('end', str(self.param["V"]))
            self.s_text_box.insert('end', str(self.param["S"]))
            self.ro_text_box.insert('end', str(self.param["ro"]))
            self.w_text_box.insert('end', str(self.param["W"]))
            self.g_text_box.insert('end', str(self.param["g"]))


if __name__ == '__main__':
    root = Tk()
    airtools = Airtools(root)
    root.mainloop()
