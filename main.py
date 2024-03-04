import helper.fileIO as fn
import PySimpleGUI as sg

label = sg.Text("Enter a to-do item")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window(title="My To-do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            fn.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
