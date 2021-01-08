"""用于练习与探究 python 中面向对象相关内容"""


class Sub:
    """基类"""
    def __init__(self):
        self.names = []
        self.scores = []
        self.dictionary = {}

    def data_input(self):
        """接收与存储数据"""
        while True:
            name = input("\ninput name:     ")
            if name == 'q':
                print("---------- stop input ----------")
                break
            score = input("input score:    ")
            self.names.append(name)
            self.scores.append(score)

        self.dictionary = self.dictionary.fromkeys(self.names)
        for i, j in zip(self.names, self.scores):
            self.dictionary[i] = j

        with open("data.txt", "w") as f:
            f.write(str(self.dictionary))

    def data_show(self):
        """展示已经获取的数据"""
        for i, j in zip(self.dictionary.keys(), self.dictionary.values()):
            print("\nname:     {}\nscore:    {}".format(i, j))

    def data_select(self):
        """筛选特定数据"""
        way = input("\n选择哪种方式筛选数据 (1.name    2.score)：      ")
        if way == "1":
            name = input("\nenter name:     ")
            print("\n匹配结果：\n")
            for i, j in zip(self.dictionary.keys(), self.dictionary.values()):
                if i == name:
                    print("name:     {}score:    {}\n".format(i, j))

        elif way == "2":
            score = input("\nenter score:     ")
            print("\n匹配结果：\n")
            for i, j in zip(self.dictionary.keys(), self.dictionary.values()):
                if int(j) == int(score):
                    print("name:     {}\nscore:    {}\n".format(i, j))

        else:
            print("\n      !!!!!! 输入错误 !!!!!!\n")

    def select_highest(self):
        """求出特定范围内的最高分"""
        way = input("选择个别学生还是全部学生 (1&2)：     ")
        if way == "1":
            name = input("\nenter name:     ")
            self.names.append(name)

            selected_name = []
            selected_score = []
            selected_dictionary = {}
            for i in self.names:
                for j, k in zip(self.dictionary.keys(), self.dictionary.values()):
                    if i == j:
                        selected_name.append(j)
                        selected_score.append(k)

            selected_dictionary = selected_dictionary.fromkeys(selected_name, 0)
            for i, j in zip(selected_dictionary.keys(), selected_score):
                selected_dictionary[i] = j

            print("\n最高分的是:\n")
            print("name:     {}\nscore:    {}".format(selected_dictionary.keys()[0], selected_dictionary.values()[0]))

        elif way == "2":
            length = len(self.scores)
            for i in range(length-1):
                for j in range(i+1, length):
                    if self.scores[i] < self.scores[j]:
                        self.scores[i], self.scores[j] = self.scores[j], self.scores[i]

            print("\n最高分是：  %d" % self.scores[0])

        else:
            print(" " * 6 + "!!!!! 输入错误 !!!!!")
            return None

    def select_average(self):
        """求出特定范围内的平均分"""
        way = input("\n选择哪种方式筛选数据 (1.name    2.score)：      ")
        if way == "1":
            name = input("\nenter name:     ")
            count = 0
            sum_score = 0
            for i, j in zip(self.dictionary.keys(), self.dictionary.values()):
                if name == i:
                    print("\nname:     {}\nscore:    {}".format(i, j))
                    count += 1
                    sum_score += int(j)

            average = sum_score / count
            print("\nTheir average score is :     %.2f" % average)

        elif way == "2":
            score = input("\nenter score:     ")
            count = 0
            sum_score = 0
            for i, j in zip(self.dictionary.keys(), self.dictionary.values()):
                if int(score) == int(j):
                    print("\nname:     {}\nscore:    {}".format(i, j))
                    count += 1
                    sum_score += int(j)

            average = sum_score / count
            print("\nTheir average score is :     %.2f" % average)

        else:
            print(" " * 6 + "!!!!! 输入错误 !!!!!")
            return None

    def select_lowest(self):
        """求出特定范围内的最低分"""
        way = input("选择个别学生还是全部学生 (1&2)：     ")
        if way == "1":
            name = input("\nenter name:     ")
            self.names.append(name)

            selected_name = []
            selected_score = []
            selected_dictionary = {}
            for i in self.names:
                for j, k in zip(self.dictionary.keys(), self.dictionary.values()):
                    if i == j:
                        selected_name.append(j)
                        selected_score.append(k)

            selected_dictionary = selected_dictionary.fromkeys(selected_name, 0)
            for i, j in zip(selected_dictionary.keys(), selected_score):
                selected_dictionary[i] = j

            print("\n最低分的是:\n")
            print("name:     {}\nscore:    {}".format(selected_dictionary.keys()[0], selected_dictionary.values()[0]))

        elif way == "2":
            length = len(self.scores)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    if self.scores[i] > self.scores[j]:
                        self.scores[i], self.scores[j] = self.scores[j], self.scores[i]

            print("\n最高分是：  %d" % self.scores[0])

        else:
            print(" " * 6 + "!!!!! 输入错误 !!!!!")
            return None













































