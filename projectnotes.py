from tkinter import * 
import calendar

main_window = Tk()
main_window.geometry("500x100")
main_window.title("Student Management System")
main_window.configure(bg="#326273")
Label(main_window, text="Press any button").place(x=20,y=20)
stu_list=[]
#Button functions : Notes
def on_notes():
    side_window = Tk()

    notes = Entry(side_window, width=50, borderwidth=20)
    notes.grid(row=0, column=1)
    def save_notes():
        print(notes.get())
        stu_list.append(notes)
    
    Button(side_window, text = "Save",command = save_notes , padx=40, pady=20).grid(row=1, column=1)
    side_window.mainloop()

#Button Functions : Tasks
def on_task():
    task_window = Tk()

    tasks = Entry(task_window, width=50, borderwidth=20)
    tasks.grid(row=0, column= 1)
    def save_task():
        print(tasks.get())
        stu_list.append(tasks)
    Button(task_window, text = "Save",command = save_task , padx=40, pady=20).grid(row=1, column=1)
    task_window.mainloop()

#Button functions : Impotant_Dates
def on_imp():
    imp_window = Tk()

    test_name = Entry(imp_window, width=50, borderwidth=20)
    test_name.grid(row=0, column= 1)
    dates = Entry(imp_window, width=50, borderwidth=20)
    dates.grid(row=2, column= 1)
    
    def save_imp():
        print(test_name.get())
        print(dates.get())
        stu_list.append(test_name)
        stu_list.append(dates)
    
    Button(imp_window, text = "Save",command = save_imp , padx=40, pady=20).grid(row=1, column=1)
    imp_window.mainloop()

def on_list():
    print(stu_list)

#Button Appearance
notes_button = Button(main_window, text = "Notes", command = on_notes, padx=20, pady=10).place(x=120, y = 20)
task_button = Button(main_window, text = "Tasks", command = on_task, padx=20, pady=10).place(x=200, y = 20)
imp_button = Button(main_window, text = "Tests", command = on_imp, padx=20, pady=10).place(x=278, y = 20)
lst_button = Button(main_window, text = "List", command = on_list, padx=20, pady=10).place(x=355, y = 20)

main_window.mainloop()