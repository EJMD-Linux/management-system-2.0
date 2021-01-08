"""作为主函数调用其它文件的类与方法"""

import fun_realize
import fun_improve

sub = fun_realize.Sub()
high = fun_improve.High()

while True:
    print("\n" + "*" * 45 + "\n" + " " * 4 + "------- 欢迎使用学生管理系统 -------"
          + " " * 8 + "\n" + "*" * 45)
    print(" " * 6 + "1.录入学生成绩")
    print(" " * 6 + "2.显示学生成绩")
    print(" " * 6 + "3.查询学生成绩")
    print(" " * 6 + "4.查询学生成绩平均分")
    print(" " * 6 + "5.查询学生成绩最高分")
    print(" " * 6 + "6.查询学生成绩最低分")
    print("*" * 45 + "\n")
    choose = input(" ---- 需要使用哪个功能 ------->      ")

    if choose == "1":
        high.data_input()

    elif choose == "2":
        high.data_show()

    elif choose == "3":
        high.data_select()

    elif choose == "4":
        high.select_average()

    elif choose == "5":
        high.select_highest()
    
    elif choose == "6":
        high.select_lowest()

    goon = input("\n需要继续使用该系统的功能吗 (y/n):      ")
    if goon != "y":
        break

































































































