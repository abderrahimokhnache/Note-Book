from tkinter import *

from tkinter import ttk 

from note_class import DBConnect

from tkinter.scrolledtext import ScrolledText

from tkinter.messagebox import showinfo ,showerror

dbconnect = DBConnect()

class List:
	
	def __init__(self):
	
		self._root = Tk()
	
		self._dbconnect = DBConnect()
	
		self._root.title("Regestired Note")
	
		# self._root.iconbitmap(r"image/Note2.ico")
	
		self._root.resizable(0,5)
	
		self._root.geometry('800x600')
	
		self.fon = ("Century Gothic" ,15 )

		f= Scrollbar(self._root)
	
		f.pack(side  = "right" , fill = Y)
	
		tv = ttk.Treeview(self._root,yscrollcommand = f.set )
	
		tv.place(relx = 0.0 , rely = 0.0 , relwidth = 0.98 , relheight =1)
	
		f.configure(command = tv.yview)
	
		tv.heading('#0' , text = 'ID')
	
		tv.configure(column = ('#title' , '#Note'))
	
		tv.heading('#title' , text = 'title' )
	
		tv.heading('#Note' , text = 'Note')
	
		tv.column('#0', width=1)
	
		def dele(event):
			see =tv.selection()
			msg =self._dbconnect.DeleteRecord(see[0][1:4])
			tv.delete(see[0])
			showinfo('INFO' , msg)

		def open_note(event):
			
			wind = Tk()
			
			wind.title("Note")
			
			wind.geometry('400x300')
			
			# wind.iconbitmap(r"image/Note2.ico")
			
			see =tv.selection()
			
			cursor = self._dbconnect.Listrequest2(see[0][1:4])
			
			MainText = ScrolledText(wind , font = self.fon , bg = '#fcfbbe')
			
			MainText.place(relx= 0.0 , rely = 0.0 , relwidth = 0.999 , relheight = 0.999)
			
			for row in cursor:
			
					msg = 'title : '+row['title']+'\n\nNote :\n'+row['Note']
			
					MainText.insert(1.0 ,msg)
			MainText['state'] = 'disabled'


		self._root.bind('<Key-d>' , dele)

		self._root.bind('<Key-Return>' , open_note)

		cursor = self._dbconnect.Listrequest()

		for row in cursor:
			
			tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
			
			tv.set('#{}'.format(row['ID']),'#title' , row['title'])
			
			tv.set('#{}'.format(row['ID']),'#Note' , row['Note'])
