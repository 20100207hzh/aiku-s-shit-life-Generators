# -*- coding:utf-8 -*-
import random
import time
'''
本作品是B站up雷姆永远の单推人所制作(也就是本人)在看完我推的孩子第162话睡不着时看到了一个用转盘绝定阿库亚人生的整活视频
于是我就花了一点时间写了这个阿库亚的逆天人生生成器这是是一款用随机数加上一点基于生活常识写出来的限制条件然后使用B站up主
冰_柜_陈_醋的模板编写的随机匹配程序特点是很适合整合且加入了文本数据库功能(其实把终端打印的东西复制一份到txt文件里)
该程序需要以下几种主要参数：
1.txt记录方式(1:每次人生分来记录,2:全部记录在同一个文件中,3:不进行记录)
2.生成速度0-100考虑到很多人电脑性能不太好最快为0.05秒进行一次记录
3.进行几次匹配(生成几次阿库亚的人生)
4.阿库亚的xp和匹配规则(是否为同,是否喜欢年龄大的,是否忽略阿库亚和露比的出生时间差,是否能接受与神木光恋爱,是否能接受骨科)
以上都是一般用户用户在不修改代码的前提下可以改变的参数至于各位专业人士想怎么改我就管不着了(虽然我没写注释但我相信以经过各
类竞赛考验的各位大佬的程序阅读理解能力看懂这份代码一定没问题[doge])
最后叠个甲本人不是专业程序员只是一名普通的信息学竞赛学生和ai爱好者所以本人代码习惯极差既不写注释也瞎写变量名希望各位不要学
习我的坏毛病
'''
cfl = ["mem", "天童寺纱利奈", "星野爱", "星野露比", "黑川赤音", "有马加奈", "齐藤京子", "不知火芙莉露"]
cml = ["五反田导演", "姬川大辉", "神木光", "齐藤一户", "明岛梅尔特", "嫡木制片人", "GOA", "啾啾仔"]
list_s = ["初恋:", "当时最讨厌的人:", "初吻给了:", "女/男朋友:", "分手安慰:", "青梅竹马:", "分手后一见钟情:",
          "想和ta成为朋友:", "好朋友是:", "推的孩子是:", "后来喜欢的人是:", "第一次和谁:", "谁一直暗恋ta:",
          "后来在一起的人是:", "ta放不下谁:", "ta和谁有娃娃亲:", "娃娃亲对象心里爱着谁:", "ta原先要和谁结婚:",
          "谁主持婚礼:", "谁出钱办婚礼:", "婚礼现场谁来抢婚了:", "最终ta和谁结婚了:", "结婚后孩子是谁的:",
          "死后和谁葬在一起:", "谁来撅坟了:"]
g = ""
ag = ""
r = ""
o = ""
ao = ""
w = ""
ga = ""
z = False
sfa = ""
mcode = 0
ft = str(time.time())


def tlng():
    strt = g + ag + r + ga + o + ao + w
    for i in strt:
        if i != 'n' and i != 'y':
            print("请不要输入小写的y和n以外的字符\n您需要重写输入")
            return (True)
    if len(strt) < 7:
        print("请不要输入空字符\n您需要重写输入")
        return (True)
    if ag == 'y' and g == 'n':
        print("如果想不能蓝瞳则绝对蓝铜必须为n\n请重新选择")
        return (True)
    if ao == 'y' and o == 'n':
        print("如果想不喜欢比自己年龄大的则只喜欢比自己年龄大的必须为n\n请重新选择")
        return (True)
    if ga == 'y' and ao == 'y' and r == 'n':
        print("这样与恋爱有关的条目中不会出现露比你确定吗如确定请输入y如不确定请输入n后重新选择")
        p2 = input("请选择y/n:")
        if p2 != "y":
            return (True)
    if ga == 'y' and ag == 'y':
        print("这样与恋爱有关的条目中不会出现露比你确定吗如确定请输入y如不确定请输入n后重新选择")
        p2 = input("请选择y/n:")
        if p2 != "y":
            return (True)
    return (False)


def tspe():
    try:
        spe = float(input("生成速度单位%(0-100)"))
    except ValueError:
        print("请输入0-100间的数字")
        spe = tspe()
    return spe


def tspn():
    try:
        spe = int(input("请输入模拟人生的数量不要超过2147483647\n:"))
    except ValueError:
        print("请输入数字")
        spe = tspe()
    return spe


mo = input(
    "请输入txt记录形式：1.每生单独一个文件 2.全部写入一个文件 3.不进行txt记录\n请输入1或2或3\n如参数错误则使用模式2进行记录\n:")
spp = tspe()
lnum = tspn()
tsp = (spp - spp * 2) / 25 + 4
if tsp <= 0:
    tsp = 0.02
print(
    "欢迎使用星野阿库亚人生生成器下面请写出你觉得阿库亚可能具有的特点\n有请输入y 没有请输入n(都是小写)\n提示：本作默认无视时间线\n温馨提示：黑川赤音和有马加奈都比阿库亚大")
g = input("可能蓝铜(男女皆可)")
ag = input("绝对蓝铜(仅限男)")
r = input("阿库亚和露比一样大(如果选y后面关于年龄的决定不对露比造成影响如果选n则认为露比比阿库亚小)")
o = input("可能喜欢比自己大的(年龄，星野爱不参与,如果选n建议绝对蓝瞳也选n否则结果会很抽象)")
ao = input("只喜欢比自己大的(年龄，星野爱不参与)")
w = input("忘记仇恨(可能会喜欢上神木光)")
ga = input("可以骨科")
while tlng():
    g = input("可能蓝铜(男女皆可)")
    ag = input("绝对蓝铜(仅限男)")
    r = input("阿库亚和露比一样大(如果选y后面关于年龄的决定不对露比造成影响如果选n则认为露比比阿库亚小)")
    o = input("可能喜欢比自己大的(年龄，星野爱不参与,如果选n建议绝对蓝瞳也选n否则结果会很抽象)")
    ao = input("只喜欢比自己大的(年龄，星野爱不参与)")
    w = input("忘记仇恨(可能会喜欢上神木光)")
    ga = input("可以骨科")
if mo == '1':
    mcode = 1
elif mo == '3':
    mcode = 3
else:
    mcode = 2
if mcode == 2:
    frm = "akua's shit life" + str(time.time()) + ".txt"
    file = open(frm, "a+", encoding='utf-8')
for k in range(lnum):
    fs0 = "第" + str(k + 1) + "生"
    print(fs0)
    if mcode == 1:
        fs1 = "akua's shit life" + fs0 + ft + ".txt"
        file = open(fs1, "a+", encoding='utf-8')
    elif mcode == 2:
        fs2 = fs0 + "\n"
        file.write(fs2)
    for d in range(0, len(list_s)):
        if z != False:
            print("蓝瞳是不会有孩子的")
            z = False
        else:
            fl = cfl
            ml = cml
            if d == 0 or d == 2 or d == 3 or d == 5 or d == 6 or d == 10 or d == 11 or d == 13 or d == 14 or d == 15 or d == 17 or d == 21:
                if g == 'n':
                    ml.clear()
                if g == "y" and ag == "y":
                    fl.clear()
                if o == 'y' and ao == 'y' and r == 'y':
                    tfl = ["天童寺纱利奈"]
                    tml = ["明岛梅尔特"]
                    for i in range(0, len(tfl)):
                        if tfl[i] in fl:
                            fl.remove(tfl[i])
                    for i in range(0, len(tml)):
                        if tml[i] in ml:
                            ml.remove(tml[i])
                if o == 'y' and ao == 'y' and r == 'n':
                    tfl = ["天童寺纱利奈", "星野露比", ]
                    tml = ["明岛梅尔特"]
                    for i in range(0, len(tfl)):
                        if tfl[i] in fl:
                            fl.remove(tfl[i])
                    for i in range(0, len(tml)):
                        if tml[i] in ml:
                            ml.remove(tml[i])
                if o == "n":
                    tfl = ["mem", "黑川赤音", "有马加奈", "齐藤京子", "不知火芙莉露"]
                    tml = ["五反田导演", "姬川大辉", "神木光", "齐藤一户", "嫡木制片人", "GOA", "啾啾仔"]
                    for i in range(0, len(tfl)):
                        if tfl[i] in fl:
                            fl.remove(tfl[i])
                    for i in range(0, len(tml)):
                        if tml[i] in ml:
                            ml.remove(tml[i])
                if ga == 'n':
                    if "星野露比" in fl:
                        fl.remove("星野露比")
                if w == 'n':
                    if "神木光" in ml:
                        ml.remove("神木光")
            if d == 22:
                fl.clear()
            tal = fl + ml
            x = random.choice(tal)
            if d == 3 and x in cml:
                suc = "男朋友:" + x
                sfa = "男朋友:"
            elif d == 3 and x in cfl:
                suc = "女朋友:" + x
                sfa = "女朋友:"
            elif d == 21 and x in cml:
                suc = list_s[d] + x
                suc = list_s[d]
                z = True
            elif d == 23:
                if x in cml:
                    cml.remove(x)
                    suc = list_s[d] + x
                    sfa = list_s[d]
                else:
                    cfl.remove(x)
                    suc = list_s[d] + x
                    sfa = list_s[d]
            else:
                suc = list_s[d] + x
                sfa = list_s[d]
            print(sfa, end="")
            time.sleep(tsp)
            print(x, end="")
            time.sleep(tsp / 4)
            print()
            if mcode == 1 or mcode == 2:
                fstxt = suc + "\n"
                file.write(fstxt)
            time.sleep(tsp / 8)
if mcode == 1 or mcode == 2:
    file.close()
