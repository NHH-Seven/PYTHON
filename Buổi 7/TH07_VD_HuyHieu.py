#Ví dụ 1
from tkinter import * 
#Tạo một cửa sổ mới 
window = Tk() 
#Thêm tiêu đề cho cửa sổ 
window.title('Welcome to EAUT') 
#Đặt kích thước của cửa sổ 
window.geometry('350x200') 
#Lặp vô tận để hiển thị cửa sổ 
window.mainloop() 

#Ví dụ 2
from tkinter import * 
window = Tk() 
window.title("Welcome to VniTeach app") 
#Thêm label có nội dung Hello, font chữ 
lbl = Label(window, text="Hello", font=("Arial Bold", 50)) 
#Xác định vị trí của label 
lbl.grid(column=0, row=0) 
window.mainloop() 

#Ví dụ 3
window = Tk() 
window.title("Welcome to EAUT") 
window.geometry('350x200') 
lbl = Label(window, text="Hello") 
lbl.grid(column=0, row=0) 
#Thêm một nút nhấn Click Me 
btn = Button(window, text="Click Me", bg="orange", fg="red") 
#Thiết lập vị trí của nút nhấn có màu nền và màu chữ 
btn.grid(column=1, row=0) 
window.mainloop() 

#Ví dụ 4
from tkinter import * 
window = Tk() 
window.title("Welcome to EAUT") 
window.geometry('350x200') 
lbl = Label(window, text="Hello") 
lbl.grid(column=0, row=0) 
#Hàm khi nút được nhấn 
def clicked(): 
lbl.configure(text="Button was clicked !!") 
#Gọi hàm clicked khi nút được nhấn 
btn = Button(window, text="Click Me", command=clicked) 
btn.grid(column=1, row=0) 
window.mainloop() 

#Ví dụ 5
from tkinter import * 
from tkinter import messagebox 
top = Tk() 
top.geometry("100x100") 
def helloCallBack(): 
   msg = messagebox.showinfo( "Hello Python", "Hello World") 
B = Button(top, text = "Hello", command = helloCallBack) 
B.place(x = 50,y = 50) 
top.mainloop() 

#Ví dụ 6
from tkinter import * 
window = Tk() 
window.title("Welcome to EAUT") 
window.geometry('350x200') 
lbl = Label(window, text="Hello") 
lbl.grid(column=0, row=0) 
#Tạo một Textbox 
txt = Entry(window,width=10) 
#Vị trí xuất hiện của Textbox 
txt.grid(column=1, row=0) 
#Đặt vị trí con trỏ tại Textbox 
txt.focus() 
#Hàm xử lý khi nút được nhấn 
def clicked(): 
    res = "Welcome to " + txt.get() 
    lbl.configure(text= res) 
btn = Button(window, text="Click Me", command=clicked) 
btn.grid(column=2, row=0) 
#Để tắt chức năng nhập của Textbox bằng state 
#txt = Entry(window,width=10, state='disabled') 
window.mainloop() 

#Ví dụ 7
from tkinter import * 
from tkinter.ttk import * 
window = Tk() 
window.title("Welcome to EAUT") 
window.geometry('350x200') 
#Tạo hộp chọn Combobox 
combo = Combobox(window) 
#Các giá trị của hộp chọn 
combo['values']= (1, 2, 3, 4, 5, "Text") 
#Thiết lập giá trị được chọn 
combo.current(1) #set the selected item 
combo.grid(column=0, row=0) 
#Lấy giá trị của hộp chọn bằng combo.get() 
window.mainloop() 

#Ví dụ 8
from tkinter import * 
from tkinter.ttk import * 
window = Tk() 
window.title("Welcome EAUT") 
window.geometry('350x200') 
#Thiết lập trạng thái của Checkbox 
chk_state = BooleanVar() 
chk_state.set(True) #set check state 
#Tạo Checkbox có trạng thái đã tích chọn 
chk = Checkbutton(window, text='Choose', var=chk_state) 
chk.grid(column=0, row=0) 
window.mainloop()

# ví dụ 9 
from tkinter import * 
from tkinter.ttk import * 
window = Tk() 
window.title("Welcome to EAUT") 
selected = IntVar() 
rad1 = Radiobutton(window,text='First', value=1, variable=selected) 
rad2 = Radiobutton(window,text='Second', value=2, variable=selected) 
rad3 = Radiobutton(window,text='Third', value=3, variable=selected) 
def clicked(): 
print(selected.get()) 
btn = Button(window, text="Click Me", command=clicked) 
rad1.grid(column=0, row=0) 
rad2.grid(column=1, row=0) 
rad3.grid(column=2, row=0) 
btn.grid(column=3, row=0) 
window.mainloop() 

#Ví dụ 10
from tkinter import * 
from tkinter import scrolledtext 
window = Tk() 
window.title("Welcome to EAUT") 
window.geometry('350x200') 
txt = scrolledtext.ScrolledText(window,width=40,height=10) 
txt.grid(column=0,row=0) 
window.mainloop() 

#Ví dụ 11
# Làm việc với Messagebox 
from tkinter import * 
from tkinter import messagebox 
window = Tk() 
window.title("Welcome to EAUT") 
window.geometry('350x200') 
def clicked(): 
    messagebox.showinfo('Message title', 'Message content') 
btn = Button(window,text='Click here', command=clicked) 
btn.grid(column=0,row=0) 
window.mainloop()

 
#Hộp thoại cảnh báo 
messagebox.showwarning('Message title', 'Message content')  
# Hộp thoại báo lỗi  
#messagebox.showerror('Message title', 'Message content') 

from tkinter import messagebox 
res = messagebox.askquestion('Message title','Message content') 
res = messagebox.askyesno('Message title','Message content') 
res = messagebox.askyesnocancel('Message title','Message content') 
res = messagebox.askokcancel('Message title','Message content') 
res = messagebox.askretrycancel('Message title','Message content') 

#Ví dụ 12
from tkinter import * 
 
window = Tk() 
window.title("Welcome to VniTeach app") 
window.geometry('350x200') 
 
 
#Tạo spinbox có chiều rộng 5, giá trị từ 0 đến 100 
spin = Spinbox(window, from_=0, to=100, width=5) 
spin.grid(column=0,row=0) 
 
window.mainloop()
