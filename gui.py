from tkintermapview import TkinterMapView
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.font as tkFont
import xml.etree.ElementTree as ET

import time
import os
from runner import Runner
import matplotlib

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class Gui(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("1280x720")
        self.title('Race App - Home')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=8)

        right_column = self.frame_menu_right()
        right_column.place(x=0, y=0, width=280, height=720)

        left_column_home = self.frame_home()
        left_column_home.place(x=280, y=0, width=1000, height=720)

        self._filelist = self.get_files_tcx()
        self.__len_runner = 0
        self.__runner_list = []
        self._map = TkinterMapView()
        self.__speed = 0.01
        self.marker1 = 0
        self.marker2 =None

    def get_files_tcx(self):
        files = []
        for file in os.listdir("static/data"):
            if file.endswith('.tcx'):
                files.append(file)
        return files

    # --------------- FRAMES
    def frame_menu_right(self):

        root = tk.Frame(self, background="#393d49")

        label_app_title = tk.Label(root,
                                   bg="#393d49",
                                   font=tkFont.Font(family="Helvetica", size=24),
                                   foreground="#ffffff",
                                   justify="center",
                                   text="Race App",
                                   relief="ridge")
        label_app_title.place(x=0, y=0, width=280, height=90)

        button_create_race = tk.Button(root)
        button_create_race["bg"] = "#1e90ff"
        ft = tkFont.Font(family="Helvetica", size=12)
        button_create_race["font"] = ft
        button_create_race["fg"] = "#000000"
        button_create_race["justify"] = "center"
        button_create_race["text"] = "Create race"
        button_create_race.place(x=0, y=90, width=280, height=40)
        button_create_race["command"] = self.button_create_race_command

        button_import_data = tk.Button(root)
        button_import_data["bg"] = "#1e90ff"
        ft = tkFont.Font(family="Helvetica", size=12)
        button_import_data["font"] = ft
        button_import_data["fg"] = "#000000"
        button_import_data["justify"] = "center"
        button_import_data["text"] = "Import file"
        button_import_data.place(x=0, y=130, width=280, height=40)
        button_import_data["command"] = self.button_import_data_command

        label_listbox_races = tk.Label(root)
        label_listbox_races["bg"] = "#393d49"
        ft = tkFont.Font(family="Helvetica", size=12)
        label_listbox_races["font"] = ft
        label_listbox_races["fg"] = "#ffffff"
        label_listbox_races["justify"] = "center"
        label_listbox_races["text"] = "Created race :"
        label_listbox_races.place(x=0, y=170, width=280, height=40)

        global listbox_races
        listbox_races = tk.Listbox(root)
        listbox_races["borderwidth"] = "1px"
        ft = tkFont.Font(family="Helvetica", size=10)
        listbox_races["font"] = ft
        listbox_races["fg"] = "#333333"
        listbox_races["justify"] = "center"
        listbox_races.place(x=0, y=210, width=280, height=200)

        label_listbox_files = tk.Label(root)
        label_listbox_files["bg"] = "#393d49"
        ft = tkFont.Font(family="Helvetica", size=12)
        label_listbox_files["font"] = ft
        label_listbox_files["fg"] = "#ffffff"
        label_listbox_files["justify"] = "center"
        label_listbox_files["text"] = "imported files:"
        label_listbox_files.place(x=0, y=410, width=280, height=40)

        global listbox_files
        listbox_files_value = tk.Variable(value=self.get_files_tcx())
        listbox_files = tk.Listbox(root, listvariable=listbox_files_value)
        listbox_files["borderwidth"] = "1px"
        ft = tkFont.Font(family="Helvetica", size=10)
        listbox_files["font"] = ft
        listbox_files["fg"] = "#333333"
        listbox_files["justify"] = "center"
        listbox_files.place(x=0, y=450, width=280, height=200)

        button_exit = tk.Button(root)
        button_exit["bg"] = "#f26f3f"
        ft = tkFont.Font(family="Helvetica", size=10)
        button_exit["font"] = ft
        button_exit["fg"] = "#000000"
        button_exit["justify"] = "center"
        button_exit["text"] = "Exit"
        button_exit.place(x=0, y=650, width=280, height=70)
        button_exit["command"] = self.button_exit_command

        return root

    def frame_home(self):
        root = tk.Frame(self, background="#393d49")

        label_title_frame = tk.Label(root)
        ft = tkFont.Font(family='Helvetica', size=34)
        label_title_frame["bg"] = "#393d49"
        label_title_frame["font"] = ft
        label_title_frame["fg"] = "#ffffff"
        label_title_frame["justify"] = "center"
        label_title_frame["text"] = "Welcome in the race app !"
        label_title_frame.place(x=0, y=0, width=1000, height=155)

        label_description = tk.Label(root)
        ft = tkFont.Font(family='Helvetica', size=12)
        label_description["bg"] = "#393d49"
        label_description["font"] = ft
        label_description["fg"] = "#ffffff"
        label_description["justify"] = "center"
        label_description[
            "text"] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis id efficitur justo. " \
                      "Sed eget fermentum est.\n Aliquam nec sem eget augue eleifend sagittis. Curabitur interdum " \
                      "malesuada est, in aliquet ligula ullamcorper ut.\n Mauris vel ipsum et nunc tristique eleifend " \
                      "in nec sapien. Nullam mollis massa sem, sed semper dui euismod sed.\n Etiam ac augue faucibus, " \
                      "sagittis neque ac, rutrum tellus.  Duis ex odio, lobortis elementum tellus in, lobortis " \
                      "suscipit ipsum. Pellentesque id laoreet felis.\n Suspendisse in gravida nibh, vel laoreet " \
                      "quam. Nulla porta orci quis euismod varius. Cras rhoncus, erat eget mollis facilisis, " \
                      "tellus diam iaculis sapien, nec viverra odio dui vitae urna.\n Nunc est dui, tempor eu sem vel," \
                      "gravida convallis diam. Praesent elementum porttitor ornare.\n Sed finibus semper sagittis. " \
                      "In eget pharetra tellus. Ut accumsan varius ipsum a vulputate.\n Morbi non sagittis eros, " \
                      "ut dapibus est. Donec lorem felis, sollicitudin non bibendum sed, egestas eget tortor."
        label_description.place(x=90, y=155, width=820, height=317)

        button_create_race = tk.Button(root)
        button_create_race["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Helvetica', size=22)
        button_create_race["font"] = ft
        button_create_race["fg"] = "#000000"
        button_create_race["justify"] = "center"
        button_create_race["text"] = "Create race"
        button_create_race.place(x=190, y=430, width=620, height=55)
        button_create_race["command"] = self.button_create_race_command

        button_import_file = tk.Button(root)
        button_import_file["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Helvetica', size=22)
        button_import_file["font"] = ft
        button_import_file["fg"] = "#000000"
        button_import_file["justify"] = "center"
        button_import_file["text"] = "Import file"
        button_import_file.place(x=190, y=510, width=620, height=55)
        button_import_file["command"] = self.button_import_data_command

        return root

    def frame_race(self):
        root = tk.Frame(self, background="#393d49")



        frame_data_1 = tk.Label(root)
        frame_data_1["bg"] = "#0000ff"
        ft = tkFont.Font(family='Times', size=10)
        frame_data_1["font"] = ft
        frame_data_1["fg"] = "#333333"
        frame_data_1["justify"] = "center"
        frame_data_1["text"] = "label"
        frame_data_1.place(x=350, y=550, width=300, height=150)

        label_actual_heartrate = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        label_actual_heartrate["bg"] = "#ffffff"
        label_actual_heartrate["font"] = ft
        label_actual_heartrate["fg"] = "#000000"
        label_actual_heartrate["justify"] = "center"
        label_actual_heartrate["text"] = "Heartrate"
        label_actual_heartrate.place(x=455, y=530, width=90, height=25)

        frame_data_2 = tk.Label(root)
        frame_data_2["bg"] = "#0000ff"
        ft = tkFont.Font(family='Times', size=10)
        frame_data_2["font"] = ft
        frame_data_2["fg"] = "#333333"
        frame_data_2["justify"] = "center"
        frame_data_2["text"] = "label"
        frame_data_2.place(x=680, y=550, width=300, height=150)

        label_actual_elevation = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        label_actual_elevation["bg"] = "#ffffff"
        label_actual_elevation["font"] = ft
        label_actual_elevation["fg"] = "#000000"
        label_actual_elevation["justify"] = "center"
        label_actual_elevation["text"] = "Heartrate"
        label_actual_elevation.place(x=125, y=530, width=90, height=25)

        frame_data_3 = tk.Label(root)
        frame_data_3["bg"] = "#002bff"
        ft = tkFont.Font(family='Times', size=10)
        frame_data_3["font"] = ft
        frame_data_3["fg"] = "#000000"
        frame_data_3["justify"] = "center"
        frame_data_3["text"] = "label"
        frame_data_3.place(x=20, y=550, width=300, height=150)

        label_real_speed = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        label_real_speed["bg"] = "#ffffff"
        label_real_speed["font"] = ft
        label_real_speed["fg"] = "#000000"
        label_real_speed["justify"] = "center"
        label_real_speed["text"] = "Speed (km/h)"
        label_real_speed.place(x=785, y=530, width=90, height=25)

        button_close = tk.Button(root)
        button_close["bg"] = "#bc0000"
        ft = tkFont.Font(family='Times', size=10)
        button_close["font"] = ft
        button_close["fg"] = "#000000"
        button_close["justify"] = "center"
        button_close["text"] = "X"
        button_close.place(x=975, y=0, width=25, height=25)
        button_close["command"] = self.button_exit_frame

        button_speed_x_2 = tk.Button(root)
        button_speed_x_2["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_speed_x_2["font"] = ft
        button_speed_x_2["fg"] = "#000000"
        button_speed_x_2["justify"] = "center"
        button_speed_x_2["text"] = "x2"
        button_speed_x_2.place(x=810, y=80, width=70, height=25)
        button_speed_x_2["command"] = self.button_speed_x_2_command

        button_start_race = tk.Button(root)
        button_start_race["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_start_race["font"] = ft
        button_start_race["fg"] = "#000000"
        button_start_race["justify"] = "center"
        button_start_race["text"] = "start"
        button_start_race.place(x=650, y=30, width=70, height=25)
        button_start_race["command"] = self.button_start_command

        button_pause_race = tk.Button(root)
        button_pause_race["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_pause_race["font"] = ft
        button_pause_race["fg"] = "#000000"
        button_pause_race["justify"] = "center"
        button_pause_race["text"] = "pause"
        button_pause_race.place(x=730, y=30, width=70, height=25)
        button_pause_race["command"] = self.button_pause_race_command

        label_actual_speed = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        label_actual_speed["bg"] = "#393d49"
        label_actual_speed["font"] = ft
        label_actual_speed["fg"] = "#ffffff"
        label_actual_speed["justify"] = "center"
        label_actual_speed["text"] = "Actual speed :"
        label_actual_speed.place(x=810, y=30, width=88, height=25)

        dynamic_actual_speed = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        dynamic_actual_speed["bg"] = "#393d49"
        dynamic_actual_speed["font"] = ft
        dynamic_actual_speed["fg"] = "#ffffff"
        dynamic_actual_speed["justify"] = "center"
        dynamic_actual_speed["text"] = self.__speed
        dynamic_actual_speed.place(x=900, y=30, width=70, height=25)

        button_speed_x_0_25 = tk.Button(root)
        button_speed_x_0_25["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_speed_x_0_25["font"] = ft
        button_speed_x_0_25["fg"] = "#000000"
        button_speed_x_0_25["justify"] = "center"
        button_speed_x_0_25["text"] = "x0.25"
        button_speed_x_0_25.place(x=650, y=80, width=70, height=25)
        button_speed_x_0_25["command"] = self.button_speed_x_0_25_command

        button_speed_x_0_5 = tk.Button(root)
        button_speed_x_0_5["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_speed_x_0_5["font"] = ft
        button_speed_x_0_5["fg"] = "#000000"
        button_speed_x_0_5["justify"] = "center"
        button_speed_x_0_5["text"] = "x0.5"
        button_speed_x_0_5.place(x=730, y=80, width=70, height=25)
        button_speed_x_0_5["command"] = self.button_speed_x_0_5_command

        button_speed_x_4 = tk.Button(root)
        button_speed_x_4["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        button_speed_x_4["font"] = ft
        button_speed_x_4["fg"] = "#000000"
        button_speed_x_4["justify"] = "center"
        button_speed_x_4["text"] = "x4"
        button_speed_x_4.place(x=890, y=80, width=70, height=25)
        button_speed_x_4["command"] = self.button_speed_x_4_command

        return root

    def frame_create_race(self):
        self.title('Race App - Create race')

        root = tk.Frame(self, background="#393d49")

        label_title_frame = tk.Label(root, justify="left")
        ft = tkFont.Font(family='Helvetica', size=25)
        label_title_frame["bg"] = "#393d49"
        label_title_frame["font"] = ft
        label_title_frame["fg"] = "#ffffff"
        label_title_frame["text"] = "New race"
        label_title_frame.place(x=30, y=0, width=970, height=30)

        button_exit_frame = tk.Button(root)
        button_exit_frame["bg"] = "#ff0000"
        ft = tkFont.Font(family='Helvetica', size=24)
        button_exit_frame["font"] = ft
        button_exit_frame["fg"] = "#000000"
        button_exit_frame["justify"] = "center"
        button_exit_frame["text"] = "x"
        button_exit_frame.place(x=970, y=0, width=30, height=30)
        button_exit_frame["command"] = self.button_exit_frame

        label_number_race = tk.Label(root)
        label_number_race["bg"] = "#393d49"
        ft = tkFont.Font(family='Helvetica', size=22)
        label_number_race["font"] = ft
        label_number_race["fg"] = "#ffffff"
        label_number_race["justify"] = "center"
        label_number_race["text"] = "Name :"
        label_number_race.place(x=0, y=70, width=225, height=110)

        global entry_name_race
        entry_name_race = tk.Entry(root)
        entry_name_race["bg"] = "#393d49"
        entry_name_race["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica', size=22)
        entry_name_race["font"] = ft
        entry_name_race["fg"] = "#000000"
        entry_name_race["justify"] = "left"
        entry_name_race.insert(0, "Enter the name of your race")
        entry_name_race.place(x=200, y=100, width=640, height=50)

        button_add_runner = tk.Button(root)
        button_add_runner["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Helvetica', size=10)
        button_add_runner["font"] = ft
        button_add_runner["fg"] = "#000000"
        button_add_runner["justify"] = "center"
        button_add_runner["text"] = "+ add a runner"
        button_add_runner.place(x=200, y=250, width=636, height=40)
        button_add_runner["command"] = lambda: self.button_add_runner_command(button_add_runner)

        button_start_race = tk.Button(root)
        button_start_race["bg"] = "#90ee90"
        ft = tkFont.Font(family='Helvetica', size=22)
        button_start_race["font"] = ft
        button_start_race["fg"] = "#000000"
        button_start_race["justify"] = "center"
        button_start_race["text"] = "Start race"
        button_start_race.place(x=100, y=600, width=800, height=55)
        button_start_race["command"] = self.button_start_race_command

        return root

    def frame_new_runner(self, name, number):

        root = tk.Frame(self, background="#393d49")
        label_number = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        label_number["bg"] = "#393d49"
        label_number["font"] = ft
        label_number["fg"] = "#ffffff"
        label_number["justify"] = "center"
        label_number["text"] = "name:"
        label_number.place(x=100, y=0, width=38, height=30)

        dynamic_number = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        dynamic_number["bg"] = "#393d49"
        dynamic_number["font"] = ft
        dynamic_number["fg"] = "#ffffff"
        dynamic_number["justify"] = "center"
        dynamic_number["text"] = number
        dynamic_number.place(x=60, y=0, width=30, height=30)

        label_name = tk.Label(root)
        label_name["bg"] = "#393d49"
        ft = tkFont.Font(family='Times', size=10)
        label_name["font"] = ft
        label_name["fg"] = "#ffffff"
        label_name["justify"] = "center"
        label_name["text"] = "number:"
        label_name.place(x=0, y=0, width=65, height=30)

        dynamic_name = tk.Label(root)
        dynamic_name["bg"] = "#393d49"
        ft = tkFont.Font(family='Times', size=10)
        dynamic_name["font"] = ft
        dynamic_name["fg"] = "#ffffff"
        dynamic_name["justify"] = "center"
        dynamic_name["text"] = name
        dynamic_name.place(x=140, y=0, width=99, height=30)

        return root

    # --------------- BUTTONS

    def button_speed_x_2_command(self):
        self.__speed = self.__speed / 2

        update_actual_speed = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        update_actual_speed["bg"] = "#393d49"
        update_actual_speed["font"] = ft
        update_actual_speed["fg"] = "#ffffff"
        update_actual_speed["justify"] = "center"
        update_actual_speed["text"] = str(self.__speed) + " s"
        update_actual_speed.place(x=1180, y=30, width=70, height=25)

    def button_speed_x_4_command(self):
        self.__speed = self.__speed / 4

        update_actual_speed = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        update_actual_speed["bg"] = "#393d49"
        update_actual_speed["font"] = ft
        update_actual_speed["fg"] = "#ffffff"
        update_actual_speed["justify"] = "center"
        update_actual_speed["text"] = str(self.__speed) + " s"
        update_actual_speed.place(x=1180, y=30, width=70, height=25)

    def button_speed_x_0_25_command(self):
        self.__speed = self.__speed * 4

        update_actual_speed = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        update_actual_speed["bg"] = "#393d49"
        update_actual_speed["font"] = ft
        update_actual_speed["fg"] = "#ffffff"
        update_actual_speed["justify"] = "center"
        update_actual_speed["text"] = str(self.__speed) + " s"
        update_actual_speed.place(x=1180, y=30, width=70, height=25)

    def button_speed_x_0_5_command(self):
        self.__speed = self.__speed * 2

        update_actual_speed = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        update_actual_speed["bg"] = "#393d49"
        update_actual_speed["font"] = ft
        update_actual_speed["fg"] = "#ffffff"
        update_actual_speed["justify"] = "center"
        update_actual_speed["text"] = str(self.__speed) + " s"
        update_actual_speed.place(x=1180, y=30, width=70, height=25)

    def button_pause_race_command(self):
        pass

    def button_start_command(self):
        runners = self.__runners
        max_len = 0
        runners_tracks = []

        track = self.__runners[0].get_track
        elevation = self.__runners[0].get_elevation
        heartrate = self.__runners[0].get_heartrate
        speed = self.__runners[0].get_speed

        list_elevation = [0 for i in range(101)]
        list_heartrate = [0 for i in range(101)]
        list_speed = [0 for i in range(101)]

        count = 0
        for i in track:
            if not self.marker2:
                self.marker2 = self._map.set_marker(i[0], i[1])
            else:
                self.marker2 = self.marker1
            self.marker1 = self._map.set_marker(i[0], i[1])

            if elevation[count] is not None:
                list_elevation.insert(len(list_elevation), int(elevation[count]))
                list_elevation.pop(0)

            if heartrate[count] is not None:
                list_heartrate.insert(len(list_heartrate), int(heartrate[count]))
                list_heartrate.pop(0)

            if speed[count] is not None:
                list_speed.insert(len(list_speed), int(speed[count]))
                list_speed.pop(0)

            self.show_elevation(list_elevation)
            self.show_hr(list_heartrate)
            self.show_speed(list_speed)
            self.update()
            time.sleep(self.__speed)
            self.marker2.delete()
            self.update()
            count += 1

    def show_elevation(self, y):
        fig = Figure(figsize=(10, 8), dpi=100)
        plot1 = fig.add_subplot(111)
        plot1.plot(y)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=300, y=550, width=300, height=150)

    def show_hr(self, y):
        fig = Figure(figsize=(10, 8), dpi=100)
        plot1 = fig.add_subplot(111)
        plot1.plot(y)
        canvas2 = FigureCanvasTkAgg(fig, self)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=630, y=550, width=300, height=150)

    def show_speed(self, y):
        fig = Figure(figsize=(10, 8), dpi=100)
        plot1 = fig.add_subplot(111)
        plot1.plot(y)
        canvas2 = FigureCanvasTkAgg(fig, self)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=960, y=550, width=300, height=150)

    def button_import_data_command(self):

        file_name = []
        filetypes = (("Tcx files", "*.tcx"), ("All files", "*.*"))
        file_name += filedialog.askopenfilename(title="Selectionnez le fichier", filetypes=filetypes, multiple=True)
        listbox_files.delete(0, listbox_files.size())
        for i in file_name:
            valeur = (i.find("data/"))
            importedfiles_list = i[valeur + 5:len(i)]
            listbox_files.insert(0, importedfiles_list)

    def button_create_race_command(self):
        left_column_home = self.frame_create_race()
        left_column_home.place(x=280, y=0, width=1000, height=720)

    def button_exit_command(self):
        exit()

    def button_start_race_command(self):

        left_column_home = self.frame_race()
        left_column_home.place(x=280, y=0, width=1000, height=720)

        self._map = TkinterMapView(self, width=600, height=500)
        self._map.place(x=300, y=20, width=600, height=500)
        Runners = []
        color = ["#3E69CB", "#3ecba5", "#afd622", "#b90ccc"]
        for attendee in self.__runner_list:
            runner_obj = Runner(file=attendee[0], name=attendee[1])
            track = runner_obj.get_track
            path_1 = self._map.set_path(track, color=color[len(Runners)])
            Runners.append(runner_obj)

        self.__runners = Runners
        track = Runners[0].get_track
        self._map.set_position(track[0][0], track[0][1])

    def button_add_runner_command(self, button):
        button.destroy()
        length = self.__len_runner
        filetypes = (("Tcx files", "*.tcx"), ("All files", "*.*"))
        file_name = filedialog.askopenfilename(title="Selectionnez le fichier", filetypes=filetypes, multiple=False)

        if file_name not in self.__runner_list:
            valeur = (file_name.find("data/"))
            name = file_name[valeur + 5:len(file_name) - 4]
            button = self.frame_new_runner(name, length + 1)
            button.place(x=380, y=210 + (30 * length), width=840, height=30)
            self.__len_runner += 1
            self.__runner_list.append((file_name, name))
        else:
            messagebox.showwarning("Attention !", message="Vous ne pouvez pas ajouter 2 fois le meme coureur")

        button_readd_runner = tk.Button(self)
        button_readd_runner["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Helvetica', size=10)
        button_readd_runner["font"] = ft
        button_readd_runner["fg"] = "#000000"
        button_readd_runner["justify"] = "center"
        button_readd_runner["text"] = "+ add a runner"
        button_readd_runner.place(x=480, y=330 + (30 * length), width=636, height=40)
        button_readd_runner["command"] = lambda: self.button_add_runner_command(button_readd_runner)

    def button_exit_frame(self):
        self.__len_runner = 0
        self.__runner_list = []
        left_column_home = self.frame_home()
        left_column_home.place(x=280, y=0, width=1000, height=720)


app = Gui()
app.mainloop()
