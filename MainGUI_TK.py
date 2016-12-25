#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
import re
import time


def init_frame(self):
    # 创建frame容器
    self.frmLL1 = Frame(width=100, height=30)
    self.frmLL2 = Frame(width=100, height=30)
    self.frmLL3 = Frame(width=100, height=30)
    self.frmLL4 = Frame(width=100, height=30)
    
    self.frmLR1 = Frame(width=100, height=30)
    self.frmLR2 = Frame(width=100, height=30)
    self.frmLR3 = Frame(width=100, height=30)
    self.frmLR4 = Frame(width=100, height=30)
    
    self.frmR = Frame(width=100, height=120)
    # 窗口布局
    self.frmLL1.grid(row=0, column=0, columnspan=1, padx=1, pady=1)
    self.frmLL2.grid(row=1, column=0, columnspan=1, padx=1, pady=1)
    self.frmLL3.grid(row=2, column=0, columnspan=1, padx=1, pady=1)
    self.frmLL4.grid(row=3, column=0, columnspan=1, padx=1, pady=1)
    
    self.frmLR1.grid(row=0, column=1, columnspan=1, padx=1, pady=1)
    self.frmLR2.grid(row=1, column=1, columnspan=1, padx=1, pady=1)
    self.frmLR3.grid(row=2, column=1, columnspan=1, padx=1, pady=1)
    self.frmLR4.grid(row=3, column=1, columnspan=1, padx=1, pady=1)
    
    self.frmR.grid(row=0, column=2, rowspan=4, columnspan=2, padx=1, pady=1)
    
    # 固定大小
    self.frmLL1.grid_propagate(0)
    self.frmLL2.grid_propagate(0)
    self.frmLL3.grid_propagate(0)
    self.frmLL4.grid_propagate(0)
    
    self.frmLR1.grid_propagate(0)
    self.frmLR2.grid_propagate(0)
    self.frmLR3.grid_propagate(0)
    self.frmLR4.grid_propagate(0)
    
    self.frmR.grid_propagate(0)
    
def isMsgtxt(filePath):
    '''判断选择的txt文件是否为QQ消息记录文件'''
    if filePath.split(".")[-1] == "txt" :
        return open(filePath,'rU', encoding='utf-8').readline()[0:5] == "﻿消息记录"
    return False

def isDateFormat(getDate):
    '''判断日期格式是否为有效的日期字符串dddd-dd-dd'''
    if re.match("\d{4}-\d{2}-\d{2}", getDate) is None :
        return False
    else :
        try:
            time.strptime(getDate, "%Y-%m-%d")
            return True
        except:
            return False

def openFile(self, filePath):
    infile = open(filePath,'rU', encoding='utf-8')
    readData = infile.read()
    infile.close()
    self.readData = readData

def Sreen(self, readData, startDate, stopDate):
    rdate = r"(\d{4}-\d{2}-\d{2}) .+:\d{2}:\d{2} .*(?![系统消息]+)\w+\("
    rname = r"\d{4}-\d{2}-\d{2} .+:\d{2}:\d{2} (.*(?![系统消息]+)\w+)\("
    listRptDate = re.findall(rdate, readData)
    listRptName = re.findall(rname, readData)
    listDate = sorted(set(listRptDate),key=listRptDate.index)
    listName = sorted(set(listRptName),key=listRptName.index)
    t2pNameList = []
    cntList = []
    if startDate > stopDate :
        tmp = stopDate
        stopDate = startDate
        startDate = tmp    
    if listDate[0] < startDate <listDate[-1] and listDate[0] < stopDate <listDate[-1] and \
     startDate not in listRptDate and stopDate not in listRptDate or \
     startDate < listDate[0] and stopDate < listDate[0] or \
     startDate > listDate[-1] and stopDate > listDate[-1] :
        tkinter.messagebox.showinfo('输入错误', '日期范围为: ' + listDate[0] + ' 至 ' + listDate[-1])
    else :
        if startDate < listRptDate[0] :
            startDate = listRptDate[0]
        if stopDate > listRptDate[-1] :
            stopDate = listRptDate[-1]
        if startDate not in listRptDate :
            for i in range(len(listRptDate)) :
                if startDate < listRptDate[i] :
                    startDate = listRptDate[i]
                    break
        if stopDate not in listRptDate :
            for i in range(len(listRptDate)) :
                if stopDate > listRptDate[-(i+1)] :
                    stopDate = listRptDate[-(i+1)]
                    break
        if stopDate == listDate[-1] :
            for item in listRptName[listRptDate.index(startDate):len(listRptDate)]:
                t2pNameList.append(item)
        else : 
            for item in listRptName[listRptDate.index(startDate):listRptDate.index(listDate[(listDate.index(stopDate)+1)])]:
                t2pNameList.append(item)
        for item in listName :
                listCnt = t2pNameList.count(item)
                s=''
                s=item+'\t ： \t'+str(listCnt)
                cntList.append(s)
    self.cntList = cntList
    
class App:
    def __init__(self,root):

#        #初始化界面
#        frame = Frame(root).pack()
        
            # 创建frame容器
        self.frmLL1 = Frame(width=60, height=30)
        self.frmLL2 = Frame(width=60, height=30)
        self.frmLL3 = Frame(width=60, height=30)
        self.frmLL4 = Frame(width=60, height=30)
        
        self.frmLR1 = Frame(width=30, height=30)
        self.frmLR2 = Frame(width=30, height=30)
        self.frmLR3 = Frame(width=30, height=30)
        self.frmLR4 = Frame(width=30, height=30)
        
        self.frmR = Frame(width=100, height=120)
        # 窗口布局
        self.frmLL1.grid(row=0, column=0, columnspan=1, padx=1, pady=1)
        self.frmLL2.grid(row=1, column=0, columnspan=1, padx=1, pady=1)
        self.frmLL3.grid(row=2, column=0, columnspan=1, padx=1, pady=1)
        self.frmLL4.grid(row=3, column=0, columnspan=1, padx=1, pady=1)
        
        self.frmLR1.grid(row=0, column=1, columnspan=1, padx=1, pady=1)
        self.frmLR2.grid(row=1, column=1, columnspan=1, padx=1, pady=1)
        self.frmLR3.grid(row=2, column=1, columnspan=1, padx=1, pady=1)
        self.frmLR4.grid(row=3, column=1, columnspan=1, padx=1, pady=1)
        
        self.frmR.grid(row=0, column=2, rowspan=4, columnspan=2, padx=1, pady=1)
        
        # 固定大小
        self.frmLL1.grid_propagate(0)
        self.frmLL2.grid_propagate(0)
        self.frmLL3.grid_propagate(0)
        self.frmLL4.grid_propagate(0)
        
        self.frmLR1.grid_propagate(0)
        self.frmLR2.grid_propagate(0)
        self.frmLR3.grid_propagate(0)
        self.frmLR4.grid_propagate(0)
        
        self.frmR.grid_propagate(0)
        
        #btn_chooseFile目录选择框
        btn_chooseFile = Button(self.frmLL4, text="File", command = lambda : self.chooseFile())
        btn_chooseFile.pack()
        #label_fileName目录选择
        Label(self.frmLL1, text = "文件名为:").pack()
        fileName = StringVar()
        label_fileName = Label(self.frmLR1, width = "10", textvariable = fileName)
        self.fileName = fileName
        label_fileName.pack()
        #entry_startDate起始日期
        Label(self.frmLL2, text = "起始时间:").pack()
        startDate = StringVar()
        entry_startDate = Entry(self.frmLR2, width = "10", textvariable = startDate,relief = 'flat')
        self.startDate = startDate
        entry_startDate.pack()
        #entry_stopDate截止日期
        Label(self.frmLL3, text = "截止时间:").pack()
        stopDate = StringVar()
        entry_stopDate = Entry(self.frmLR3, width = "10",textvariable = stopDate,relief = 'flat')
        self.stopDate = stopDate
        entry_stopDate.pack()
        #btn_setData发送数据
        btn_setData = Button(self.frmLR4, text='统计', command = lambda : self.sendData())
        btn_setData.pack()
        #listbox_showData显示消息统计
        listbox_showData = Listbox(self.frmR, width = "15", height = 7, selectmode = EXTENDED)
        listbox_showData.pack()
        self.listbox_showData = listbox_showData
    
    def sendData(self):
        if not isDateFormat(self.startDate.get()) : 
            tkinter.messagebox.showinfo('输入错误', '正确的日期格式:1975-01-01')
            self.startDate.set("")
        elif not isDateFormat(self.stopDate.get()) :
            tkinter.messagebox.showinfo('输入错误', '正确的日期格式:1975-01-01')
            self.stopDate.set("")
        elif self.fileName.get() == "" :
            tkinter.messagebox.showinfo('输入错误', '请选择文件')
        else :
            self.listbox_showData.delete(0,END)
            Sreen(self, self.readData, self.startDate.get(), self.stopDate.get())
            for key, item in enumerate(self.cntList):
                self.listbox_showData.insert(key+1, item )
                
#        date = sorted(set(self.list_date),key=self.list_date.index)
#        name = sorted(set(self.list_name),key=self.list_name.index)
#        Screen(get_date_start,get_date_stop)
#        for key, item in enumerate(list_cnt_name):
#            listbox.insert(key+1, item )
        
    def chooseFile(self):
        while True:
            filePath = askopenfilename() 
            if isMsgtxt(filePath) :
                fileName = filePath.split("/")[-1]
                self.fileName.set(fileName)
                openFile(self, filePath)
                break
            elif filePath == "" : break

if __name__ == '__main__':
    root=Tk()
    root.resizable(False, False)
    root.title("QQ记录统计")
    a = App(root)
    root.mainloop()        
