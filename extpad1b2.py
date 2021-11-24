cfgPath=""
import tkinter as tk
import tkinter.ttk as ttk
import time


class Source():

	def __init__(self):
		global cfgPath
		self.xTk = 0
		self.yTk = 0
		self.sizeX = 0
		self.sizeY = 0
		self.nID = ""
		self.cfgPath = cfgPath
		self.imgstr = "Base64Code"
		self.swin = tk.Tk()
		self.img_close = tk.BitmapImage(data="""#define close_width 16
#define close_height 16
static unsigned char close_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0x0c, 0x30, 0x1c, 0x38, 0x38, 0x1c, 0x70, 0x0e,
    0xe0, 0x07, 0xc0, 0x03, 0xc0, 0x03, 0xe0, 0x07, 0x70, 0x0e, 0x38, 0x1c,
    0x1c, 0x38, 0x0c, 0x30, 0x00, 0x00, 0x00, 0x00 };""", \
foreground="black")
		self.img_win = tk.BitmapImage(data="""#define winIco_width 16
#define winIco_height 16
static unsigned char winIco_bits[] = {
    0x00, 0x00, 0xf8, 0x3f, 0x04, 0x60, 0xfe, 0x5f, 0x02, 0x70, 0xfe, 0x5f,
    0x02, 0x50, 0x7a, 0x52, 0x02, 0x57, 0x9a, 0x52, 0x42, 0x51, 0xe2, 0x50,
    0x62, 0x56, 0x02, 0x30, 0xfe, 0x1f, 0x00, 0x00};""", \
foreground="black")
		self.img_min = tk.BitmapImage(data="""#define min_width 16
#define min_height 16
static unsigned char min_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xfc, 0x03, 0xfc, 0x03, 0xfc, 0x03, 0xfc, 0x03,
    0x0c, 0x3b, 0x0c, 0x3b, 0xfc, 0x3b, 0xfc, 0x3b, 0x00, 0x30, 0xc0, 0x30,
    0xc0, 0x3f, 0xc0, 0x3f, 0x00, 0x00, 0x00, 0x00 };""", \
foreground="black")
		self.img_max = tk.BitmapImage(data="""#define max_width 16
#define max_height 16
static unsigned char max_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xfc, 0x3f, 0xfc, 0x3f, 0xfc, 0x3f, 0xfc, 0x3f,
    0x0c, 0x30, 0x0c, 0x30, 0x0c, 0x30, 0x0c, 0x30, 0x0c, 0x30, 0x0c, 0x30,
    0xfc, 0x3f, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };""", \
foreground="black")
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
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };""", \
foreground="black")
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
	def lulzf(self): print("Source.lulzf(): init")
	def quit(self): self.swin.destroy()



def app():
	# Sourse
	source = Source()
	mWin = source.swin
	img_win = source.img_win
	img_min = source.img_min
	img_max = source.img_max
	img_close = source.img_close
	mWin.title("ExtPad")
	mWin.geometry("400x300")
	mWin.attributes('-type', 'dock')
	blueButton = {"relief":"flat", "bg":"skyblue", "pady":0, "highlightthickness":0, "borderwidth":0}
	mBG = mWin.cget('bg')
	exemple = tk.Entry(mWin)
	mFG = exemple.cget('bg')
	style = ttk.Style()
	style.theme_create("deft", parent="default", settings={
			   "TNotebook": {
				"configure": {"borderwidth": 0,"tabmargins": [3, 4, 2, 0]}
			}, "TNotebook.Tab": {
				"configure": {"borderwidth": 0, "padding": [5, 1], "background": mBG},
				"map": {"background": [("selected", mFG)] }
			}
		}
	)
	style.theme_use("deft")

	# Funcions
	def forceTk(): mWin.focus_force()
	def pointTk(event):
		win_position = [int(coord) for coord in mWin.wm_geometry().split('+')[1:]]
		source.xTk, source.yTk = win_position[0] - event.x_root, win_position[1] - event.y_root
		forceTk()
	def moveTk(event): 
		mWin.wm_geometry("+%d+%d" % (event.x_root + source.xTk, event.y_root + source.yTk))
	def withMin():
		mMinBtn.pack_forget()
		mMG.pack_forget()
		mMaxBtn.pack(fill="both", side="right")
		mMG.pack(fill="both", expand=True)
	def withMax():
		mMaxBtn.pack_forget()
		mMG.pack_forget()
		tmpx = mWin.cget("padx")
		tmpy = mWin.cget("pady")
		mLbl["text"] = f"root x={tmpx}, y={tmpy}; xTk={source.xTk}, yTk={source.yTk}, wrx={mWin.winfo_rootx()}; wry={mWin.winfo_rooty()}"
		mMinBtn.pack(fill="both", side="right")
		mMG.pack(fill="both", expand=True)
	def withQuit():
		source.quit()
	def menupopFile(event):
		fMenu.tk_popup(event.x_root, event.y_root, 0)
		mbFile.focus_force()
	def nSel(event):
		source.nID = mNB.select()
		mLbl["text"] = f'Selected tab: {mNB.tab(source.nID, "text")}'

	# Help-Bar: mainSizegrip, tkhelpButton, mainLabel
	hBar = tk.Frame(mWin, borderwidth=1)
	mSG = ttk.Sizegrip(hBar)
	mLbl = tk.Label(hBar, text="[Information label]", anchor="w")
		# Pack this
	mSG.pack(fill="both", side="right")
	mLbl.pack(fill="both", expand=True)
	hBar.pack(fill="both", side="bottom")

	# Title-Bar: wmButton, mainLabel, mainLabel
	tBar = tk.Frame(mWin, bg="skyblue")
	wmBtn = tk.Button(tBar, image=img_win, **blueButton)
	menuBar = tk.Frame(tBar, bg="skyblue")
	mbFile = tk.Button(menuBar, text="File", **blueButton)
	mbFile.bind('<Button-1>', menupopFile)
	mMG = tk.Canvas(tBar, bg="skyblue", highlightthickness=0, height=0)
	mMG.bind('<Button-1>', pointTk)
	mMG.bind('<B1-Motion>', moveTk)
	mMinBtn = tk.Button(tBar, image=img_min, command=withMin, **blueButton)
	mMaxBtn = tk.Button(tBar, image=img_max, command=withMax, **blueButton)
	mQuitBtn = tk.Button(tBar, image=img_close, command=withQuit, **blueButton)
		# Menu
	fMenu = tk.Menu(mWin, tearoff=0)
	fMenu.add_command(label="lulz init", command=source.lulzf)
	fMenu.add_command(label="quit", command=withQuit)
		# Pack this
	mQuitBtn.pack(fill="both", side="right")
	mMaxBtn.pack(fill="both", side="right")
	wmBtn.pack(fill="both", side="left")
	menuBar.pack(fill="both", side="left")
	mbFile.pack(fill="both", side="right")
	mMG.pack(fill="both", expand=True)
	tBar.pack(fill="both", side="top")

	# mainNoteBook

	mNB = ttk.Notebook(mWin, height=0)
	nPage1 = tk.Frame(mNB)
	nPage2 = tk.Frame(mNB)
	n1Text = tk.Text(nPage1, borderwidth=0, highlightthickness=0)
	n2Text = tk.Text(nPage2, borderwidth=0, highlightthickness=0)
		# Pack this
	n1Text.pack(fill="both", expand=True)
	n2Text.pack(fill="both", expand=True)
	mNB.add(nPage1, text="Page1")
	mNB.add(nPage2, text="Page2")
	mNB.bind("<<NotebookTabChanged>>", nSel)
	mNB.pack(fill="both", expand=True)

	# mainloop the mWin
	forceTk()
	mWin.mainloop()


if __name__ == "__main__": app()

