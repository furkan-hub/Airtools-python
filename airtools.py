from tkinter import *


class Airtools:

    def __init__(self, master):
        self.master = master
        master.title("Airtools")
        master.geometry("640x480")
        master.configure(border=0, bg="black")

        cl_label = Label(master, text="CL")
        cl_label.place(x=25, y=50)

        cd_label = Label(master, text="CD")
        cd_label.place(x=25, y=75)

        v_label = Label(master, text="V")
        v_label.place(x=25, y=100)

        s_label = Label(master, text="S")
        s_label.place(x=25, y=125)

        ro_label = Label(master, text="ro")
        ro_label.place(x=25, y=150)

        w_label = Label(master, text="W")
        w_label.place(x=25, y=175)

        g_label = Label(master, text="g")
        g_label.place(x=25, y=200)

        # variables
        self.CL = 0.764  # lift(taşıma) katsayısı
        self.CD = 0.016  # drag(sürtünme) Katsayısı
        self.V = 23  # Hız (m/s)
        self.S = 0.156  # kanat alanı(m^2)
        self.ro = 1.225  # hava yoğunluğu
        self.W = 1.8  # ağırlık (Kg)
        self.g = 9.81  # yer çekimi ivmesi

        # widgets
        self.lift_btn = Button(master, text="Lift", command=self.lift)
        self.lift_btn.pack()

        self.stallspeed_btn = Button(
            master, text="Stall Speed", command=self.stallspeed)
        self.stallspeed_btn.pack()

        self.drag_btn = Button(master, text="Drag", command=self.drag)
        self.drag_btn.pack()

        cl_text_box = Text(master,
                           height=1,
                           width=5)
        cl_text_box.place(x=50, y=50)

        cd_text_box = Text(master,
                           height=1,
                           width=5)
        cd_text_box.place(x=50, y=75)

        v_text_box = Text(master,
                          height=1,
                          width=5)
        v_text_box.place(x=50, y=100)

        s_text_box = Text(master,
                          height=1,
                          width=5)
        s_text_box.place(x=50, y=125)

        ro_text_box = Text(master,
                           height=1,
                           width=5)
        ro_text_box.place(x=50, y=150)

        w_text_box = Text(master,
                          height=1,
                          width=5)
        w_text_box.place(x=50, y=175)

        g_text_box = Text(master,
                          height=1,
                          width=5)
        g_text_box.place(x=50, y=200)

    def lift(self):
        L = (self.CL * self.ro * self.S * (self.V ** 2)) / 2
        print("Lift= ", L, "N =", L / self.g, "Kg")

    def stallspeed(self):
        Vs = ((2 * self.W * self.g) / (self.ro * self.S * self.CL)) ** (1 / 2)
        print("stallspeed= ", Vs, "m/s")

    def drag(self):
        D = (self.ro * (self.V ** 2) * self.CD * self.S) / 2
        print("Drag= ", D, "N")


if __name__ == '__main__':
    root = Tk()
    airtools = Airtools(root)
    root.mainloop()
