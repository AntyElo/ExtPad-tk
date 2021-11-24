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
		self.dbg.set(False)
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
		self.sbVT = tk.PhotoImage(data="""R0lGODlhEAAQAIABALDE3kaCtCH+CHNiVHJvdWdoACH5BAEKAAEALAAAAAAQABAAAAIgjI95wO28
lAKGSmTtrXx3vWXeNwbieHpp2KktWz1yqRQAOw==""")
		self.sbVH = tk.PhotoImage(data="""R0lGODlhEAAgAKEAAEaCtLDE3kaCtEaCtCH+BHNiVlQAIfkEAQoAAgAsAAAAABAAIAAAAkCUgKlo
Fw/jAwbIG6jDUVsOeWBYjVNpiik6qi0LujHMyTWN2Tl+6T0v8QWBHSJp80LOlDfmzvmDDqVF6vGw
yBoKADs=""")
		self.sbVG = tk.PhotoImage(data="""R0lGODlhCgAOAIAAAEaCtEaCtCH+BHNiVkcAIfkEAQoAAQAsAAAAAAoADgAAAhCEj5nB7f+UlLDW
iY/dLecCADs=""")
		self.sbHT = tk.PhotoImage(data="""R0lGODlhEAAQAIABALDE3kaCtCH+CHNiVHJvdWdoACH5BAEKAAEALAAAAAAQABAAAAIgjI95wO28
lAKGSmTtrXx3vWXeNwbieHpp2KktWz1yqRQAOw==""")
		self.sbHH = tk.PhotoImage(data="""R0lGODlhIAAQAKEAAEaCtLDE3kaCtEaCtCH+BHNiSEgAIfkEAQoAAgAsAAAAACAAEAAAAjOUj6mb
4A+jnE6AgLPevGPnhWIGjiZXnmqQrmbrinDszTR63XKu13yPA9YslKKxwkgqEwUAOw==""")
		self.sbHG = tk.PhotoImage(data="""R0lGODlhDgAKAIAAAEaCtEaCtCH+BHNiSEcAIfkEAQoAAQAsAAAAAA4ACgAAAhcEEoaadr2ekzSy
S3G0FTbtTVvojBiIFQA7""")
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
				   "map": {
						"background": [("", self.clr_bg)]
				}
			}, "Flat.TButton": {
				   "configure": {
						"margins": [0],
						"padding": [3],
						"relief": "flat", 
						"highlightthickness": 0, 
						"borderwidth": 0
				}
			}, "Togle.TButton": {
				   "configure": {
						"margins": [0],
						"padding": [3],
						"relief": "raised", 
						"highlightthickness": 1, 
						"borderwidth": 1,
				}, "map": {
						"relief": [("active", "raised"), ("", "flat")], 
						"foreground": [("active", self.clr_gw), ("", self.clr_sb)], 
						"background": [("active", self.clr_lsb), ("", self.clr_bg)]
				}
			}, "Title.TButton": {
				   "configure": {
						"margins": [0],
						"padding": [3],
						"relief": "flat", 
						"highlightthickness": 0, 
						"borderwidth": 0,
						"font": 10
				}, "map": {
						"foreground": [("active", self.clr_gw), ("", self.clr_gw)], 
						"background": [("active", self.clr_lsb), ("", self.clr_sb)]
				}
			}, "TButton": {
				   "configure": {
						"margins": [0],
						"padding": [3],
						"relief": "raised", 
						"highlightthickness": 1, 
						"borderwidth": 1,
						"background": self.clr_lsb
				}, "map": {
						"foreground": [("active", self.clr_gw), ("", self.clr_gw)], 
						"background": [("active", self.clr_lsb), ("", self.clr_sb)]
				}
			}, "CNotebook": {
				   "configure": {
						"borderwidth": 0, 
						"tabmargins": [3, 4, 2, 0], 
						#"tabposition": "wn"
				}
			}, "CNotebook.Tab": {
				   "configure": {
						"borderwidth": 0, 
						"padding": [5, 3]
				}, "map": {
						"background": [("selected", self.clr_tw), ("", self.clr_bg)] 
				}
			}, "Vertical.TScrollbar": {
				   "configure": {
						"relief": "flat",
						"highlightthickness": 0, 
						"borderwidth": 0,
						"troughborderwidth": 0,
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
		self.srcStyle.element_create("Horizontal.Scrollbar.trough", "image", self.sbHT, border=2, sticky="ew")
		self.srcStyle.element_create("Horizontal.Scrollbar.thumb", "image", self.sbHH, border=1, sticky="ew")
		self.srcStyle.element_create("Horizontal.Scrollbar.grip", "image", self.sbHG)
		self.srcStyle.element_create("Vertical.Scrollbar.trough", "image", self.sbVT, border=2, sticky="ns")
		self.srcStyle.element_create("Vertical.Scrollbar.thumb", "image", self.sbVH, border=1, sticky="ns")
		self.srcStyle.element_create("Vertical.Scrollbar.grip", "image", self.sbVG)
		
		self.srcStyle.element_create("Scrollbar.uparrow", "image", self.sbUN, ("pressed", self.sbUP), sticky="")
		self.srcStyle.element_create("Scrollbar.downarrow", "image", self.sbDN, ("pressed", self.sbDP), sticky="")
		self.srcStyle.element_create("Scrollbar.leftarrow", "image", self.sbLN, ("pressed", self.sbLP), sticky="")
		self.srcStyle.element_create("Scrollbar.rightarrow", "image", self.sbRN, ("pressed", self.sbRP), sticky="")

	# Funcions
	def quit(self): self.srcWin.destroy()
	def lulzf(self): print("Source.lulzf(): LULZ!!!")
	def cfgpath_set(self, inp=None):
		global cfgPath
		if inp == None: cfgPath = tkfd.askopenfilename(filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")])
		else:
			cfgPath = str(inp)
			self.cfgPath = str(inp)
	def cfg_update(self):
		if self.cfgPath == "": return
		else:
			tmp = open(cfgPath, "x")
			self.cfgFile = tmp.read()
			tmp.close()

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


class CNotebook(ttk.Notebook): # With "CustomNotebook" and TNotebook
	__initialized = False
	def __init__(self, *args, **kwargs):
		self.style = ttk.Style()
		self.clr_bg = "#b7b7b7"
		self.clr_tw = "#ffffff"
		if not self.__initialized:
			self.__initialize_custom_style()
			self.__inititialized = True

		kwargs["style"] = "CNotebook"
		self.style.theme_use("deft")
		ttk.Notebook.__init__(self, *args, **kwargs)

		self._active = None

		self.bind("<ButtonPress-1>", self.on_close_press, True)
		self.bind("<ButtonRelease-1>", self.on_close_release)

	def on_close_press(self, event):
		element = self.identify(event.x, event.y)

		if "close" in element:
			index = self.index("@%d,%d" % (event.x, event.y))
			self.state(['pressed'])
			self._active = index
			return "break"

	def on_close_release(self, event):
		if not self.instate(['pressed']):
			return

		element =  self.identify(event.x, event.y)
		if "close" not in element:
			# user moved the mouse off of the close button
			return

		index = self.index("@%d,%d" % (event.x, event.y))

		if self._active == index:
			self.event_generate("<<NotebookTabClosed>>")

		self.state(["!pressed"])
		self._active = None

	def __initialize_custom_style(self):
		style = self.style
		self.img_close = tk.Image("bitmap", "img_close", data = '''#define close_width 16
#define close_height 16
static unsigned char close_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0x0c, 0x30, 0x1c, 0x38, 0x38, 0x1c, 0x70, 0x0e,
    0xe0, 0x07, 0xc0, 0x03, 0xc0, 0x03, 0xe0, 0x07, 0x70, 0x0e, 0x38, 0x1c,
    0x1c, 0x38, 0x0c, 0x30, 0x00, 0x00, 0x00, 0x00 };''', foreground = "steelblue")
		self.img_closeact = tk.Image("bitmap", "img_closeactive", data='''#define close_width 16
#define close_height 16
static unsigned char close_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0x0c, 0x30, 0x1c, 0x38, 0x38, 0x1c, 0x70, 0x0e,
    0xe0, 0x07, 0xc0, 0x03, 0xc0, 0x03, 0xe0, 0x07, 0x70, 0x0e, 0x38, 0x1c,
    0x1c, 0x38, 0x0c, 0x30, 0x00, 0x00, 0x00, 0x00 };''', foreground="lightsteelblue")
		self.img_closepr = tk.Image("bitmap", "img_closepressed", data='''#define close_width 16
#define close_height 16
static unsigned char close_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0x0c, 0x30, 0x1c, 0x38, 0x38, 0x1c, 0x70, 0x0e,
    0xe0, 0x07, 0xc0, 0x03, 0xc0, 0x03, 0xe0, 0x07, 0x70, 0x0e, 0x38, 0x1c,
    0x1c, 0x38, 0x0c, 0x30, 0x00, 0x00, 0x00, 0x00 };''', foreground="darkslateblue")

		style.theme_settings(style.theme_use(), {
			   "CNotebook": {
				"layout": [
					("CNotebook.client", {"sticky": "nswe"})
				]
			}, "CNotebook.Tab": {
				"layout": [
					("CNotebook.tab", {"sticky": "nswe", "children": [
						("CNotebook.padding", {"side": "top", "sticky": "nswe", "children": [
							("CNotebook.focus", {"side": "top", "sticky": "nswe", "children": [
									("CNotebook.label", {"side": "left", "sticky": ''}),
									("CNotebook.close", {"side": "left", "sticky": ''}),
							]})
						]})
					]})
				]
			}
		})
		style.element_create(
			"close", "image", "img_close",
			("active", "pressed", "!disabled", "img_closepressed"),
			("active", "!disabled", "img_closeactive"), 
			border=8, sticky=""
		)


class App():
	# Sourse
	def __init__(self):
		self.version = "1r0"
		self.vkw = {
			"codename": "argentum", # Arch
			"major": 1, # Every update
			"type": "release", # alpha/beta/candidate/release
			"minor": 0 # Is a path of major
		}
		self.vpr = str(self.vkw["major"]) + "." + str(self.vkw["minor"]) + " " + self.vkw["type"].title()
		self.source = Source()
		self.mWin = self.source.srcWin
		if sys.platform == "win32": self.mWin.overrideredirect(True)
		else: self.mWin.attributes('-type', "dock")
		self.mWin.title("ExtPad")
		self.mWin.geometry("400x300")
		self.mWin["takefocus"] = True
		self.style = self.source.srcStyle
		self.nBuffer = ""
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
		self.istopTk = tk.BooleanVar()
		self.istopTk.set(True)
		self.mLblCheck = -1
		self.style.map("ghost.TFrame", background = [("", self.clr_tw)])

		# Title-Bar: wmButton, mainLabel, mainLabel
		self.tBar = tk.Frame(self.mWin, bg=self.clr_dsb, bd=1)
		self.wmBtn = ttk.Button(self.tBar, image=self.img_win, style="Title.TButton")
		self.mMG = tk.Canvas(self.tBar, bg=self.clr_sb, highlightthickness=0, height=0)
		self.mMG.bind('<Button-1>', self.pointTk)
		self.mMG.bind('<B1-Motion>', self.moveTk)
		self.mMinBtn  = ttk.Button(self.tBar, style="Title.TButton", image=self.img_min,   command=self.withMin)
		self.mMaxBtn  = ttk.Button(self.tBar, style="Title.TButton", image=self.img_max,   command=self.withMax)
		self.mQuitBtn = ttk.Button(self.tBar, style="Title.TButton", image=self.img_close, command=self.withQuit)
			# Menu
				# Controls
		self.menuBar = tk.Frame(self.tBar, bg=self.clr_dsb)
		self.mbFile = ttk.Button(self.menuBar, text="File", style="Title.TButton")
		self.mbEdit = ttk.Button(self.menuBar, text="Edit", style="Title.TButton")
		self.mbView = ttk.Button(self.menuBar, text="View", style="Title.TButton")
		self.mbMods = ttk.Button(self.menuBar, text="Mods", style="Title.TButton")
		self.mbHelp = ttk.Button(self.menuBar, text="Help", style="Title.TButton")
				# Bind this
		self.wmBtn.bind('<Button-1>', self.popWM)
		self.mbFile.bind('<Button-1>', self.popFile)
		self.mbEdit.bind('<Button-1>', self.popEdit)
		self.mbView.bind('<Button-1>', self.popView)
		self.mbMods.bind('<Button-1>', self.popMods)
		self.mbHelp.bind('<Button-1>', self.popHelp)
				# Menus
		self.wmMenu = tk.Menu(self.mWin, tearoff=0) # WM
		self.fMenu = tk.Menu(self.mWin, tearoff=0) # File
		self.eMenu = tk.Menu(self.mWin, tearoff=0) # Edit
		self.vMenu = tk.Menu(self.mWin, tearoff=0) # View
		self.modMenu = tk.Menu(self.mWin, tearoff=0) # Mods
		self.hMenu = tk.Menu(self.mWin, tearoff=0) # Help

		self.wmMenu.add_command(label="Normal window", command=self.withMin)
		self.wmMenu.add_command(label="Zoom window", command=self.withMax)
		self.wmMenu.add_checkbutton(label="Always at the top", variable=self.istopTk, offvalue=False, onvalue=True, command=self.topTk)
		self.wmMenu.add_command(label="Quit", accelerator="Ctrl-Q", command=self.withQuit)

		self.fMenu.add_command(label="Save", accelerator="Ctrl-S", command=self.nSave)
		self.fMenu.add_command(label="Save as...", accelerator="Ctrl-Shift-S", command=self.nSaveas)
		self.fMenu.add_command(label="Open", accelerator="Ctrl-O", command=self.nOpen)
		self.fMenu.add_command(label="New", accelerator="Ctrl-N", command=self.nNew)
		self.fMenu.add_command(label="Close", accelerator="Ctrl-Shift-D", command=self.nClose)

		self.eMenu.add_command(label="Copy", accelerator="Ctrl-C", command=self.eCopy)
		self.eMenu.add_command(label="Paste", accelerator="Ctrl-V", command=self.ePaste)
		self.eMenu.add_command(label="Cut", accelerator="Ctrl-X", command=self.eCut)

		self.vMenu.add_command(label="[View]", command=self.source.lulzf)

		self.modMenu.add_command(label="Exec", command=self.modexec)

		self.hMenu.add_command(label="About", accelerator="F1", command=self.source.lulzf)
			# Pack this
		self.mQuitBtn.pack(fill="both", side="right")
		self.mMaxBtn.pack(fill="both", side="right")
		self.wmBtn.pack(fill="both", side="left")
		self.menuBar.pack(fill="both", side="left")
		self.mbFile.pack(fill="both", side="left")
		self.mbEdit.pack(fill="both", side="left")
		#self.mbView.pack(fill="both", side="left")
		self.mbMods.pack(fill="both", side="left")
		self.mbHelp.pack(fill="both", side="left")
		self.mMG.pack(fill="both", expand=True)
		self.tBar.pack(fill="both", side="top")

		# Help-Bar: mainSizegrip, tkhelpButton, mainLabel
		self.hBar = ttk.Frame(self.mWin)
		self.mSG = ttk.Sizegrip(self.hBar)
		self.mLbl = ttk.Label(self.hBar, text=f"Hello in ExtPad {self.vpr}")
			# Pack this
		self.mSG.pack(fill="both", side="right")
		self.mLbl.pack(fill="both", expand=True)
		self.hBar.pack(fill="both", side="bottom")

		# mainNoteBook
		self.mNB = CNotebook(self.mWin, height=0)
		self.iif = ttk.Frame(self.mNB)
		self.iil = ttk.Label(self.iif)
		self.iil.pack(fill="both")
			# Pack this
		self.mNB.bind("<<NotebookTabChanged>>", self.nSel)
		self.mNB.bind("<<NotebookTabClosed>>", lambda event: self.nClose())
		self.mNB.pack(fill="both", expand=True)

	# Funcions
		# Tk
	def forceTk(self): self.mWin.focus_force()
	def topTk(self, bl=None): 
		if bl == None: bl = self.istopTk.get()
		self.mWin.attributes("-topmost", bl)
	def pointTk(self, event):
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
	def popEdit(self, event):
		self.eMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbEdit.focus_force()
	def popView(self, event):
		self.vMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbView.focus_force()
	def popMods(self, event):
		self.modMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbMods.focus_force()
	def popHelp(self, event):
		self.hMenu.tk_popup(event.x_root, event.y_root, 0)
		self.mbHelp.focus_force()
		# Notebook (aka n-prefixed)
	def get_nText(self): return self.mWin.nametowidget(self.mNB.select()+".!text")
	def nSel(self, event):
		if   len(self.mNB.tabs()) == 0:
			self.mLbl["text"] = f"Hello in ExtPad {self.vpr}"
			self.mLblCheck = -1
		elif self.source.dbg.get() == True:
			self.mLbl["text"] = f'Selected "{str(self.mNB.select())}" tab: {self.mNB.tab(self.mNB.select())}'
			self.mLblCheck = 30
		else: self.mLblCheck = 0
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
		nText.edit_reset()
		nText.edit_modified(0)
		nText.bind("<Button-3>", self.popEdit)
		# Grid controls
		nSBX.grid(column=0, row=1, sticky="nsew")
		nSBY.grid(column=1, row=0, sticky="nsew")
		nText.grid(column=0, row=0, sticky="nsew")
		nPage.rowconfigure(0, weight=1)
		nPage.columnconfigure(0, weight=1)
		self.mNB.add(nPage, text=name)
	def nSaveas(self):
		if self.mNB.tabs() == (): return
		path = tkfd.asksaveasfilename(
			title="Save as",
			defaultextension=".txt", 
			filetypes=[("All formats", "*.*"), ("Text file", "*.txt"), ("Python file", "*.py")]
		)
		self.forceTk()
		if not path: return
		try:
			nText = self.get_nText().edit_reset()
			nText.edit_modified(0)
			nfile = open(path, "w")
			nfile.write(nText.get("1.0", "end").rstrip("\n"))
			nfile.close()
		except: print("AppErorr: Can't save file")
	def nSave(self):
		if self.mNB.tabs() == (): return
		nText = self.get_nText().edit_modified(0)
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
		nText.bind("<Button-3>", self.popEdit)
		# Grid controls
		nSBX.grid(column=0, row=1, sticky="nsew")
		nSBY.grid(column=1, row=0, sticky="nsew")
		nText.grid(column=0, row=0, sticky="nsew")
		nPage.rowconfigure(0, weight=1)
		nPage.columnconfigure(0, weight=1)
		self.mNB.add(nPage, text=name)
	def nClose(self):
		if self.mNB.tabs() == (): return
		seltype = self.mNB.select().split(":")[0].split(".")[-1]
		if seltype == "file":
			nText = self.get_nText()
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
	def eCopy(self): 
		try: self.nBuffer = self.get_nText().selection_get()
		except: print("AppError: Can't copy")
	def ePaste(self): 
		try: self.get_nText().insert("insert", self.nBuffer)
		except: print("AppError: Can't paste")
	def eCut(self):
		try:
			nText = self.get_nText()
			self.nBuffer = nText.selection_get()
			nText.delete(tk.SEL_FIRST, tk.SEL_LAST)
		except: print("AppError: Can't cut")

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
			if not nText.edit_modified():
				self.mLbl["text"] = f"[File] Line: {insLine}/{endLine}  Col: {insCol}/{endCol}  Path: {path}"
			else:
				self.mLbl["text"] = f"[File*] Line: {insLine}/{endLine}  Col: {insCol}/{endCol}  Path: {path}"
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
		if sys.platform != "win32": self.mWin.after_idle(lambda: self.mWin.attributes('-type', "normal"))
		self.topTk(True)
		self.mWin.mainloop()


if __name__ == "__main__": 
	app = App()
	app.init()
