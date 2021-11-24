cfgPath=""
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
from random import randint as rint
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
		self.sbVT = self.Fimg("Scrollbar_Vetical_thumb", """#define sbvt_width 16
#define sbvt_height 24
static unsigned char sbvt_bits[] = {
    0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
    0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
    0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
    0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00 };""").fimg(self.clr_sb, self.clr_tw)
		self.sbHT = self.Fimg("Scrollbar_Horisontal_thumb", """#define sbht_width 24
#define sbht_height 16
static unsigned char sbht_bits[] = {
    0x00, 0x00, 0x00, 0xfc, 0xff, 0x3f, 0x02, 0x00, 0x40, 0x02, 0x00, 0x40,
    0x02, 0x00, 0x40, 0x02, 0x00, 0x40, 0x02, 0x00, 0x40, 0x02, 0x00, 0x40,
    0x02, 0x00, 0x40, 0x02, 0x00, 0x40, 0x02, 0x00, 0x40, 0x02, 0x00, 0x40,
    0x02, 0x00, 0x40, 0x02, 0x00, 0x40, 0xfc, 0xff, 0x3f, 0x00, 0x00, 0x00 };""").fimg(self.clr_sb, self.clr_tw)
		self.sbU = self.Fimg("Scrollbar_Up-arorr", """#define sbu_width 16
#define sbu_height 16
static unsigned char sbu_bits[] = {
    0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x82, 0x41, 0xc2, 0x43, 0xe2, 0x47,
    0xf2, 0x4f, 0xf2, 0x4f, 0xf2, 0x4f, 0xf2, 0x4f, 0xf2, 0x4f, 0xf2, 0x4f,
    0xe2, 0x47, 0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00 };""").fimg
		self.sbD = self.Fimg("Scrollbar_Down-arorr", """#define sbd_width 16
#define sbd_height 16
static unsigned char sbd_bits[] = {
    0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0xe2, 0x47, 0xf2, 0x4f, 0xf2, 0x4f,
    0xf2, 0x4f, 0xf2, 0x4f, 0xf2, 0x4f, 0xf2, 0x4f, 0xe2, 0x47, 0xc2, 0x43,
    0x82, 0x41, 0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00 };""").fimg
		self.sbL = self.Fimg("Scrollbar_Left-arorr", """#define sbl_width 16
#define sbl_height 16
static unsigned char sbl_bits[] = {
    0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x02, 0x40, 0xc2, 0x4f, 0xe2, 0x5f,
    0xf2, 0x5f, 0xfa, 0x5f, 0xfa, 0x5f, 0xf2, 0x5f, 0xe2, 0x5f, 0xc2, 0x4f,
    0x02, 0x40, 0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00 };""").fimg
		self.sbR = self.Fimg("Scrollbar_Right-arorr", """#define sbr_width 16
#define sbr_height 16
static unsigned char sbr_bits[] = {
    0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x02, 0x40, 0xf2, 0x43, 0xfa, 0x47,
    0xfa, 0x4f, 0xfa, 0x5f, 0xfa, 0x5f, 0xfa, 0x4f, 0xfa, 0x47, 0xf2, 0x43,
    0x02, 0x40, 0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00 };""").fimg
		self.sbUN = self.sbU(self.clr_sb, self.clr_tw)
		self.sbUP = self.sbU(self.clr_lsb, self.clr_tw)
		self.sbDN = self.sbD(self.clr_sb, self.clr_tw)
		self.sbDP = self.sbD(self.clr_lsb, self.clr_tw)
		self.sbLN = self.sbL(self.clr_sb, self.clr_tw)
		self.sbLP = self.sbL(self.clr_lsb, self.clr_tw)
		self.sbRN = self.sbR(self.clr_sb, self.clr_tw)
		self.sbRP = self.sbR(self.clr_lsb, self.clr_tw)
		self.srcStyle = ttk.Style()
		self.srcStyle.theme_create("deft", parent="alt", settings={
				   "TButton": {
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
						"background": self.clr_bg, 
						"compound": "left"
					}, "map": {"background": [("selected", self.clr_tw)] }
				}, "Vertical.TScrollbar": {
					   "configure": {
						"relief": "flat", 
						"highlightthickness": 0, 
						"borderwidth": 0
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
						"darkbordercolor": self.clr_tw,
						"lightbordercolor": self.clr_tw
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
			}
		)
		self.srcStyle.theme_use("deft")
		self.srcStyle.element_create("Horizontal.Scrollbar.thumb", "image", self.sbHT, border=3, sticky="ew")
		#self.srcStyle.element_create("Horizontal.Scrollbar.grip", "image", sbHG())
		#self.srcStyle.element_create("Horizontal.Scrollbar.trough", "image", sbHR())
		self.srcStyle.element_create("Vertical.Scrollbar.thumb", "image", self.sbVT, border=3, sticky="ns")
		#self.srcStyle.element_create("Vertical.Scrollbar.grip", "image", sbVG())
		#self.srcStyle.element_create("Vertical.Scrollbar.trough", "image", sbVR())
		
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
			title="Открыть фаил",
			filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")]
		)
		if not filepath: return

	# Funcion-image (fimage, fimg)
	class Fimg():
		def __init__(self, fimgName, fimgData):
			self.fimgData = fimgData
			self.fimgName = str(fimgName)
		def fimg(self, fg, bg=None):
			global imgCont
			imgCont += 1
			self.imgCont = imgCont
			img = {
				"name": f"bitmap:{self.fimgName}+cont{self.imgCont}", 
				"imgtype": "bitmap", 
				"data": self.fimgData, 
				"foreground": fg
			}
			if bg == None:
				return tk.Image(**img)
			else:
				return tk.Image(**img, background=bg)



class App():
	# Sourse
	def __init__(self):
		self.version = "1.b3"
		self.source = Source()
		self.mWin = self.source.srcWin
		self.mWin.attributes('-type', 'dock')
		self.mWin.title("ExtPad")
		self.mWin.geometry("400x300")
		self.style = self.source.srcStyle
		self.clr_bg = self.source.clr_bg
		self.clr_tw = self.source.clr_tw
		self.clr_gw = self.source.clr_gw
		self.clr_sb = self.source.clr_sb
		self.clr_dsb = "darkslateblue"
		self.clr_lsb = self.source.clr_lsb
		self.img_win = self.source.img_win(self.clr_gw)
		self.img_min = self.source.img_min(self.clr_gw)
		self.img_max = self.source.img_max(self.clr_gw)
		self.img_close = self.source.img_close(self.clr_gw)
		self.files = {}
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
		self.mbAbout = ttk.Button(self.menuBar, text="About", style="stibl.TButton")
				# Bind this
		self.wmBtn.bind('<Button-1>', self.popWM)
		self.mbFile.bind('<Button-1>', self.popFile)
		self.mbMods.bind('<Button-1>', self.popMods)
		self.mbAbout.bind('<Button-1>', self.popAbout)
				# tkMenus
		self.wmMenu = tk.Menu(self.mWin, tearoff=0)
		self.fMenu = tk.Menu(self.mWin, tearoff=0)
		self.modMenu = tk.Menu(self.mWin, tearoff=0)
		self.aMenu = tk.Menu(self.mWin, tearoff=0)
					# WM menu
		self.wmMenu.add_command(label="Normal window", command=self.withMin)
		self.wmMenu.add_command(label="Zoom window", command=self.withMax)
		self.wmMenu.add_command(label="Quit", command=self.withQuit)
					# File menu
		self.fMenu.add_command(label="Save (cmd test)", command=self.nSave)
		self.fMenu.add_command(label="Open (cmd test)", command=self.nOpen)
		self.fMenu.add_command(label="Close", command=self.nClose)
					# Mods menu
		self.modMenu.add_command(label="Exec mod", command=self.modexec)
					# About menu
		self.aMenu.add_command(label="lulzf", command=self.source.lulzf)
		self.aMenu.add_checkbutton(label="debug", onvalue=True, offvalue=False, variable=self.source.dbg)
			# Pack this
		self.mQuitBtn.pack(fill="both", side="right")
		self.mMaxBtn.pack(fill="both", side="right")
		self.wmBtn.pack(fill="both", side="left")
		self.menuBar.pack(fill="both", side="left")
		self.mbFile.pack(fill="both", side="left")
		self.mbMods.pack(fill="both", side="left")
		self.mbAbout.pack(fill="both", side="left")
		self.mMG.pack(fill="both", expand=True)
		self.tBar.pack(fill="both", side="top")

		# Help-Bar: mainSizegrip, tkhelpButton, mainLabel
		self.hBar = ttk.Frame(self.mWin)
		self.mSG = ttk.Sizegrip(self.hBar)
		self.mLbl = tk.Label(self.hBar, text="Open file with Ctrl-O", anchor="w", padx=3)
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


		def exemple_of_altStream():
			## [AltStream code]
			pass
		self.altstreamf = exemple_of_altStream

	# Funcions
	def forceTk(self): self.mWin.focus_force()
	def pointTk(self, event):
		win_position = [int(coord) for coord in self.mWin.wm_geometry().split('+')[1:]]
		self.source.xTk, self.source.yTk = win_position[0] - event.x_root, win_position[1] - event.y_root
		self.forceTk()
	def moveTk(self, event): 
		if self.source.Tk == "max": self.withMin()
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
	def withQuit(self, event=0):
		self.source.quit()
	def popWM(self, event):
		self.wmMenu.tk_popup(event.x_root, event.y_root, 0)
		self.wmBtn.focus_force()
	def popFile(self, event):
		self.fMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbFile.focus_force()
	def popMods(self, event):
		self.modMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbAbout.focus_force()
	def popAbout(self, event):
		self.aMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbAbout.focus_force()
	def nSel(self, event):
		r = rint(0, 3)
		if   len(self.mNB.tabs()) == 0:
			self.mLbl["text"] = "Open file with Ctrl-O"
		elif self.source.dbg.get() == True:
			self.mLbl["text"] = f'Selected "{str(self.mNB.select())}" tab: {self.mNB.tab(self.mNB.select())}'
		elif len(self.mNB.tabs()) == 1 and r < 3:
			self.mLbl["text"] = "Save file with Ctrl-S"
		elif len(self.mNB.tabs()) == 1 and r == 3:
			self.mLbl["text"] = '"Save as ..." file with Ctrl-Shift-S'
		elif len(self.mNB.tabs()) >= 2:
			self.mLbl["text"] = "Close file with Ctrl-D"
	def nSave(self, event=0):
		if self.mNB.tabs() == ():
			return
		print(f'Save tab {self.mNB.tab(self.mNB.select(), "text")}:')
		nText = self.mWin.nametowidget(self.mNB.select()+".!text")
		tmpText = nText.get("1.0", "end")
		print(tmpText.rstrip("\n"))
		print("END")
	def nOpen(self, event=0):
		# Input path, text
		filepath = input(f"[Print file's name]$ ")
		filetext = input(f"[Print what is'n the file]$ ")
		# Controls
		nPage = ttk.Frame(self.mNB, style="ghost.TFrame", name=f'file:"{filepath.replace(".", "%2E")}"')
		nText = tk.Text(nPage, bd=0, highlightthickness=0, wrap="none", undo=True)
		nSBX = ttk.Scrollbar(nPage, command=nText.xview, orient="horizontal")
		nSBY = ttk.Scrollbar(nPage, command=nText.yview, orient="vertical")
		nText.config(xscrollcommand=nSBX.set, yscrollcommand=nSBY.set)
		nText.insert("1.0", filetext)
		# Grid controls
		nSBX.grid(column=0, row=1, sticky="nsew")
		nSBY.grid(column=1, row=0, sticky="nsew")
		nText.grid(column=0, row=0, sticky="nsew")
		nPage.rowconfigure(0, weight=1)
		nPage.columnconfigure(0, weight=1)
		self.mNB.add(nPage, text=filepath, image=self.img_save)
		self.forceTk()
	def nClose(self, event=0):
		if self.mNB.tabs() == ():
			return
		tmp = list(input(f'[Save tab? (y/n)]$ ').lower())
		if len(tmp) == 0:
			self.nClose()
			return
		if tmp[0] == "y" or tmp[0] == "д":
			self.nSave()
		self.mNB.forget(self.mNB.select())

	def altstream(self):
		self.mWin.after(80, self.altstream)
		self.altstreamf()
	
	def modexec(self, path=None):
		if path == None:
			path = tkfd.askopenfilename(
				title="Открыть фаил",
				filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")]
			)
			if not path: return
		modfile = open(path)
		exec(modfile.read())
		modfile.close()

	# mainloop the mWin
	def init(self):
		self.forceTk()
		self.mWin.bind("<Control-s>", self.nSave)
		self.mWin.bind("<Control-o>", self.nOpen)
		self.mWin.bind("<Control-d>", self.nClose)
		self.mWin.bind("<Control-q>", self.withQuit)
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