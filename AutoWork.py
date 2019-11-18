# -*- coding: utf-8 -*
#####################################################################################
# python 3
# author:胡子涵
# 2019/11/17
#####################################################################################

# 导入Tkinter绘制GUI
import tkinter as tk
from FetchData import DataFetcher
import pyperclip
import threading

class AppGUI():
    def __init__(self):
        self.data_fetcher = DataFetcher()
        self.tmp_value = ""
        self.recent_value = ""
        # 创建窗口
        self.root = tk.Tk()
        self.root.resizable(width=False, height=False)
        # 设置窗口始终在屏幕最上面
        self.root.wm_attributes('-topmost', 1)
        # 设置窗口大小
        self.root.geometry("420x500+10+10")

        # 窗口标题
        self.root.title("搜题助手")

        # 用于listbox中列出来的结果
        self.result = tk.StringVar()

        # Label
        self.Label_titile = tk.Label(self.root, text='Nice to meet you.')
        self.Label_titile.pack()

        self.content = tk.Text(self.root)
        self.scroll = tk.Scrollbar(self.root,command=self.content.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)  # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
        self.content.pack(side=tk.LEFT, fill=tk.Y)
        self.content.configure(yscrollcommand=self.scroll.set)

        self.content.bind('<<get>>',self.set_result)

        y = threading.Thread(target=self.getinput)
        y.daemon = True
        y.start()

        self.root.mainloop()


    # 设置显示数据
    def set_result(self, ev = None):
        query = str(pyperclip.paste()).strip()
        if query == "":
            return

        res = self.get_ans(query)
        self.content.delete('1.0', 'end')
        temp_content = ""
        if res[0] or res[1] or res[2]:
            for i in range(0, 3):
                if i == 0 and res[0]:
                    temp_content += "单选题\n=========================================================\n"
                    for index,item in enumerate(res[0]):
                        temp_content += "\n{0}) ------问题------：\n  {1}\n\n答案：{2}\n\n选项：\n".format(index+1,item[0], item[1])
                        if item[2]:
                            temp_content += "(A) {0}\n".format(item[2])
                        if item[3]:
                            temp_content += "(B) {0}\n".format(item[3])
                        if item[4]:
                            temp_content += "(C) {0}\n".format(item[4])
                        if item[5]:
                            temp_content += "(D) {0}\n".format(item[5])
                        if item[6]:
                            temp_content += "(E) {0}\n".format(item[6])
                    temp_content += "  \n\n\n"

                elif i == 1 and res[1]:
                    temp_content += "多选题\n=========================================================\n"
                    for index,item in enumerate(res[1]):
                        temp_content += "\n{0}) ------问题------：\n  {1}\n\n答案：{2}\n\n选项：\n".format(index+1,item[0], item[1])
                        if item[2]:
                            temp_content += "(A) {0}\n".format(item[2])
                        if item[3]:
                            temp_content += "(B) {0}\n".format(item[3])
                        if item[4]:
                            temp_content += "(C) {0}\n".format(item[4])
                        if item[5]:
                            temp_content += "(D) {0}\n".format(item[5])
                        if item[6]:
                            temp_content += "(E) {0}\n".format(item[6])
                    temp_content += "   \n\n\n"
                elif i == 2 and res[2]:
                    temp_content += "判断题\n=========================================================\n"
                    for index, item in enumerate(res[2]):
                        temp_content += "\n{0}) ------问题------：\n  {1}\n\n答案：{2}\n".format(index+1, item[0], item[1])
                    temp_content += "  \n\n\n"
                else:
                    pass
            self.content.insert(tk.END, temp_content)
        else:
            self.content.insert(tk.END, "抱歉，未搜索到结果")


    def get_ans(self, query):
        return self.data_fetcher.search_question(query)


    def getinput(self):
        # 这个线程用以监听命令行输入,并发送event给tkinter
        while True:
            self.tmp_value = pyperclip.paste().strip()  # 读取剪切板复制的内容
            if self.tmp_value != self.recent_value:  # 如果检测到剪切板内容有改动，那么就进入文本的修改
                self.recent_value = self.tmp_value
                self.content.event_generate("<<get>>")



if __name__ == '__main__':
    app = AppGUI()



