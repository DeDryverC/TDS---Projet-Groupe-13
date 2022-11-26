import PySimpleGUI as sg
import os.path

## A snippet of the PySimpleGui tutorial
## https://realpython.com/pysimplegui-python/

if __name__ == '__main__':
    first_column = [
        [sg.Text("Race app"),
         sg.In(size=(25 ,1), enable_events=True, key="-FOLDER-"),
         sg.FolderBrowse()
         ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40,20), key="-FILE LIST-"
            )
        ]
    ]
    file_viewer_colum = [
        [sg.Text("Choose a file in the left :")],
        [sg.Text(size=(40,1), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")]
    ]
    layout = [
        [
            sg.Column(first_column),
            sg.VSeparator(),
            sg.Column(file_viewer_colum)
        ]
    ]

    window = sg.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".png", ".gif"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)
            except:
                pass
    window.close()
