import functions
# Module Library creating instance
import PySimpleGUI as sg # Importing third-party code (Package)
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
add_button2 = sg.Button("Edit")



window = sg.Window('To-Do App', layout=[[label],[input_box,add_button,add_button2]]) #Title of the application
window.read()  # Display the window on the screen
window.close()


