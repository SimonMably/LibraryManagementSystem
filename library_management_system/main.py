import time
import os

import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        
        
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
        self.login_panel = wx.Panel(parent=self, id=-1, pos=wx.DefaultPosition, style= wx.BORDER_DEFAULT)
        self.login_panel.SetBackgroundColour(wx.WHITE)
        
        self.lbl_login = wx.StaticText(parent=self.login_panel, pos=wx.DefaultPosition, label="Login", style=wx.ALIGN_CENTER_VERTICAL | wx.ID_UNDERLINE | wx.ST_NO_AUTORESIZE)
        login_title_font = wx.Font(26, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=True)
        self.lbl_login.SetFont(login_title_font)
        
        
        self.lbl_username = wx.StaticText(parent=self.login_panel, pos=wx.DefaultPosition, label="Username", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        
        self.inpt_username = wx.TextCtrl(parent=self.login_panel, id=wx.ID_ANY, value="", style=0)  # ,style=wx.TE_PROCESS_ENTER)
        
        self.lbl_password = wx.StaticText(parent=self.login_panel, pos=wx.DefaultPosition, label="Password", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        
        self.inpt_password = wx.TextCtrl(parent=self.login_panel, id=wx.ID_ANY, value="", style=0)  # ,style=wx.TE_PROCESS_ENTER)
        
        self.btn_login = wx.Button(parent=self.login_panel, id=101, pos=wx.DefaultPosition, label="&Login", size=wx.DefaultSize, style=0, name="btn_login")
        
        self.btn_password_reset = wx.Button(parent=self.login_panel, id=102, pos=wx.DefaultPosition, label="&Reset Password", size=wx.DefaultSize, style=0, name="btn_password_reset")
        
        self.btn_new_user = wx.Button(parent=self.login_panel, id=103, pos=wx.DefaultPosition, label="&New User", size=wx.DefaultSize, style=0, name="btn_new_user")
    
    def bind_events(self):
        """"""
        pass
    
    def create_layout(self):
        """"""
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        login_ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        password_ctrl_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        login_group_sizer = wx.BoxSizer(wx.VERTICAL)
        misc_btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Login Controls Sizers
        login_ctrl_sizer.Add(self.lbl_username, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        login_ctrl_sizer.Add(self.inpt_username, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        
        password_ctrl_sizer.Add(self.lbl_password, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        password_ctrl_sizer.Add(self.inpt_password, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        
        # Main Button Sizer
        main_btn_sizer.Add(self.btn_login, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        main_btn_sizer.Add(self.btn_password_reset, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        
        # Sizer to group above sizers together
        
        login_group_sizer.Add(login_ctrl_sizer, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        login_group_sizer.Add(password_ctrl_sizer, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        login_group_sizer.Add(main_btn_sizer, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        
        # Sizer for Miscellaneous Buttons (Add new user button)
        
        misc_btn_sizer.Add(self.btn_new_user, proportion=1, flag=0, border=0)
        
        # Add Login Label and All Other Sizers to Main Sizer
        
        main_sizer.Add(self.lbl_login, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        main_sizer.Add(login_group_sizer, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        main_sizer.Add(misc_btn_sizer, proportion=1, flag=wx.ALIGN_CENTER, border=0)
        
        self.login_panel.SetSizerAndFit(main_sizer)


class LibManageSys(wx.App):
    def OnInit(self):
        frame = MainFrame(parent=None, id=-1, title="Library Management System")
        self.SetTopWindow(frame)
        frame.Centre()
        frame.Show(True)
        return True
    