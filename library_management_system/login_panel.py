import wx


class LoginPanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.create_ctrls()
        self.bind_events()
        self.create_layout()
    
    def create_ctrls(self):
        """"""
        self.lbl_login = wx.StaticText(parent=self, pos=wx.DefaultPosition, label="Login", style=wx.ALIGN_CENTER_VERTICAL | wx.ID_UNDERLINE | wx.ST_NO_AUTORESIZE)
        login_title_font = wx.Font(26, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=True)
        self.lbl_login.SetFont(login_title_font)
        
        
        self.lbl_username = wx.StaticText(parent=self, pos=wx.DefaultPosition, label="Username", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        
        self.inpt_username = wx.TextCtrl(parent=self, id=wx.ID_ANY, value="", size=(125, -1), style=0)  # ,style=wx.TE_PROCESS_ENTER)
        
        self.lbl_password = wx.StaticText(parent=self, pos=wx.DefaultPosition, label="Password", style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        
        self.inpt_password = wx.TextCtrl(parent=self, id=wx.ID_ANY, value="", size=(150, -1), style=wx.TE_PASSWORD)  # ,style=wx.TE_PROCESS_ENTER)
        
        self.btn_login = wx.Button(parent=self, id=101, pos=wx.DefaultPosition, label="&Login", size=wx.DefaultSize, style=0, name="btn_login")
        
        self.btn_password_reset = wx.Button(parent=self, id=102, pos=wx.DefaultPosition, label="&Reset Password", size=wx.DefaultSize, style=0, name="btn_password_reset")
        
        self.btn_new_user = wx.Button(parent=self, id=103, pos=wx.DefaultPosition, label="&New User", size=wx.DefaultSize, style=0, name="btn_new_user")
    
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
        
        self.SetSizerAndFit(main_sizer)

    def login(self):
        """"""
        # TODO: Create a binding for the login button in the bind_events() function
        pass
    
    def reset_password(self):
        """"""
        # TODO: Create a binding for the reset password button in the bind_events() function
        pass
    
    def create_new_user(self):
        """"""
        # TODO: Create a binding for the new user button in the bind_events() function
        pass
