# -*- coding: utf-8 -*
#####################################################################################
# python 3
# author:胡子涵
# 2019/11/17
#####################################################################################

import xlrd

class DataFetcher(object):

    sheets = None

    def __init__(self):
        self.file = './data/data.xlsx'
        self.questions = self.load_data()

    # 加载execl表格数据到内存
    def load_data(self):
        wb = xlrd.open_workbook(filename=self.file)  # 打开文件

        sheet1 = wb.sheet_by_name('单选题')
        sheet2 = wb.sheet_by_name('多选题')
        sheet3 = wb.sheet_by_name('判断题')
        self.sheets = [sheet1, sheet2, sheet3]

        questions = [[],[],[]]
        for i in range(0, len(self.sheets)):
            if i == 0:
                questions[0] = self.sheets[0].col_values(0)
            elif i == 1:
                questions[1] = self.sheets[1].col_values(0)
            elif i == 2:
                questions[2] = self.sheets[2].col_values(0)
            else:
                pass

        return questions

    # 根据问题查找原问题和相应的答案
    def search_question(self, question = ""):
        result = [[],[],[]]
        question.strip()

        for i in range(0,3):
            length = len(self.questions[i])
            for j in range(0,length):
                if question in self.questions[i][j]:
                    result[i].append(tuple(self.sheets[i].row_values(j)))
        return result