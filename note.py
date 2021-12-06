from tkinter import *

from tkinter import ttk , filedialog as tkFileDialog  ,font

import logging

from note_class import DBConnect

from list_notes import List

from datetime import datetime

from tkinter.messagebox import showinfo ,showerror

dbconnect = DBConnect()

log_format = '%(levelname)s - %(asctime)s - %(message)s'

logging.basicConfig(filename = 'data/Note_logs.log' , level = logging.DEBUG,

	format = log_format)

logger = logging.getLogger()


def main():

	now = datetime.today()

	root = Tk()

	root.geometry('700x440')

	root.title('Note book')

	root.resizable(0,0)

	root.configure(bg = '#000')

	backg = '#333'

	foreg = '#fff'

	fon = ("Brush Script MT" ,20 ,'bold')

	# root.iconbitmap(r"image/Note2.ico")


	def BuListData():
		
		Listusers = List()

	def Create() :

		try:
	
			if '' == get_title.get() :
	
				showerror('Filed Error ! ','Please Enter the title !' )
	
			else:

				msg=dbconnect.Add(get_title.get() , get_note.get(1.0, "end") , now)
				
				get_title.delete(0,"end")
				
				get_note.delete(1.0,"end")
				
				showinfo('INFO !' ,'New note has been registered')

				get_note.delete(1.0,"end")
				
				logger.info('saved note')
	
		except Exception as e:
	
			logger.error(e)


	title_l= Label(root , bd=3, relief=SOLID, borderwidth=1 ,  text = "Title",font = fon , bg= backg , fg =foreg )

	title_l.place(relx= 0.1 , rely = 0.01, relwidth = 0.8, relheight = 0.1 )

	get_title= ttk.Entry(root  ,font = fon)

	get_title.place(relx= 0.1 , rely = 0.1 , relwidth = 0.8 , relheight = 0.1)

	note_l= Label(root ,bd=3, relief=SOLID, text = "Note ",font = fon , bg= backg , fg =foreg)

	note_l.place(relx= 0.019 , rely = 0.21 , relwidth = 0.97, relheight = 0.1)

	get_note= Text(root ,bg ='#fcfbbe', insertwidth = 0.5 ,font = fon ,bd=3, relief=SOLID, borderwidth=1  )

	get_note.place(relx= 0.019 , rely = 0.3 , relwidth = 0.97 , relheight = 0.68)

	create_btn= Button(root , bd=3, relief=SOLID, borderwidth=1 , text = "Create",font = fon, cursor = 'hand2',bg=backg , fg =foreg, command =Create)

	create_btn.place(relx= 0.77 , rely = 0.83 , relwidth = 0.2 , relheight = 0.13)

	view_btn= Button(root , bd=3, relief=SOLID, borderwidth=1 , text = "View",font = fon , bg=backg, cursor = 'hand2' , fg =foreg,command =BuListData)

	view_btn.place(relx= 0.77 , rely = 0.67 , relwidth = 0.2 , relheight = 0.13)


	root.mainloop()

if __name__ == '__main__':

	main()