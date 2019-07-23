import tkinter as tk

def calcu(e):
    txt=str(e.widget.configure().get("text")[-1])
    if (txt=="CE") or (txt == "C"):
        varEntry1.set("")
    elif txt == "退格":
        varEntry1.set(varEntry1.get()[0:len(varEntry1.get())-1])
    elif txt == "=":
        btnEqual_click()
    elif txt == '+/-':
        var = varEntry1.get()
        if var == "":
            varEntry1.set('-')
        else:
            flag = var[0]
            if flag == "-":
                varEntry1.set(varEntry1.get()[1:])
            else:
                varEntry1.set("")
                varEntry1.set("-"+var)
    else:
        varEntry1.set(varEntry1.get()+txt)
    pass


def btnEqual_click():
    result = eval(varEntry1.get())
    varEntry1.set(result)

# 创建一个窗口
forml = tk.Tk()
# 窗口标题
forml.title("简单计算器")
# 创建一个画布
forml.geometry('380x536+500+100')

# 第一部分 文本框
# 给entry绑定变量
varEntry1= tk.StringVar()
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