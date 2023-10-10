
from tkinter import *
import tkinter as tk
from TextSearch import search_keyword ;










## This the Custom Table To show the Out Put Of The Search 

class Table:
	def __init__(self , root , dataList , headerList ):
		self.dataList = dataList
		self.headerList = headerList
		if( dataList == "Not Found" ):
			self.e = Entry(root, width=75, fg='red', bg='white' ,
                               font=('Arial',16,'bold') ,justify='center' )
			self.e.grid(row=0 , column=0 )
			self.e.insert(END , ('No Matches Found !'))
			return 
		TableHeader(root , self.headerList )
		for i in range(len(dataList)):
			for j in range(len(dataList[0])):
				textContent = StringVar() 
				textContent.set(dataList[i][j])
				w = 45 if j == 0  else 20 
				self.e = Entry(root, width=w, fg='blue', bg='white' ,
                               font=('Arial',16,'bold') , textvariable=textContent ,
							   state='readonly')
				self.e.grid(row=i+1 , column=j )
		
## The Table Header Is he Part Of The Table 

class TableHeader:
	def __init__(self , root , headerList):
		self.headerList = headerList
		for i in range(len(headerList)):
			for j in range(len(headerList[0])):
				textContent = StringVar() 
				textContent.set(headerList[i][j])
				w = 45 if j == 0  else 20 
				self.h = Entry(root, width=w, fg='black', textvariable=textContent ,
                               font=('Arial',16,'bold') , state=DISABLED )
				
				self.h.grid(row=i , column=j )
				

##The Single Entry Form Is a Form Template Which Has an Entry and A Button Widget  

class SingleEntryForm:
	def __init__(self , frame , entryType ):
		self.textBox = Text(
							frame , 
							height = 1,
							font=80 ,
							width = 60,
							bd=3
						)
		self.button = Button(
			frame ,
			text = "Search" if  entryType == 'search' else 'Add' ,
			bg='skyblue' ,
			fg='black',
			command = self.printInput if  entryType == 'search' else self.addDirectory  ,
			height=1,
			width=10,
			font=80
		)

		self.textBox.grid(row=1 , column=1)
		self.button.grid(row=1 , column=2)
	
	def printInput(self):
		keyword = self.textBox.get(1.0, "end-1c")
		for dir_path in dir_paths:
			res = search_keyword(dir_path[0]  , keyword )
		clear_frame(frame)
		headerList = [( 'File Paths' , 'Line No')]
		Table(frame , res , headerList)

	def addDirectory(self):
		global dir_paths 
		li = []
		dir_path = self.textBox.get(1.0, "end-1c")
		li.append(dir_path)
		if dir_paths.__contains__(li) == False  :
			dir_paths.append( li )
		headerList  = [( 'Directories' , )]
		Table(dirFrame , dir_paths , headerList )


	
# Top level window
root = tk.Tk()
root.title("Text Search App")
root.geometry('900x600')


#response table frame
frame = tk.Frame(root ,height = 150,
				width = 150  )

# directory table list frame
dirFrame = tk.Frame(root)





# search bar 
searchBar = tk.Frame(root ,height = 5,
				width = 60  )

SingleEntryForm(searchBar , entryType='search' ) 

# directory list 

dirList = tk.Frame(root , width=60 , height=5 )
SingleEntryForm(dirList , entryType='add_dir')


dir_paths = [] 



# clear frame widgets 
def clear_frame(frame):
	for widget in frame.winfo_children():
		widget.destroy()







# packing parent widgets
dirList.pack()
dirFrame.pack()
searchBar.pack()
frame.pack()
root.mainloop()
