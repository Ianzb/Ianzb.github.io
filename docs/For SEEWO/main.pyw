v = "1.4.1-20221025"
from os import *
from time import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Separator
from webbrowser import *

time = strftime("%Y-%m-%d")
# 初始化
tk = Tk()
tk.title("郑博的小程序For Seewo " + v)
x = 200
y = 225
max_x = tk.winfo_screenwidth()
max_y = tk.winfo_screenheight()
now_x = (max_x - x) / 2
now_y = (max_y - y) / 2
tk.geometry("%dx%d+%d+%d" % (x, y, now_x, now_y))

# 设置样式
st = ttk.Style()
st.configure("TButton")


# 功能
def b1():
    popen("pc.pyw")


def b2():
    open("https://ianzb.github.io/")


def b3():
    import os
    sleep(0.25)
    os.popen("taskkill -f -im PPTService.exe")
    sleep(0.25)
    os.popen("C:\Program Files (x86)\Seewo\PPTService\Main\PPTService.exe")


def b4():
    import os
    sleep(0.25)
    os.popen("taskkill -f -im PPTService.exe")


def b5():
    import os, shutil
    list = os.walk(r"D:\\EasiCameraPhoto")
    list2 = []
    for i in list:
        list2.append(i)
    list = list2[0][1]
    for i in list:
        if i != time and os.path.exists(r"D:/EasiCameraPhoto/" + i):
            shutil.rmtree(r"D:/EasiCameraPhoto/" + i)


def b6():
    open("https://tv.cctv.cn/live/cctv13/?spm=C28340.P4hQlpYBT2vN.ExidtyEJcS5K.25")


def b7():
    popen(r"echo Y|PowerShell.exe -NoProfile -Command Clear-RecycleBin")
    popen(r"rd /s %systemdrive%$Recycle.bin")
    popen(
        r"@echo off setlocal enabledelayedexpansion for %%a in (C D E F G H I J K L M N O P Q R S T U V W X Y Z) do ( if exist %%a:\$recycle.bin ( pushd %%a:\$recycle.bin for /f %%b in ('dir /b /a') do (rd /s /q %%b)))")


def repeat_clear(path):
    import os, filecmp, glob
    file_lst = []

    for i in glob.glob(path + '/**/*', recursive=True):
        if os.path.isfile(i):
            file_lst.append(i)

    for x in file_lst:
        for y in file_lst:
            if x != y and os.path.exists(x) and os.path.exists(y):
                if filecmp.cmp(x, y):
                    if len(x) > len(y):
                        os.remove(x)
                    else:
                        os.remove(y)


def b8():
    import os, shutil, stat
    from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
    key = OpenKey(HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    path = QueryValueEx(key, "Desktop")[0] + r"\ "[0:-1]
    list2 = []
    list3 = os.walk(path)
    for i in list3:
        list2.append(i)
    list3 = list2[0][2]
    ppt = []
    doc = []
    xls = []
    img = []
    mp3 = []
    zip = []
    to = r"D:/文件/"
    for i in list3:
        if ".ppt" in i and os.path.exists(path + i):
            ppt.append(i)
        if (".doc" in i or ".txt" in i or ".pdf" in i) and os.path.exists(path + i):
            doc.append(i)
        if ".xls" in i and os.path.exists(path + i):
            xls.append(i)
        if (".png" in i or ".jpg" in i or ".jpeg" in i or ".webp" in i) and os.path.exists(path + i):
            img.append(i)
        if ".mp" in i and os.path.exists(path + i):
            mp3.append(i)
        if (".zip" in i or ".rar" in i or ".7z" in i) and os.path.exists(path + i):
            zip.append(i)
    for i in range(len(ppt)):
        if os.path.exists(to + "PPT/" + ppt[i]):
            j = 1
            while os.path.exists(
                    to + "PPT/" + ppt[i][:ppt[i].rfind(".")] + "(" + str(j) + ")" + ppt[i][ppt[i].rfind("."):]):
                j = j + 1
            ppt[i] = ppt[i] + "(" + str(j) + ")"
    for i in range(len(doc)):
        if os.path.exists(to + "文档/" + doc[i]):
            j = 1
            while os.path.exists(
                    to + "文档/" + doc[i][:doc[i].rfind(".")] + "(" + str(j) + ")" + doc[i][doc[i].rfind("."):]):
                j = j + 1
            doc[i] = doc[i] + "(" + str(j) + ")"
    for i in range(len(xls)):
        if os.path.exists(to + "表格/" + xls[i]):
            j = 1
            while os.path.exists(
                    to + "表格/" + xls[i][:xls[i].rfind(".")] + "(" + str(j) + ")" + xls[i][xls[i].rfind("."):]):
                j = j + 1
            xls[i] = xls[i] + "(" + str(j) + ")"
    for i in range(len(img)):
        if os.path.exists(to + "图片/" + img[i]):
            j = 1
            while os.path.exists(
                    to + "图片/" + img[i][:img[i].rfind(".")] + "(" + str(j) + ")" + img[i][img[i].rfind("."):]):
                j = j + 1
            img[i] = img[i] + "(" + str(j) + ")"
    for i in range(len(mp3)):
        if os.path.exists(to + "音视频/" + mp3[i]):
            j = 1
            while os.path.exists(
                    to + "音视频/" + mp3[i][:mp3[i].rfind(".")] + "(" + str(j) + ")" + mp3[i][mp3[i].rfind("."):]):
                j = j + 1
            mp3[i] = mp3[i] + "(" + str(j) + ")"
    for i in range(len(zip)):
        if os.path.exists(to + "压缩包/" + zip[i]):
            j = 1
            while os.path.exists(
                    to + "压缩包/" + zip[i][:zip[i].rfind(".")] + "(" + str(j) + ")" + zip[i][zip[i].rfind("."):]):
                j = j + 1
            zip[i] = zip[i] + "(" + str(j) + ")"
    if not os.path.exists(to + "PPT/"):
        os.makedirs(to + "PPT/")
    if not os.path.exists(to + "表格/"):
        os.makedirs(to + "表格/")
    if not os.path.exists(to + "文档/"):
        os.makedirs(to + "文档/")
    if not os.path.exists(to + "图片/"):
        os.makedirs(to + "图片/")
    if not os.path.exists(to + "音视频/"):
        os.makedirs(to + "音视频/")
    if not os.path.exists(to + "压缩包/"):
        os.makedirs(to + "压缩包/")
    for i in ppt:
        try:
            os.chmod(path + i, stat.S_IWRITE)
            shutil.move(path + i, to + "PPT/" + i)
        except:
            os.chmod(path + i[:i.rfind("(")], stat.S_IWRITE)
            shutil.move(path + i[:i.rfind("(")],
                        to + "PPT/" + i[:i.rfind(".")] + i[i.rfind("("):] + i[i.rfind("."):i.rfind("(")])
    for i in doc:
        try:
            os.chmod(path + i, stat.S_IWRITE)
            shutil.move(path + i, to + "文档/" + i)
        except:
            os.chmod(path + i[:i.rfind("(")], stat.S_IWRITE)
            shutil.move(path + i[:i.rfind("(")],
                        to + "文档/" + i[:i.rfind(".")] + i[i.rfind("("):] + i[i.rfind("."):i.rfind("(")])
    for i in xls:
        try:
            os.chmod(path + i, stat.S_IWRITE)
            shutil.move(path + i, to + "表格/" + i)
        except:
            os.chmod(path + i[:i.rfind("(")], stat.S_IWRITE)
            shutil.move(path + i[:i.rfind("(")],
                        to + "表格/" + i[:i.rfind(".")] + i[i.rfind("("):] + i[i.rfind("."):i.rfind("(")])
    for i in img:
        try:
            os.chmod(path + i, stat.S_IWRITE)
            shutil.move(path + i, to + "图片/" + i)
        except:
            os.chmod(path + i[:i.rfind("(")], stat.S_IWRITE)
            shutil.move(path + i[:i.rfind("(")],
                        to + "图片/" + i[:i.rfind(".")] + i[i.rfind("("):] + i[i.rfind("."):i.rfind("(")])
    for i in mp3:
        try:
            os.chmod(path + i, stat.S_IWRITE)
            shutil.move(path + i, to + "音视频/" + i)
        except:
            os.chmod(path + i[:i.rfind("(")], stat.S_IWRITE)
            shutil.move(path + i[:i.rfind("(")],
                        to + "音视频/" + i[:i.rfind(".")] + i[i.rfind("("):] + i[i.rfind("."):i.rfind("(")])
    for i in zip:
        try:
            os.chmod(path + i, stat.S_IWRITE)
            shutil.move(path + i, to + "压缩包/" + i)
        except:
            os.chmod(path + i[:i.rfind("(")], stat.S_IWRITE)
            shutil.move(path + i[:i.rfind("(")],
                        to + "压缩包/" + i[:i.rfind(".")] + i[i.rfind("("):] + i[i.rfind("."):i.rfind("(")])
    if not os.path.exists(to + "文件夹/"):
        os.makedirs(to + "文件夹/")
    list3 = list2[0][1]
    fold = []
    for i in list3:
        if i != "软件":
            fold.append(i)
    for i in range(len(fold)):
        if os.path.exists(to + "文件夹/" + fold[i]):
            j = 1
            while os.path.exists(to + "文件夹/" + fold[i] + "(" + str(j) + ")"):
                j = j + 1
            fold[i] = fold[i] + "(" + str(j) + ")"
    for i in fold:
        try:
            shutil.move(path + i, to + "文件夹/" + i)
        except:
            shutil.move(path + i[:i.rfind("(")], to + "文件夹/" + i)
    repeat_clear(to + "PPT/")
    repeat_clear(to + "表格/")
    repeat_clear(to + "图片/")
    repeat_clear(to + "文档/")
    repeat_clear(to + "文件夹/")
    repeat_clear(to + "压缩包/")
    repeat_clear(to + "音视频/")


def b9():
    open("http://10.8.8.35:8443/live/31384275e5e0443fa4364714fcbf85fd")


def b10():
    import sys, os
    if os.path.exists("update.pyw"):
        popen("update.pyw")
        sys.exit()


# txt = ttk.Label(tk, text="文字").place(x=100,y=,width=200,height=30,anchor="center")
# b = ttk.Button(tk, text="按钮", style="TButton", command=b).place(x=,y=,width=100,height=30)
# sep = Separator(tk, orient=HORIZONTAL).place(x=0,y=,width=5000,height=30)
txt = ttk.Label(tk, text="实用工具").place(x=75, y=0, width=150, height=30)
sep = Separator(tk, orient=HORIZONTAL).place(x=0, y=0, width=200, height=2)

b3 = ttk.Button(tk, text="PPT小助手重启", style="TButton", command=b3).place(x=0, y=30, width=100, height=30)
b4 = ttk.Button(tk, text="干掉PPT小助手", style="TButton", command=b4).place(x=100, y=30, width=100, height=30)
b5 = ttk.Button(tk, text="清理扫描图片", style="TButton", command=b5).place(x=0, y=60, width=100, height=30)
b6 = ttk.Button(tk, text="打开CCTV-13", style="TButton", command=b6).place(x=100, y=60, width=100, height=30)
b9 = ttk.Button(tk, text="校园电视台", style="TButton", command=b9).place(x=0, y=90, width=100, height=30)
b7 = ttk.Button(tk, text="清理回收站", style="TButton", command=b7).place(x=100, y=90, width=100, height=30)
b8 = ttk.Button(tk, text="整理桌面文件", style="TButton", command=b8).place(x=0, y=120, width=100, height=30)

sep = Separator(tk, orient=HORIZONTAL).place(x=0, y=155, width=200, height=30)

txt = ttk.Label(tk, text="郑博的小程序For Seewo").place(x=30, y=160, width=150, height=30)

b10 = ttk.Button(tk, text=v, style="TButton", command=b10).place(x=50, y=190, width=100, height=30)

sep = Separator(tk, orient=HORIZONTAL).place(x=0, y=225, width=200, height=30)

txt = ttk.Label(tk, text="夹带私货").place(x=75, y=230, width=150, height=30)

b2 = ttk.Button(tk, text="我的网站", style="TButton", command=b2).place(x=0, y=260, width=100, height=30)
b1 = ttk.Button(tk, text="MC版本爬虫", style="TButton", command=b1).place(x=100, y=260, width=100, height=30)
sep = Separator(tk, orient=HORIZONTAL).place(x=0, y=295, width=200, height=30)
sep = Separator(tk, orient=VERTICAL).place(x=-1, y=0, width=2, height=295)
sep = Separator(tk, orient=VERTICAL).place(x=200, y=0, width=2, height=295)
tk.mainloop()
