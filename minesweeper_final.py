from Tkinter import *
import random
import time

class minesweeper(object):

#All that has to happen to the "game" as a whole is done in this class, like winning,losing,creation,placements of mines,numbering, all these are issues not related to just a particular box.


	def __init__(self):
		self.game_grid=[]
		self.length=9
		self.width=9
		self.bombs=10
		self.frame1=Frame(game)
		self.frame=Frame(game)
		self.frame2=Frame(game)
		self.flags=10
		self.boxes_closed=self.length*self.width
		self.check_won=0
		self.time_w=Frame(game)
		self.correct_flags=0 #correct_flags are for keeping a count of the flagged boxes which actually contain mines.
		self.ideal_time=0    #ideal_time is a time developed by using the world records and recent statistics in minesweeper.
		self.max_time=0      #max_time is a time developed by using the times we when playing the game.

	def new_game(self):
		self.frame.destroy()
		self.frame2.destroy()
		self.time_w.destroy()
		self.time_w=Frame(game)
		self.frame1=Frame(game)
		self.frame1.pack()
		self.frame=Frame(game)
		button1=Button(self.frame1,text="Beginner",fg="blue",bg="yellow",command=Beginner)
		button1.grid(row=1)
		button2=Button(self.frame1,text="intermediate",fg="blue",bg="yellow",command=Intermediate)
		button2.grid(row=2)
		button3=Button(self.frame1,text="Advanced",fg="blue",bg="yellow",command=Advanced)
		button3.grid(row=3)
		button4=Button(self.frame1,text="CUSTOM",fg="blue",bg="yellow",command=Custom)
		button4.grid(row=4)
	def create_game(self):

		self.correct_flags=0
		self.boxes_closed=self.length*self.width
		self.frame.pack()
		self.game_grid=[[box() for i in range(self.width)] for j in range(self.length)]
		self.flags=self.bombs
		self.put_bombs()     #to randomly assign mines to the boxes.
		self.number_boxes()  #to give the numbers in each box according to the mines around a particular box.
		self.draw_game()     #makes the game grid as per the length and width of the chosen level.
		self.time1=time.time()	#notes the current time of the system.

	def put_bombs(self):
		b=0
		while(b!=self.bombs):
			x1=random.randint(0,self.length-1)
			y1=random.randint(0,self.width-1)
			if(self.game_grid[x1][y1].content!="B"):
				self.game_grid[x1][y1].content="B"
				b+=1 #increasing the count of mines each time a mine is placed
	def number_boxes(self):
		for i in range(self.length):
			for j in range(self.width):
				self.game_grid[i][j].x=i
				self.game_grid[i][j].y=j
				num=0
				around=[(i-1,j),(i+1,j),(i,j-1),(i,j+1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)] #the 3*3 grid around the selected box.
				if(self.game_grid[i][j].content!="B"):
					for (x,y) in around:
						if valid_coordinates(x,y):
							if self.game_grid[x][y].content=="B":
								num+=1
					self.game_grid[i][j].content=num


	def draw_game(self):
		for i in range(self.length):
			for j in range(self.width):
				self.game_grid[i][j].draw(i,j)
	def game_lost(self):
		for i in range(self.length):
			for j in range(self.width):
				self.game_grid[i][j].open_box()
		self.frame2=Frame(game)
		button1=Button(self.frame2,text="QUIT",fg="blue",bg="yellow",command=self.game_quit)
		button1.grid(row=1)
		button2=Button(self.frame2,text="Retry",fg="blue",bg="yellow",command=self.new_game)
		button2.grid(row=2)
		self.frame2.pack()
	def game_quit(self):
		game.destroy()

	def game_won(self):

#A game is won,when the all the boxes flagged, contain mines or when all the boxes exempting the ones with a mine are revealed.
		self.frame.destroy()
		self.frame2=Frame(game)
		label=Label(self.frame2,text="CONGRATULATIONS!!!!",fg="purple")
		button1=Button(self.frame2,text="QUIT",fg="blue",bg="yellow",command=self.game_quit)
		button1.grid(row=2)
		button2=Button(self.frame2,text="Retry",fg="blue",bg="yellow",command=self.new_game)
		button2.grid(row=3)
		self.frame2.pack()

		label.grid(row=1)

		self.time2=time.time()
		self.time_elapsed=self.time2-self.time1

		if self.time_elapsed<=self.ideal_time:
			self.performance_l=Label(self.time_w,text="     performance assessment :  " + "Try some competitions!! :) ",fg="green",bg="black")
		else:
			if self.time_elapsed<self.max_time:
					self.performance_l=Label(self.time_w,text="     performance assessment :  " + "Keep trying! can start with the retry option :P ",fg="green",bg="black")
			else:
				if self.time_elapsed>self.max_time:
					self.performance_l=Label(self.time_w,text="     performance assessment :  " + " Way to go buddy! :) ",fg="green",bg="black")



			self.time_l=Label(self.time_w,text= "     time  =  " + str(self.time_elapsed) + "  seconds" + "       ",fg="red",bg="black")
			self.time_l.grid(row=1)
			self.performance_l.grid(row=3)
			self.time_w.pack()




def Beginner():
	x.length=9
	x.width=9
	x.bombs=10
	x.ideal_time=13.34
	x.max_time=29.6
	x.frame1.destroy()
	x.create_game()
def Intermediate():
	x.length=16
	x.width=16
	x.bombs=40
	x.ideal_time=52.35
	x.max_time=92.001
	x.frame1.destroy()
	x.create_game()
def Advanced():
	x.length=16
	x.width=30
	x.bombs=60
	x.ideal_time=100
	x.max_time=223.78
	x.frame1.destroy()
	x.create_game()
def Custom():

	x.frame1.destroy()
	c_frame=Frame(game)
	c_frame.pack()
	#length
	label_l=Label(c_frame,text="Length ")
	l11=Label(c_frame,text=x.length,fg="black")
	b11=Button(c_frame,text="^",fg="black")
	b11.bind("<Button-1>",lambda event: Press(event,11))
	b12=Button(c_frame,text="v",fg="black")
	b12.bind("<Button-1>",lambda event: Press(event,12))
	label_l.grid(row=0,column=0)
	l11.grid(row=0,column=1)
	b11.grid(row=0,column=2)
	b12.grid(row=0,column=3)
	##length
	#width
	label_w=Label(c_frame,text="Width ")
	l21=Label(c_frame,text=x.width,fg="black")
	b21=Button(c_frame,text="^",fg="black")
	b21.bind("<Button-1>",lambda event: Press(event,21))
	b22=Button(c_frame,text="v",fg="black")
	b22.bind("<Button-1>",lambda event: Press(event,22))
	l21.grid(row=1,column=1)
	b21.grid(row=1,column=2)
	b22.grid(row=1,column=3)
	label_w.grid(row=1,column=0)
	##width
	#bombs
	label_b=Label(c_frame,text="Bombs ")
	l31=Label(c_frame,text=x.bombs,fg="black")
	b31=Button(c_frame,text="^",fg="black")
	b31.bind("<Button-1>",lambda event: Press(event,31))
	b32=Button(c_frame,text="v",fg="black")
	b32.bind("<Button-1>",lambda event: Press(event,32))
	l31.grid(row=2,column=1)
	b31.grid(row=2,column=2)
	b32.grid(row=2,column=3)
	label_b.grid(row=2,column=0)
	##bombs
	b4=Button(c_frame,text="Play")
	b4.bind("<Button-1>",lambda event: Press(event,0))
	b4.grid(row=4,column=1)
##For the custom level, there are two options, we can create 6 buttons and mention an event for 6, or give arbitrary values and make the function work i.e here for the increment and decrement of length,width and no. of mines, is decided by the user. Checks are maintainced such that, the combination of the three that the user chooses doesn't turn out to be trivial.
	def Press(event,n):
		if n==11:
			if x.length<=25:
				x.length+=1
				l11.config(text=x.length,fg="black")
				bomb_check()
		if n==12:
			if x.length>=5:
				x.length-=1
				l11.config(text=x.length,fg="black")
				bomb_check()
		if n==21:
			if x.width<=25:
				x.width+=1
				l21.config(text=x.width,fg="black")
				bomb_check()
		if n==22:
			if x.width>=5:
				x.width-=1
				l21.config(text=x.width,fg="black")
				bomb_check()
		if n==31:
			if x.bombs<=(x.length*x.width)/2:
				x.bombs+=1
				l31.config(text=x.bombs,fg="black")
		if n==32:
			if x.bombs>=x.length:
				x.bombs-=1
				l31.config(text=x.bombs,fg="black")
		if n==0:
			c_frame.destroy()
			x.create_game()
	def bomb_check():
		if x.bombs>(x.length*x.width)/2:
			x.bombs=(x.length*x.width)/2
			l31.config(text=x.bombs,fg="black")

class box():

#All the events that has to happen at the level of a box, are written in here, like, flagging,opening the boxes.
	def __init__(self):
		self.status="closed"
		self.content=0
		self.x=0
		self.y=0
		self.flagged=False
		self.button=Button(x.frame,text="    ",bg="grey")
		self.button.bind("<Button-1>",self.left_clicked)
		self.button.bind("<Button-3>",self.flag)
		self.label=Button(x.frame,text=str(self.content),fg="red",bg="grey")
	def left_clicked(self,event):

		if self.status=="closed":
			x.boxes_closed-=1
			self.status="open"
			if self.flagged:
				x.flags-=1
			if self.content!=0 and self.content!="B":
				self.button.config( text = str(self.content),fg="red",bg="white")
			if self.content==0:
				self.button.config( text ="  ",fg="red",bg="white")
				self.clear_around()
			if self.content=="B":
				x.game_lost()
		if x.boxes_closed == x.bombs and x.check_won==0:
			if self.content!="B":
				x.game_won()
				x.check_won+=1

	def draw(self,i,j):
		if self.status=="closed":
			self.button.grid(row=i,column=j)
		else:
			self.label.grid(row=i,column=j)
	def clear_around(self):
		around=[(self.x-1,self.y),(self.x+1,self.y),(self.x,self.y-1),(self.x,self.y+1),(self.x+1,self.y+1),(self.x+1,self.y-1),(self.x-1,self.y+1),(self.x-1,self.y-1)]
		for (x1,y1) in around:
			if valid_coordinates(x1,y1):
				x.game_grid[x1][y1].left_clicked("<Button-1>")
	def open_box(self):
		self.status="open"
		if self.content!=0:
			self.button.config(text = " "+str(self.content)+" ",fg="red",bg="white")
		else:
			self.button.config(text = "   ",fg="red",bg="white")
	def flag(self,event):

		if not self.flagged :
			if x.flags>0:
				self.flagged=True
				self.button.config( text ="|> ",fg="red",bg="black")
				x.flags-=1
				if self.content=="B":
					x.correct_flags+=1
		else:
			self.flagged=False
			self.button.config( text ="  ",fg="red",bg="grey")
			x.flags+=1
			if self.content=="B":
				x.correct_flags-=1
		if x.correct_flags==x.bombs:
			x.game_won()


def valid_coordinates(x1,y1):    #to check if a box lies in the grid, when we try to number the boxes(the 3?*3 grid around a particular box is checked)
	if x1>=0 and x1<x.length:
		if y1>=0 and y1<x.width:
			return True
	return False

game=Tk()



x=minesweeper()
x.new_game()


game.mainloop()
