import random as ran


print("""==== 学生点名系统 ====
1. 点名
2. 重置名单
3. 退出
=======================
请选择操作: 
""")#这个是GUI



students = list(range(1,77))#创建一个包含学生编号的名单
emstudents = []#创建一个空列表用来存放已经点过的学生





while students:  # 只要 students 列表中还有学生，循环继续


    choice = int(input())


    if choice == 1:
        j = len(students)
        k = ran.randint(0, j - 1)  # 修改索引范围，防止越界
        print(f"学号: {students[k]}")
        emstudents.append(students[k])
        students.pop(k)


    elif choice == 2:
        students.extend(emstudents)
        emstudents.clear()
        print("名单已重置")


    elif choice == 3:
        break