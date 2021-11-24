cfgPath=""
import tkinter as tk
import tkinter.tix as tix
import tkinter.ttk as ttk
import time


class Source():

	def __init__(self):
		global cfgPath
		self.cfgPath = cfgPath
		self.imgstr = "Base64Code"
		self.swin = tix.Tk()
		self.img_open = tk.BitmapImage(data="""#define open32_width 32
#define open32_height 32
static unsigned char open32_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0xc0, 0xff, 0xff, 0x00, 0xc0, 0xff, 0xff, 0x00,
   0x30, 0x00, 0xf0, 0x03, 0x30, 0x00, 0xf0, 0x03, 0x30, 0x00, 0xf0, 0x0f,
   0x30, 0x00, 0xf0, 0x0f, 0x30, 0xff, 0xf0, 0x0f, 0x30, 0xff, 0xf0, 0x0f,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0xff, 0x3f, 0x0c,
   0x30, 0xff, 0x3f, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0xff, 0x3f, 0x0c, 0x30, 0xff, 0x3f, 0x0c, 0x30, 0x00, 0x00, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0xff, 0x3f, 0x0c, 0x30, 0xff, 0x3f, 0x0c,
   0x30, 0x00, 0x00, 0x0c, 0x30, 0x00, 0x00, 0x0c, 0xc0, 0xff, 0xff, 0x03,
   0xc0, 0xff, 0xff, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };""", foreground="black")
		self.img_p = tk.PhotoImage(data=\
"""R0lGODlhQABAAKECAAAA/wCq/5CQkJCQkCH+FmJ5IEFudHlFbG8gKyB3aXRoIEdJTVAAIfkEAQoA
AgAsAAAAAEAAQAAAAv6Uj6nL7Q+jnLTai7PeoPsPht5WieZJQufKdunSxuJryDZL3vqc7T5v+QlH
paHRNTkeKUojsymUQJWqqfNhvTqywy0oAA6LxaHxuGwOfxjo9PnrDrTTa5gnTr/j5Xp8XfGx99Yh
GLj3l2AIdkPG0rjC1scn83hSaRJJqGZzKdIZkgnwabm5MoqIoFjqeCjphnqguhhT6JqHBAj36tmq
6UeUKzuoGydsBlvDu6vacgqcqHwr2byKaUdd6ew7iXLNml0d3RKKza0tGg7qXc78zW0dTLt6fk7u
3m6aDhIqCD6b/69bvH7z9OETCG3br4Mm6nkjOIcdjgZcomCp6KMKRjUdGjfakOJxXJKQE0GSRNjx
pLonKp+xbAlAQ8scKmkIqGgzFZec6zLypKjlp9ChRIsaPVq0AAA7""")

	def getcfg(self):
		if self.cfgPath == "": return 0
		else: return file(cfgPath, "x")

	def helpf(self): help("tkinter")

	def lulzf(self): print("Source.lulzf(): init")

	def quit(self): self.swin.destroy()


xTk = 0
yTk = 0
def app():
	source = Source()
	mWin = source.swin
	mWin.attributes('-type', 'dock')
	tBar = tk.Frame(mWin, bg="skyblue", borderwidth=2)

	def pointTk(event):
		global xTk, yTk
		win_position = [int(coord) for coord in mWin.wm_geometry().split('+')[1:]]
		xTk, yTk = win_position[0] - event.x_root, win_position[1] - event.y_root
	def moveTk(event): 
		global xTk, yTk
		mWin.wm_geometry("+%d+%d" % (event.x_root + xTk, event.y_root + yTk))
		mgLbl.config(text=f"evx={event.x}; evy={event.y}; wrx={mWin.winfo_rootx()}; wry={mWin.winfo_rooty()}, wpx={mWin.winfo_pointerx()}; wpy={mWin.winfo_pointery()}; evk={event.keysym}")

	wmBtn = tk.Button(tBar, text="[WM]", bg="skyblue", width=0)
	wmBtn.grid(row=0, column=0, sticky="swen")
	menuBar = tk.Frame(tBar, bg="skyblue")
	mMenu = tk.Menu(menuBar)
	fMenu = tk.Menu(mMenu)
	fMenu.add_command(label="lulz", command=source.lulzf)
	mMenu.add_cascade(label="about", menu=fMenu)
	menuBar.grid(row=0, column=1, sticky="swen")
	#mWin["menu"] = mMenu
	mMG = tk.Canvas(tBar, bg="skyblue", height=0)
	mMG.grid(row=0, column=2, sticky="swen")
	qBtn = tk.Button(tBar, bg="skyblue", text="X", command=source.quit, width=0)
	qBtn.grid(row=0, column=3, sticky="swen")
	mMG.bind('<Button-1>', pointTk)
	mMG.bind('<B1-Motion>', moveTk)

	mNB = tix.NoteBook(mWin)
	nbEntry = tk.Entry(mNB)
	nbEntry.pack()
	mNB.grid(row=1, column=0, columnspan=3, sticky="swen")

	hBtn = ttk.Button(mWin, text="[Tk]", command=source.helpf, width=0)
	hBtn.grid(row=2, column=0, sticky="swen")
	mgLbl = ttk.Label(mWin, text="Move mMG")
	mgLbl.grid(row=2, column=1, sticky="swen")
	mSG = ttk.Sizegrip(mWin)
	mSG.grid(row=2, column=2, sticky="swen")


	tBar.grid(row=0, columnspan=4, sticky="swen")
	tBar.rowconfigure(0, weight=1)
	tBar.columnconfigure(2, weight=1)

	mWin.rowconfigure(1, weight=1)
	mWin.columnconfigure(1, weight=1)
	mWin.focus_force()
	mWin.iconphoto(1, source.img_p)
	mWin.mainloop()


if __name__ == "__main__": app()
