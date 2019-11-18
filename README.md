# AutoWork

## 简介

AutoWork是一款用于在合肥工业大学形势与政策在线练习与考试中搜题查题的辅助桌面软件。

该软件使用Python3开发。

## 如何使用

**1、下载**

* 打开仓库主页下的binary目录，可以看到一个AutoWork2.0.zip文件，该文件为该软件的exe程序。点击下载，解压即可。

**2、使用方法**

* zip文件解压后的文件夹内，可以看到AutoWork.exe和data文件夹。

* 双击AutoWork.exe运行程序。

* 程序将始终悬浮在屏幕最上方。

* 在形势与政策的练习或考试网页上，选中并复制想要搜索的题目文本，程序会自动查询题库中的原题，并按照“单选题”、“多选题”和“判断题”分类列出原题与答案。

* 根据查询结果愉快作答即可。



## 项目说明

**说明**

本项目使用Python3开发，采用TKInter框架绘制软件界面，并使用子线程轮询监听剪切板内容变化， 一旦发现剪切板内容变化，便立刻抛出自定义“<<get>>”事件，界面中事先绑定了该“<<get>>”事件的Text文本框组件接收到该事件后，执行回调函数，依据剪切板内容查询是否有类似问题，返回匹配结果，并显示在界面的Text文本框中。



**项目结构**

* AutoWork.py

  程序入口，实现了AppGUI类，用于绘制GUI界面，并启动子线程轮询监听剪切板内容变化事件。

* FetchData.py

  实现了DataFetcher类，用于从excel文件中读取题库，并提供查询接口。

* data/

  该文件夹下的data.xlsx文件即为题库，程序从该文件中读取题库到内存。



## 扩展

本项目中的题库并没有使用最新题库，但根据使用情况来看，题库覆盖率达到90%以上，用于练习或考试没有问题。

若想使用最新的题库，只需将data文件夹下的data.xlsx文件进行替换即可。

注意：替换的文件需要保持文件名一致，且excel表格内的字段名称和顺序也须与原文件保持一致才可使用。

