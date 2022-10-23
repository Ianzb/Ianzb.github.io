import requests
from os import popen,remove
import bs4
from time import *
import sys


def t():
    return strftime(r"[%T]")


def p(a):
    print(str(t()) + str(a))


def remove1(d, name):
    a = [k for (k, v) in d.items() if v == name]
    for i in a:
        del d[i]


def remove_if_in(d, name):
    a = []
    for i in d.keys():
        if name in i:
            a.append(i)
    for i in a:
        del d[i]


b = []
a = []
v = {}
response = requests.get("https://minecraft.fandom.com/zh/wiki/Template:Version#table")
response.encoding = "UTF-8"
soup = bs4.BeautifulSoup(response.text, "lxml")
data1 = soup.find_all(name="td")
for n in data1:
    a.append(n.text)
for i in range(len(a)):
    if i % 3 != 2:
        b.append(a[i])
for i in range(len(b)):
    if i % 2 == 0:
        v[b[i]] = b[i + 1]
remove1(v, "")
for c in ["内部", "Windows", "macOS", "Linux", "即将到来", "ChromeOS", "PlayStation", "Nintendo", "Xbox", "Steam",
          "demo", "教育版（iOS）", "Minecraft Dungeons（启动器版）"]:
    remove_if_in(v, c)
with open("mc.txt", "w", encoding="utf-8") as file:
    for (k, v) in v.items():
        file.write(k + "版本：" + v + "\n")
popen("mc.txt")
sleep(1)
remove("mc.txt")