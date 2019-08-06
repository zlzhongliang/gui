import tkinter as tk
import re
global a
a = '0'

def calcu(e):
    global a
    txt = str(e.widget.configure().get("text")[-1])
    flag = varEntry1.get()+txt
    print(flag)
    if flag == '00':
        varEntry1.set('0')
        return
    elif re.search('^0\d',flag):
        varEntry1.set(flag[1:])
        return
    if (txt=="CE") or (txt == "C"):
        varEntry1.set("0")
        a = '0'
        return
    elif txt == "退格":
        if len(varEntry1.get()) <= 1:
            varEntry1.set('0')
            return
        else:
            varEntry1.set(varEntry1.get()[:(len(varEntry1.get())-1)])
            return
    elif txt == '+/-':
        var = varEntry1.get()
        if var == '0':
            varEntry1.set('-')
            return
        elif var == '-':
            varEntry1.set('0')
            return
        elif var[0] == "-":
            varEntry1.set(varEntry1.get()[1:])
            return
        else:
            varEntry1.set("")
            varEntry1.set("-"+var)
            return
    elif txt == "=":
        if a == '0':
            a = varEntry1.get()
            return
        else:
            btnEqual_click()
    elif txt == "+":
        a = a + '+'
        btnEqual_click()
    elif txt == "-":
        a = a + '-'
        btnEqual_click()
    elif txt == "*":
        a = a + '*'
        btnEqual_click()
    elif txt == "/":
        a = a + '/'
        btnEqual_click()

    else:
        varEntry1.set(varEntry1.get()+txt)





def btnEqual_click():
    global a
    b = a+varEntry1.get()
    result = eval(b)
    a = result
    varEntry1.set('0')

# 创建一个窗口
forml = tk.Tk()
# 窗口标题
forml.title("简单计算器")
# 创建一个画布
forml.geometry('380x536+500+100')

# 第一部分 文本框
# 给entry绑定变量
varEntry1= tk.StringVar()
varEntry1.set('0')
entry1 = tk.Label(forml,fg="black",bg="white",font=("Arial",25),textvariable=varEntry1)
# 使用grid作为外部布局，第一部分在第一行第一列
entry1.grid(row=0,column=0,sticky=tk.EW,ipady=20)  # sticky 表单填充

# 第二部分 按钮
# 创建frame控件,使用frame作为内部按钮布局
f1 = tk.Frame(forml)
# 将frame控件放在grid的第二行
f1.grid(row=1,column=0)
# 创建按钮列表
fn = ["CE","C","退格","/",7,8,9,"*",4,5,6,"-",1,2,3,"+","+/-",0,".","="]
a = 0
for v in fn:
    btn1 = tk.Button(f1, text=v,font=('Arial',22), width=5,height=2)
    btn1.bind("<Button-1>",calcu)
    btn1.grid(row=a//4,column=a%4)
    a+=1


# 运行
forml.mainloop()