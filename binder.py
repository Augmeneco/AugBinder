from tkinter import *
import json

root = Tk()
root.geometry("500x400+300+100")
try:
	binds = json.loads(open('binds.json','r',encoding='utf-8').read())
except:
	binds = []

def add(event):
	bind = bind_entry.get()
	binds.append(bind)
	open('binds.json','w',encoding='utf-8').write(json.dumps(binds))
	logbox.insert(END,bind)
def delete(event):
	selection = logbox.curselection()
	binds.remove(logbox.get(logbox.curselection()))
	open('binds.json','w',encoding='utf-8').write(json.dumps(binds))
	logbox.delete(selection[0])
def buffadd(event):
	
	root.clipboard_clear()
	root.clipboard_append(logbox.get(logbox.curselection()))

bind_entry = Entry(width=40)
bind_entry.pack(fill = 'both')
add_button = Button(root, text="Добавить")
add_button.pack(fill = 'both')
del_button = Button(root, text="Удалить")
del_button.pack(fill = 'both')
buff = Button(root, text="Добавить в буфер")
buff.pack(fill = 'both')
add_button.bind('<Button-1>',add)
del_button.bind('<Button-1>',delete)
buff.bind('<Button-1>',buffadd)
logbox = Listbox(root)
logbox.pack(fill='both')

for bind in binds:
	logbox.insert(END,bind)
mainloop()