# Roll-Caller

这是一个9/9/2024Python课程练习


《随机点名程序》
要求
1.点到的人不能重复点
2.打包成程序


这是我的思路（主要是用列表方法，个人想法仅参考）

- 创建一个完整的学生名单，并将它存储在一个列表中，创建一个空列表来记录已点名的学生

- 从列表中随机抽取一个学生。将该学生从列表中移除储存在另一个列表中，以防下次重复。

- 如果所有学生都被抽到退出循环，程序结束

- 主要使用 `while` 循环持续运行主菜单，直到选择退出。

另外做一个一个简单的终端界面
可以的话在后续版本中添加并使用支持GUI的库

打包程序
这里打包程序使用的是PyInstaller库

