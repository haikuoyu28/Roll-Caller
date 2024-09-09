import random as ran
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("点名器")
root.geometry("400x300") 


students = list(range(1, 77)) 
emstudents = []  # 


result_label = tk.Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=20)


def call_name():
    if students:
        k = ran.randint(0, len(students) - 1)  
        selected_student = students.pop(k)  
        emstudents.append(selected_student)  
        result_label.config(text=f"学号: {selected_student}")
    else:
        result_label.config(text="请重置名单。")


def reset_list():
    students.extend(emstudents)  
    emstudents.clear()  
    result_label.config(text="名单已重置")


def exit_program():
    root.quit()  

# 创建并布局按钮
call_button = tk.Button(root, text="点名", command=call_name, font=('Helvetica', 12))
call_button.pack(pady=10)

reset_button = tk.Button(root, text="重置名单", command=reset_list, font=('Helvetica', 12))
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="退出", command=exit_program, font=('Helvetica', 12))
exit_button.pack(pady=10)


root.mainloop()
