cfgPath=""
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmb
from random import randint as rint
import os.path as ospath
import sys
import time
imgCont = 0


class Source():
	# So, sorce
	def __init__(self):
		global cfgPath
		self.cfgPath = cfgPath
		self.cfgFile = None
		self.srcWin = tk.Tk()
		self.Tk = "normal"
		self.dbg = tk.BooleanVar()
		self.dbg.set(True)
		self.xTk = 0
		self.yTk = 0
		self.wrx = 0
		self.wry = 0
		self.ww = 400
		self.wh = 300
		self.sizeX = 0
		self.sizeY = 0
		global imgCont
		self.imgCont = imgCont
		self.clr_bg = self.srcWin.cget('bg')
		self.clr_tw = tk.Entry(self.srcWin).cget("bg")
		self.clr_gw = "ghostwhite"
		self.clr_sb = "steelblue"
		self.clr_lsb = "lightsteelblue"
		self.img_win_alt = self.Fimg("win_alt", """#define win_width 16
#define win_height 16
static unsigned char win_bits[] = {
    0x00, 0x00, 0xfe, 0x7f, 0xfe, 0x7f, 0x02, 0x40, 0xea, 0x4e, 0x02, 0x40,
    0x7a, 0x4f, 0x02, 0x40, 0xba, 0x4d, 0x02, 0x40, 0x7a, 0x4f, 0x02, 0x40,
    0xda, 0x4d, 0x02, 0x40, 0xfe, 0x7f, 0x00, 0x00 };""").fimg
		self.img_win = self.Fimg("win", """#define win_width 16
#define win_height 16
static unsigned char win_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xd8, 0x36, 0xfc, 0x3f, 0x14, 0x22, 0xfc, 0x3f,
    0x44, 0x28, 0xfc, 0x3f, 0x84, 0x24, 0xfc, 0x3f, 0x04, 0x20, 0xfc, 0x3f,
    0x04, 0x21, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };""").fimg
		self.img_min = self.Fimg("min", """#define min_width 16
#define min_height 16
static unsigned char min_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xfc, 0x03, 0xfc, 0x03, 0xfc, 0x03, 0xfc, 0x03,
    0x0c, 0x3b, 0x0c, 0x3b, 0xfc, 0x3b, 0xfc, 0x3b, 0x00, 0x30, 0xc0, 0x30,
    0xc0, 0x3f, 0xc0, 0x3f, 0x00, 0x00, 0x00, 0x00 };""").fimg
		self.img_max = self.Fimg("max", """#define max_width 16
#define max_height 16
static unsigned char max_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xfc, 0x3f, 0xfc, 0x3f, 0xfc, 0x3f, 0xfc, 0x3f,
    0x0c, 0x30, 0x0c, 0x30, 0x0c, 0x30, 0x0c, 0x30, 0x0c, 0x30, 0x0c, 0x30,
    0xfc, 0x3f, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };""").fimg
		self.img_close = self.Fimg("close", """#define close_width 16
#define close_height 16
static unsigned char close_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0x0c, 0x30, 0x1c, 0x38, 0x38, 0x1c, 0x70, 0x0e,
    0xe0, 0x07, 0xc0, 0x03, 0xc0, 0x03, 0xe0, 0x07, 0x70, 0x0e, 0x38, 0x1c,
    0x1c, 0x38, 0x0c, 0x30, 0x00, 0x00, 0x00, 0x00 };""").fimg
		self.img_open = self.Fimg("open", """#define open32_width 32
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
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };""").fimg
		self.img_save = self.Fimg("save", """#define save16_width 16
#define save16_height 16
static unsigned char save16_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xf8, 0x0f, 0x74, 0x14, 0x74, 0x24, 0x74, 0x24,
    0xf4, 0x27, 0x04, 0x20, 0x04, 0x20, 0xe4, 0x27, 0x14, 0x28, 0x14, 0x28,
    0x14, 0x28, 0xf8, 0x1f, 0x00, 0x00, 0x00, 0x00 };""").fimg
		self.sbVT = tk.PhotoImage(data="""R0lGODlhEAAgAKEAAEaCtLDE3kaCtEaCtCH+BHNiVlQAIfkEAQoAAgAsAAAAABAAIAAAAkOUj3nA
7byCnFQCA6oOV+RNdR9oYeQknqWncqaawu8Z0zNZ4zeY8/vWA/40QeKwUkQeQ0tUczXSsWRTW1Xq
eWgV3EQBADs=""")
		self.sbVG = tk.PhotoImage(data="""R0lGODlhEAAQAKEBAEaCtLDE3rDE3rDE3iH+BHNiVkcAIfkEAQoAAgAsAAAAABAAEAAAAisUgqkI
YgGinNCdia9dvL6uNE9GiRcZeQeYmGy7oakra9/rviok7/WuaxQAADs=""")
		self.sbVR = tk.PhotoImage(data="""R0lGODlhEAABAIABAP///0aCtCH+BHNiVlIAIfkEAQoAAQAsAAAAABAAAQAAAgSEjwkFADs=""")
		self.sbHT = tk.PhotoImage(data="""R0lGODlhIAAQAKEAAEaCtLDE3kaCtEaCtCH+BHNiSFQAIfkEAQoAAgAsAAAAACAAEAAAAjeUj6mr
4A+jnAeEi7PeHBjLhSLmCeCIauWZtmsLB2+czvRo32Gub3yf+QEvwmHJNEkqH4ymc1EAADs=""")
		self.sbHG = tk.PhotoImage(data="""R0lGODlhEAAQAKEBAEaCtLDE3rDE3rDE3iH+BHNiSEcAIfkEAQoAAgAsAAAAABAAEAAAAieUjynA
7Q+CnLRKdmPAW/PvhdnYkaApluq5puzrxujcWjYF5Y3CHwUAOw==""")
		self.sbHR = tk.PhotoImage(data="""R0lGODlhAQAQAIABAP///0aCtCH+BHNiSFIAIfkEAQoAAQAsAAAAAAEAEAAAAgSEjwkFADs=""")
		self.sbUN = tk.PhotoImage(data="""R0lGODlhEAAQAIABAEaCtLDE3iH+BHNiVU4AIfkEAQoAAQAsAAAAABAAEAAAAiaMj3nA7byehGFO
YyV+23X6AZ/iVWDSbApCnaRoZmksw/VMW+t+FAA7""")
		self.sbUP = tk.PhotoImage(data="""R0lGODlhEAAQAIAAALDE3rDE3iH+BHNiVVAAIfkEAQoAAQAsAAAAABAAEAAAAiaMj3nA7byehGFO
YyV+23X6AZ/iVWDSbApCnaRoZmksw/VMW+t+FAA7""")
		self.sbDN = tk.PhotoImage(data="""R0lGODlhEAAQAIABAEaCtLDE3iH+BHNiRE4AIfkEAQoAAQAsAAAAABAAEAAAAiaMj3nA7byehGFO
YyUGClHaVZw4Ks0GRp/jseT5rhk8uzUcX+FeAAA7""")
		self.sbDP = tk.PhotoImage(data="""R0lGODlhEAAQAIAAALDE3rDE3iH+BHNiRFAAIfkEAQoAAQAsAAAAABAAEAAAAiaMj3nA7byehGFO
YyUGClHaVZw4Ks0GRp/jseT5rhk8uzUcX+FeAAA7""")
		self.sbLN = tk.PhotoImage(data="""R0lGODlhEAAQAIABAEaCtLDE3iH+BHNiTE4AIfkEAQoAAQAsAAAAABAAEAAAAiaMj3nA7byehGEC
47CMdPNbZYgojo1GmV2Jgl7bnnDokdbzWcqeFAA7""")
		self.sbLP = tk.PhotoImage(data="""R0lGODlhEAAQAIAAALDE3rDE3iH+BHNiTFAAIfkEAQoAAQAsAAAAABAAEAAAAiaMj3nA7byehGEC
47CMdPNbZYgojo1GmV2Jgl7bnnDokdbzWcqeFAA7""")
		self.sbRN = tk.PhotoImage(data="""R0lGODlhEAAQAIABAEaCtLDE3iH+BHNiUk4AIfkEAQoAAQAsAAAAABAAEAAAAieMj3nA7byehMGZ
CW6LT1O/VSFHWYlpIugIZuL3hukEtjLW2ZLCJwUAOw==""")
		self.sbRP = tk.PhotoImage(data="""R0lGODlhEAAQAIAAALDE3rDE3iH+BHNiUlAAIfkEAQoAAQAsAAAAABAAEAAAAieMj3nA7byehMGZ
CW6LT1O/VSFHWYlpIugIZuL3hukEtjLW2ZLCJwUAOw==""")
		self.srcStyle = ttk.Style()
		self.srcStyle.theme_create("deft", parent="alt", settings={
			   "TLabel": {
				   "configure": {
					"background": self.clr_bg
				}
			}, "TButton": {
				   "configure": {
					"margins": [0],
					"padding": [3],
					"relief": "flat", 
					"highlightthickness": 0, 
					"borderwidth": 0
				}
			}, "TNotebook": {
				   "configure": {"borderwidth": 0, "tabmargins": [3, 4, 2, 0], "tabpadding": [99]}
			}, "TNotebook.Tab": {
				   "configure": {
					"borderwidth": 0, 
					"padding": [5, 3], 
					"compound": "left"
				}, "map": {
					"background": [("selected", self.clr_tw), ("", self.clr_bg)] 
				}
			}, "Vertical.TScrollbar": {
				   "configure": {
					"relief": "flat", 
					"highlightthickness": 0, 
					"borderwidth": 0,
					"background": self.clr_tw
				}, "layout": [
					("Vertical.Scrollbar.uparrow", {"side": "top", "sticky": ""}),
					("Vertical.Scrollbar.downarrow", {"side": "bottom", "sticky": ""}),
					("Vertical.Scrollbar.uparrow", {"side": "bottom", "sticky": ""}),
					("Vertical.Scrollbar.trough", {"sticky": "ns", "children": [
						("Vertical.Scrollbar.thumb", {"expand": 1, "unit": 1, "children": [
							("Vertical.Scrollbar.grip", {"sticky": ""})
						]})
					]})
				]
			}, "Horizontal.TScrollbar": {
				   "configure": {
					"relief": "flat", 
					"highlightthickness": 0, 
					"borderwidth": 0,
					"background": self.clr_tw
				}, "layout": [
					("Horizontal.Scrollbar.leftarrow", {"side": "left", "sticky": ""}),
					("Horizontal.Scrollbar.rightarrow", {"side": "right", "sticky": ""}),
					("Horizontal.Scrollbar.leftarrow", {"side": "right", "sticky": ""}),
					("Horizontal.Scrollbar.trough", {"sticky": "ew", "children": [
						("Horizontal.Scrollbar.thumb", {"expand": 1, "unit": 1, "children": [
							("Horizontal.Scrollbar.grip", {"sticky": ""})
						]})
					]})
				]
			}
		})
		self.srcStyle.theme_use("deft")
		self.srcStyle.element_create("Horizontal.Scrollbar.thumb", "image", self.sbHT, border=3, sticky="ew")
		self.srcStyle.element_create("Horizontal.Scrollbar.grip", "image", self.sbHG)
		self.srcStyle.element_create("Horizontal.Scrollbar.trough", "image", self.sbHR)
		self.srcStyle.element_create("Vertical.Scrollbar.thumb", "image", self.sbVT, border=3, sticky="ns")
		self.srcStyle.element_create("Vertical.Scrollbar.grip", "image", self.sbVG)
		self.srcStyle.element_create("Vertical.Scrollbar.trough", "image", self.sbVR)
		
		self.srcStyle.element_create("Scrollbar.uparrow", "image", self.sbUN, ("pressed", self.sbUP), sticky="")
		self.srcStyle.element_create("Scrollbar.downarrow", "image", self.sbDN, ("pressed", self.sbDP), sticky="")
		self.srcStyle.element_create("Scrollbar.leftarrow", "image", self.sbLN, ("pressed", self.sbLP), sticky="")
		self.srcStyle.element_create("Scrollbar.rightarrow", "image", self.sbRN, ("pressed", self.sbRP), sticky="")

	# Funcions
	def quit(self): self.srcWin.destroy()
	def lulzf(self): print("Source.lulzf(): LULZ!!!")
	def setpath(self, strv):
		global cfgPath
		cfgPath = strv
		self.cfgPath = strv
	def resetcfg(self):
		if self.cfgPath == "": 
			return
		else: 
			self.cfgFile = open(cfgPath, "x").read()
	def setcfg(self):
		filepath = tkfd.askopenfilename(
			title="Open config",
			filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")]
		)
		if not filepath: return

	# Funcion-image (fimage, fimg)
	class Fimg():
		def __init__(self, fimgName, fimgData):
			self.fimgData = fimgData
			self.fimgName = str(fimgName)
		def fimg(self, fg, bg=None, **kw):
			global imgCont
			imgCont += 1
			self.imgCont = imgCont
			name = f'bitmap:"{self.fimgName}",cont:{self.imgCont}'
			img = {
				"name": name, 
				"imgtype": "bitmap", 
				"data": self.fimgData, 
				"foreground": fg
			}
			if "takename" in list(kw.keys()): takename = kw["takename"]
			else: takename = 0
			if takename == 1:
				if bg == None: return tk.Image(**img), name
				else: return tk.Image(**img, background=bg), name
			elif takename == 0:
				if bg == None: return tk.Image(**img)
				else: return tk.Image(**img, background=bg)



class App():
	# Sourse
	def __init__(self):
		self.version = "1.b4"
		self.source = Source()
		self.mWin = self.source.srcWin
		if sys.platform == "win32": self.mWin.overrideredirect(True)
		else: self.mWin.attributes('-type', "dock")
		self.mWin.title("ExtPad")
		self.mWin.geometry("400x300")
		self.mWin["takefocus"] = True
		self.style = self.source.srcStyle
		self.clr_bg = self.source.clr_bg
		self.clr_tw = self.source.clr_tw
		self.clr_gw = self.source.clr_gw
		self.clr_sb = self.source.clr_sb
		self.clr_dsb = "darkslateblue"
		self.clr_lsb = self.source.clr_lsb
		self.img_win = self.source.img_win(self.clr_gw)
		self.img_win_alt, self.imgname_win_alt = self.source.img_win(self.clr_gw, takename=1)
		self.mWin.iconname(self.imgname_win_alt)
		self.img_min = self.source.img_min(self.clr_gw)
		self.img_max = self.source.img_max(self.clr_gw)
		self.img_close = self.source.img_close(self.clr_gw)
		self.mLblCheck = -1
		self.style.map("stibl.TButton",
			foreground = [("active", self.clr_gw), ("", self.clr_gw)], 
			background = [("active", self.clr_lsb), ("", self.clr_sb)]
		)
		self.style.configure("stibl.TButton", font=10)
		self.style.map("ghost.TFrame", background = [("", self.clr_tw)])

		# Title-Bar: wmButton, mainLabel, mainLabel
		self.tBar = tk.Frame(self.mWin, bg=self.clr_dsb, bd=1)
		self.wmBtn = ttk.Button(self.tBar, image=self.img_win, style="stibl.TButton")
		self.mMG = tk.Canvas(self.tBar, bg=self.clr_sb, highlightthickness=0, height=0)
		self.mMG.bind('<Button-1>', self.pointTk)
		self.mMG.bind('<B1-Motion>', self.moveTk)
		self.mMinBtn  = ttk.Button(self.tBar, style="stibl.TButton", image=self.img_min,   command=self.withMin)
		self.mMaxBtn  = ttk.Button(self.tBar, style="stibl.TButton", image=self.img_max,   command=self.withMax)
		self.mQuitBtn = ttk.Button(self.tBar, style="stibl.TButton", image=self.img_close, command=self.withQuit)
			# Menu
				# Controls
		self.menuBar = tk.Frame(self.tBar, bg=self.clr_dsb)
		self.mbFile = ttk.Button(self.menuBar, text="File", style="stibl.TButton")
		self.mbMods = ttk.Button(self.menuBar, text="Mods", style="stibl.TButton")
		self.mbHelp = ttk.Button(self.menuBar, text="Help", style="stibl.TButton")
				# Bind this
		self.wmBtn.bind('<Button-1>', self.popWM)
		self.mbFile.bind('<Button-1>', self.popFile)
		self.mbMods.bind('<Button-1>', self.popMods)
		self.mbHelp.bind('<Button-1>', self.popHelp)
				# tkMenus
		self.wmMenu = tk.Menu(self.mWin, tearoff=0)
		self.fMenu = tk.Menu(self.mWin, tearoff=0)
		self.modMenu = tk.Menu(self.mWin, tearoff=0)
		self.hMenu = tk.Menu(self.mWin, tearoff=0)
					# WM menu
		self.wmMenu.add_command(label="Normal window", command=self.withMin)
		self.wmMenu.add_command(label="Zoom window", command=self.withMax)
		self.wmMenu.add_command(label="Quit", accelerator="Ctrl-Q", command=self.withQuit)
					# File menu
		self.fMenu.add_command(label="Save", accelerator="Ctrl-S", command=self.nSave)
		self.fMenu.add_command(label="Save as...", accelerator="Ctrl-Shift-S", command=self.nSaveas)
		self.fMenu.add_command(label="Open", accelerator="Ctrl-O", command=self.nOpen)
		self.fMenu.add_command(label="New", accelerator="Ctrl-N", command=self.nNew)
		self.fMenu.add_command(label="Close", accelerator="Ctrl-Shift-D", command=self.nClose)
					# Mods menu
		self.modMenu.add_command(label="Exec mod", command=self.modexec)
					# Help menu
		self.hMenu.add_command(label="About", accelerator="F1", command=self.source.lulzf)
		self.hMenu.add_checkbutton(label="debug", onvalue=True, offvalue=False, variable=self.source.dbg)
			# Pack this
		self.mQuitBtn.pack(fill="both", side="right")
		self.mMaxBtn.pack(fill="both", side="right")
		self.wmBtn.pack(fill="both", side="left")
		self.menuBar.pack(fill="both", side="left")
		self.mbFile.pack(fill="both", side="left")
		self.mbMods.pack(fill="both", side="left")
		self.mbHelp.pack(fill="both", side="left")
		self.mMG.pack(fill="both", expand=True)
		self.tBar.pack(fill="both", side="top")

		# Help-Bar: mainSizegrip, tkhelpButton, mainLabel
		self.hBar = ttk.Frame(self.mWin)
		self.mSG = ttk.Sizegrip(self.hBar)
		self.mLbl = tk.Label(self.hBar, text=f"Hello in ExtPad {self.version}!", anchor="w", padx=3)
			# Pack this
		self.mSG.pack(fill="both", side="right")
		self.mLbl.pack(fill="both", expand=True)
		self.hBar.pack(fill="both", side="bottom")

		# mainNoteBook
		self.img_save = self.source.img_save(self.clr_sb)
		self.mNB = ttk.Notebook(self.mWin, height=0)
		self.iif = ttk.Frame(self.mNB)
		self.iil = ttk.Label(self.iif)
		self.iil.pack(fill="both")
			# Pack this
		self.mNB.bind("<<NotebookTabChanged>>", self.nSel)
		self.mNB.pack(fill="both", expand=True)

	# Funcions
		# Tk
	def forceTk(self): self.mWin.focus_force()
	def pointTk(self, event):
		if sys.platform != "win32": self.mWin.attributes('-type', "normal")
		win_position = [int(coord) for coord in self.mWin.wm_geometry().split('+')[1:]]
		self.source.xTk, self.source.yTk = win_position[0] - event.x_root, win_position[1] - event.y_root
	def moveTk(self, event): 
		if self.source.Tk == "max": 
			self.withMin()
			return
		else: self.mWin.wm_geometry(f"+{str(event.x_root+self.source.xTk)}+{str(event.y_root+self.source.yTk)}")
	def withMin(self):
		if self.source.Tk != "normal":
			self.mMinBtn.pack_forget()
			self.mMG.pack_forget()
			self.mLbl.pack_forget()
			self.mSG.pack(fill="both", side="right")
			self.mLbl.pack(fill="both", expand=True)
			self.mWin.geometry(f"{self.source.ww}x{self.source.wh}+{self.source.wrx}+{self.source.wry}")
			self.mMaxBtn.pack(fill="both", side="right")
			self.mMG.pack(fill="both", expand=True)
			self.source.Tk = "normal"
	def withMax(self):
		if self.source.Tk != "max":
			self.mMaxBtn.pack_forget()
			self.mMG.pack_forget()
			self.mSG.pack_forget()
			self.tmpx = self.mWin.cget("padx")
			self.tmpy = self.mWin.cget("pady")
			self.source.wrx = self.mWin.winfo_rootx()
			self.source.wry = self.mWin.winfo_rooty()
			self.source.ww  = self.mWin.winfo_width()
			self.source.wh  = self.mWin.winfo_height()
			self.mWin.geometry(f"{self.mWin.winfo_screenwidth()}x{self.mWin.winfo_screenheight()}+0+0")
			self.mMinBtn.pack(fill="both", side="right")
			self.mMG.pack(fill="both", expand=True)
			self.source.Tk = "max"
	def withQuit(self):
		self.source.quit()
		# Menu
	def popWM(self, event):
		self.wmMenu.tk_popup(event.x_root, event.y_root, 0)
		self.wmBtn.focus_force()
	def popFile(self, event):
		self.fMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbFile.focus_force()
	def popMods(self, event):
		self.modMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbMods.focus_force()
	def popHelp(self, event):
		self.hMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbHelp.focus_force()
		# Notebook (aka n-prefixed)
	def nSel(self, event):
		if   len(self.mNB.tabs()) == 0:
			self.mLbl["text"] = f"Hello in ExtPad {self.version}!"
			self.mLblCheck = -1
		elif self.source.dbg.get() == True:
			self.mLbl["text"] = f'Selected "{str(self.mNB.select())}" tab: {self.mNB.tab(self.mNB.select())}'
			self.mLblCheck = 20
	def nOpen(self, path=None):
		# Input path, text
		if path == None:
			path = tkfd.askopenfilename(
				title="Open file",
				filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")]
			)
			self.forceTk()
			if not path: return
		nfile = open(str(path))
		text = nfile.read()
		nfile.close()
		name = ospath.split(path)[-1]
		# Controls
		nPage = ttk.Frame(self.mNB, style="ghost.TFrame", name=f'file:"{path.replace(".", "%2E")}"')
		nText = tk.Text(nPage, bd=0, highlightthickness=0, wrap="none", undo=True)
		nSBX = ttk.Scrollbar(nPage, command=nText.xview, orient="horizontal")
		nSBY = ttk.Scrollbar(nPage, command=nText.yview, orient="vertical")
		nText.config(xscrollcommand=nSBX.set, yscrollcommand=nSBY.set)
		nText.insert("1.0", text)
		nText.edit_modified(0)
		# Grid controls
		nSBX.grid(column=0, row=1, sticky="nsew")
		nSBY.grid(column=1, row=0, sticky="nsew")
		nText.grid(column=0, row=0, sticky="nsew")
		nPage.rowconfigure(0, weight=1)
		nPage.columnconfigure(0, weight=1)
		self.mNB.add(nPage, text=name, image=self.img_save)
	def nSaveas(self):
		path = tkfd.asksaveasfilename(
			title="Save as",
			defaultextension=".txt", 
			filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")]
		)
		self.forceTk()
		if not path: return
		try:
			nText = self.mWin.nametowidget(self.mNB.select()+".!text")
			nText.edit_reset()
			nText.edit_modified(0)
			nfile = open(path, "w")
			nfile.write(nText.get("1.0", "end").rstrip("\n"))
			nfile.close()
		except: print("AppErorr: Can't save file")
	def nSave(self):
		if self.mNB.tabs() == (): return
		nText = self.mWin.nametowidget(self.mNB.select()+".!text").edit_modified(0)
		tmpText = nText.get("1.0", "end").rstrip("\n")
		path = self.mNB.select().split(":")[1].strip('"').replace("%2E", ".")
		open(path).write(tmpText).close()
		self.mLbl["text"] = "Saved"
	def nNew(self):
		path = tkfd.asksaveasfilename(
			title="New file",
			defaultextension=".txt", 
			filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")]
		)
		self.forceTk()
		if not path: return
		name = ospath.split(path)[-1]
		# Controls
		nPage = ttk.Frame(self.mNB, style="ghost.TFrame", name=f'file:"{path.replace(".", "%2E")}"')
		nText = tk.Text(nPage, bd=0, highlightthickness=0, wrap="none", undo=True)
		nSBX = ttk.Scrollbar(nPage, command=nText.xview, orient="horizontal")
		nSBY = ttk.Scrollbar(nPage, command=nText.yview, orient="vertical")
		nText.config(xscrollcommand=nSBX.set, yscrollcommand=nSBY.set)
		# Grid controls
		nSBX.grid(column=0, row=1, sticky="nsew")
		nSBY.grid(column=1, row=0, sticky="nsew")
		nText.grid(column=0, row=0, sticky="nsew")
		nPage.rowconfigure(0, weight=1)
		nPage.columnconfigure(0, weight=1)
		self.mNB.add(nPage, text=name, image=self.img_save)
	def nClose(self):
		if self.mNB.tabs() == (): return
		seltype = self.mNB.select().split(":")[0].split(".")[-1]
		if seltype == "file":
			nText = self.mWin.nametowidget(self.mNB.select()+".!text")
			if nText.edit_modified():
				save = tkmb.askyesnocancel(
					"Save file",
					"You have unsaved changes.\nDo you want to save before closing?",
				)
				if save: self.nSave()
				elif save == None: return
		elif seltype == "cfg":
			print("is Config!")
		else: print("fail type")
		self.mNB.forget(self.mNB.select())

		# Etc
	def altstream(self):
		self.mWin.after(80, self.altstream)
		self.mLblCheck = round(self.mLblCheck)
		if self.mLblCheck == 0:
			path = self.mNB.select().split(":")[1].strip('"').replace("%2E", ".")
			nText = self.mWin.nametowidget(self.mNB.select()+".!text")
			insLine, insCol = str.split(nText.index("insert"), ".")
			endLine = str(int(str.split(nText.index("end"), ".")[0]) - 1)
			endCol = str.split(nText.index(f"{insLine}.end"), ".")[1]
			self.mLbl["text"] = f"Line: {insLine}/{endLine}  Col: {insCol}/{endCol}  Path: {path}"
		elif self.mLblCheck > 0:
			self.mLblCheck -= 1

	def modexec(self, path=None):
		if path == None:
			path = tkfd.askopenfilename(
				title="Exec file",
				filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")]
			)
			if not path: return
		modfile = open(path)
		exec(modfile.read())
		modfile.close()

	# mainloop the mWin
	def init(self):
		self.forceTk()
		self.mWin.bind("<Control-q>", lambda ev: self.withQuit())
		self.mWin.bind("<Control-o>", lambda ev: self.nOpen())
		self.mWin.bind("<Control-s>", lambda ev: self.nSave())
		self.mWin.bind("<Control-S>", lambda ev: self.nSaveas())
		self.mWin.bind("<Control-n>", lambda ev: self.nNew())
		self.mWin.bind("<Control-D>", lambda ev: self.nClose())
		self.mWin.bind("<F1>", lambda ev: self.source.lulzf())
		self.mWin.update()
		self.mWin.minsize(
			int(self.wmBtn.winfo_width() * 4.5) + self.menuBar.winfo_width(), 
			self.tBar.winfo_height() + self.hBar.winfo_height()
		)
		self.mWin.after_idle(self.altstream)
		self.mWin.mainloop()


if __name__ == "__main__": 
	app = App()
	app.init()
