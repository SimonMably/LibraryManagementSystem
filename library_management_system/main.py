import time
import os

import wx
from library_management_system import login_panel

from library_management_system.login_panel import LoginPanel

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        # TODO: Finish create_ctrls() and create_layout() and test to see if login_panel works
        
        
        self.set_properties()
        self.make_menu_bar()
        self.create_ctrls()
        self.bind_events()
        self.create_layout()
        
        # TODO: Find a way for users (library staff) to log in
        # TODO: When user logs in, switch to different panel
        # NOTICE: For switching between panels, see answerin  https://stackoverflow.com/questions/53736862/wxpython-clear-widgets-and-create-new-layout
        
        # NOTICE: Possible other windows, call here
    
    def set_properties(self):
        """"""
        self.SetIcon(wx.Icon("library.ico"))
        self.SetSize((1500, 800))
        self.SetMinSize((1500, 800))
        self.SetMaxSize((1500, 800))
        # self.Maximize()
    
    def make_menu_bar(self):
        """"""
        menu_bar = wx.MenuBar()
        
        self.menu = wx.Menu()
        
        self.menu.Append(101, item="&Find Book")
        self.menu.AppendSeparator()
        
        menu_bar.Append(self.menu, title="&Menu")
        self.SetMenuBar(menu_bar)
      
    def create_ctrls(self):
        """"""
        self.main_panel = wx.Panel(parent=self, id=-1, pos=wx.DefaultPosition, style=wx.BORDER_DEFAULT)
        
        self.login_pnl = LoginPanel(self.main_panel)
        self.login_pnl.SetBackgroundColour(wx.WHITE)
        
    
    def bind_events(self):
        """"""
        pass
    
    def create_layout(self):
        """"""
        general_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        
        general_sizer.Add(self.login_pnl, proportion=1, flag=wx.EXPAND)
        
        self.main_panel.SetSizerAndFit(general_sizer)


class LibManageSys(wx.App):
    def OnInit(self):
        frame = MainFrame(parent=None, id=-1, title="Library Management System")
        self.SetTopWindow(frame)
        frame.Centre()
        frame.Show(True)
        return True
    