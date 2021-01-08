"""用于完善已有功能与增添新功能"""

import fun_realize


class High(fun_realize.Sub):
    """完善sub功能"""
    def __init__(self):
        super().__init__()

    def data_input(self):
        """接收输入数据并存储"""
        super().data_input()

    def data_show(self):
        """展示已存储数据"""
        super().data_show()

    def data_select(self):
        """展示筛选数据"""
        super().data_show()

    def select_average(self):
        """展示特定范围的平均分"""
        super().select_average()

    def select_highest(self):
        """选出特定范围的最高分"""
        super().select_highest()

    def select_lowest(self):
        """选出特定范围的最低分"""
        super().select_lowest()
































































































