from tkintermapview import TkinterMapView
import tkinter as tk
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1280x720")
        self.title('Login')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=8)

        self.create_widgets()

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
        """
        Affiche la frame de creation de course.
        :return: tkinter frame
        """
        count = 1
        frame = ttk.Frame(self)

        title = ttk.Label(frame, text="New course")
        title.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        race_name = ttk.Label(frame, text="Race name :")
        race_name.grid(column=0, row=1, rowspan=2, sticky=tk.W, padx=5, pady=5)

        race_name_input = ttk.Entry(frame, width=30)
        race_name_input.focus()
        race_name_input.grid(column=1, row=1, rowspan=2, sticky=tk.W)

        add_runner = ttk.Label(frame, text="+ add runner")
        add_runner.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

        self.frame_add_runner(count)
        return frame

    def import_data(self):
        frame = ttk.Frame(self)

        return frame

    def start_race(self, race):
        frame = ttk.Frame(self)

        return frame

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


app = Gui()
app.mainloop()
