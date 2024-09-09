import random as ran
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("点名器")
root.geometry("400x300")  # 设置窗口大小

# 初始化学生列表和点名记录列表
students = list(range(1, 77))  # 包含学生编号的列表
emstudents = []  # 存放已经点过名的学生

# 定义一个显示结果的标签
result_label = tk.Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=20)

# 定义“点名”按钮的事件处理函数
def call_name():
    if students:
        k = ran.randint(0, len(students) - 1)  # 随机选择学生
        selected_student = students.pop(k)  # 从学生列表中移除
        emstudents.append(selected_student)  # 存入已点名单
        result_label.config(text=f"已点名的学生编号是: {selected_student}")
    else:
        result_label.config(text="没有学生可以点名，请重置名单。")

# 定义“重置名单”按钮的事件处理函数
def reset_list():
    students.extend(emstudents)  # 把已点名的学生重新加入学生列表
    emstudents.clear()  # 清空已点名单
    result_label.config(text="名单已重置，所有学生重新可点名。")

# 定义“退出”按钮的事件处理函数
def exit_program():
    root.quit()  # 退出程序

# 创建并布局按钮
call_button = tk.Button(root, text="点名", command=call_name, font=('Helvetica', 12))
call_button.pack(pady=10)

reset_button = tk.Button(root, text="重置名单", command=reset_list, font=('Helvetica', 12))
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="退出", command=exit_program, font=('Helvetica', 12))
exit_button.pack(pady=10)

# 启动主循环
root.mainloop()
