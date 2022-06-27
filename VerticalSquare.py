# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.0-4761b0c)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWindowAbstract
###########################################################################

class MainWindowAbstract ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Vertical Square Check", pos = wx.DefaultPosition, size = wx.Size( 300,250 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer26.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer26, 0, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Import .log file :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer6.Add( self.m_staticText21, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer6, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_FilePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select the .log File to Import", u"*.log", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST )
		bSizer7.Add( self.m_FilePicker, 1, wx.ALL, 5 )


		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer24.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer24, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Create Plot and Output File", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer25.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer25, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		sb_Max = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText16 = wx.StaticText( sb_Max.GetStaticBox(), wx.ID_ANY, u"MAX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer38.Add( self.m_staticText16, 0, wx.ALL, 5 )


		sb_Max.Add( bSizer38, 0, wx.ALIGN_CENTER, 5 )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline9 = wx.StaticLine( sb_Max.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer39.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )


		sb_Max.Add( bSizer39, 1, wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		self.m_MAX_VAL = wx.StaticText( sb_Max.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_MAX_VAL.Wrap( -1 )

		self.m_MAX_VAL.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer40.Add( self.m_MAX_VAL, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		sb_Max.Add( bSizer40, 1, wx.EXPAND, 5 )


		bSizer3.Add( sb_Max, 1, wx.EXPAND, 5 )

		sb_Max1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		bSizer381 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText161 = wx.StaticText( sb_Max1.GetStaticBox(), wx.ID_ANY, u"MIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		self.m_staticText161.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer381.Add( self.m_staticText161, 0, wx.ALL, 5 )


		sb_Max1.Add( bSizer381, 0, wx.ALIGN_CENTER, 5 )

		bSizer391 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline91 = wx.StaticLine( sb_Max1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer391.Add( self.m_staticline91, 0, wx.EXPAND |wx.ALL, 5 )


		sb_Max1.Add( bSizer391, 1, wx.EXPAND, 5 )

		bSizer401 = wx.BoxSizer( wx.VERTICAL )

		self.m_MIN_VAL = wx.StaticText( sb_Max1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_MIN_VAL.Wrap( -1 )

		self.m_MIN_VAL.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer401.Add( self.m_MIN_VAL, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		sb_Max1.Add( bSizer401, 1, wx.EXPAND, 5 )


		bSizer3.Add( sb_Max1, 1, wx.EXPAND, 5 )

		sb_Max2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		bSizer382 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText162 = wx.StaticText( sb_Max2.GetStaticBox(), wx.ID_ANY, u"DELTA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )

		self.m_staticText162.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer382.Add( self.m_staticText162, 0, wx.ALL, 5 )


		sb_Max2.Add( bSizer382, 0, wx.ALIGN_CENTER, 5 )

		bSizer392 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline92 = wx.StaticLine( sb_Max2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer392.Add( self.m_staticline92, 0, wx.EXPAND |wx.ALL, 5 )


		sb_Max2.Add( bSizer392, 1, wx.EXPAND, 5 )

		bs_Delta = wx.BoxSizer( wx.VERTICAL )

		self.m_DELTA_VAL = wx.StaticText( sb_Max2.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_DELTA_VAL.Wrap( -1 )

		self.m_DELTA_VAL.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_DELTA_VAL.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bs_Delta.Add( self.m_DELTA_VAL, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		sb_Max2.Add( bs_Delta, 1, wx.EXPAND, 5 )


		bSizer3.Add( sb_Max2, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit"+ u"\t" + u"CTRL+X", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.onCreatePlot )
		self.Bind( wx.EVT_MENU, self.onExit, id = self.m_menuItem1.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def onCreatePlot( self, event ):
		event.Skip()

	def onExit( self, event ):
		event.Skip()


