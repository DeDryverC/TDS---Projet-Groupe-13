from tkintermapview import TkinterMapView
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

import os


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

    def get_files_tcx(self):
        files = []
        for file in os.listdir("static/data"):
            if file.endswith('.tcx'):
                files.append(file)
        return files

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
        button_import_data["text"] = "Import data"
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

        listbox_races_value = tk.Variable(value="lol")
        listbox_races = tk.Listbox(root, listvariable=listbox_races_value)
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

    def button_import_data_command(self):
        print("A faire")

    def button_create_race_command(self):
        left_column_home = self.frame_create_race()
        left_column_home.place(x=280, y=0, width=1000, height=720)

    def create_widgets(self):
        # ------TEMP VAR

        races = ('Race 1', 'Race 2')
        var_races = tk.Variable(value=races)

        files = ('file1.tcx', 'file2.tcx', 'file3.tcx')
        var_files = tk.Variable(value=files)
        # ------ LEFT ROW

        name_label = ttk.Label(self, text="Running App")
        name_label.grid(column=0, row=0, rowspan=1, sticky=tk.W, padx=5, pady=5)

        # TODO : Transformer les labels en boutons
        button_create_label = ttk.Label(self, text="Create race")
        button_create_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        # TODO : Transformer les labels en boutons
        button_import_label = ttk.Label(self, text="Import data")
        button_import_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        list_created_race = tk.Listbox(
            self,
            listvariable=var_races,
            height=6,
            selectmode=tk.EXTENDED
        )
        list_created_race.grid(column=0, row=4, rowspan=2, sticky=tk.W, padx=5, pady=5
                               )

        list_file = tk.Listbox(
            self,
            listvariable=var_files,
            height=6,
            selectmode=tk.EXTENDED
        )
        list_file.grid(column=0, row=6, rowspan=2, sticky=tk.W, padx=5, pady=5)

        # TODO : Transformer les labels en boutons
        button_exit = ttk.Label(self, text="Exit")
        button_exit.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)

        # ------ RIGHT ROW

        # TODO: Lier les boutons aux fonctions d'affichage de frame
        create_race = self.frame_create_race()
        create_race.grid(column=1, row=0, rowspan=4, sticky=tk.W)

        # # create map widget
        # map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
        # map_widget.pack(fill="both", expand=True)
        #
        # # google normal tile server
        # map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        #
        # map_widget.set_address("Ottignies Belgium", marker=False)

    def button_exit_command(self):
        exit()

    def frame_add_runner(self, count):
        """

        :param count:
        :return:
        """

        # TODO: Faire un check si meme course (comparer les differences entre les coordonnées, si proche alors c'est bon

        frame = ttk.Frame(self)

        title = ttk.Label(frame, text="Runner {}".format(count))
        title.grid(column=0, row=0, sticky=tk.W)

        # TODO : faire un file input

        return frame

    def frame_create_race(self):
        self.title('Race App - Create race')

        root = tk.Frame(self, background="#393d49")

        label_title_frame = tk.Label(root, justify="left")
        ft = tkFont.Font(family='Helvetica', size=12)
        label_title_frame["bg"] = "#393d49"
        label_title_frame["font"] = ft
        label_title_frame["fg"] = "#ffffff"
        label_title_frame["text"] = "new race"
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

        label_name_race = tk.Label(root)
        label_name_race["bg"] = "#393d49"
        ft = tkFont.Font(family='Helvetica', size=22)
        label_name_race["font"] = ft
        label_name_race["fg"] = "#ffffff"
        label_name_race["justify"] = "center"
        label_name_race["text"] = "Name :"
        label_name_race.place(x=0, y=70, width=225, height=110)

        entry_name_race = tk.Entry(root)
        entry_name_race["bg"] = "#393d49"
        entry_name_race["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica', size=22)
        entry_name_race["font"] = ft
        entry_name_race["fg"] = "#ffffff"
        entry_name_race["justify"] = "left"
        entry_name_race["text"] = "Entry"
        entry_name_race.place(x=200, y=100, width=640, height=50)

        # TODO : Trouver comment faire un affichage stylé.
        GLabel_924 = tk.Label(root)
        ft = tkFont.Font(family='Helvetica', size=10)
        GLabel_924["font"] = ft
        GLabel_924["fg"] = "#333333"
        GLabel_924["justify"] = "center"
        GLabel_924["text"] = "label"
        GLabel_924.place(x=0, y=190, width=840, height=113)

        button_add_runner = tk.Button(root)
        button_add_runner["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Helvetica', size=10)
        button_add_runner["font"] = ft
        button_add_runner["fg"] = "#000000"
        button_add_runner["justify"] = "center"
        button_add_runner["text"] = "+ add a runner"
        button_add_runner.place(x=200, y=330, width=636, height=40)
        button_add_runner["command"] = self.button_add_runner_command

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

    def button_start_race_command(self):
        print("button_start_race_command")

    def button_add_runner_command(self):
        print("button_add_runner_command")

    def button_exit_frame(self):
        left_column_home = self.frame_home()
        left_column_home.place(x=280, y=0, width=1000, height=720)


app = Gui()
app.mainloop()
