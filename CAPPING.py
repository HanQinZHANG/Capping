# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1221,299 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"切后序列", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Xulie = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), 0 )
		bSizer2.Add( self.Xulie, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND|wx.SHAPED, 5 )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Exact Mass：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer16.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( fgSizer16, 1, wx.EXPAND, 5 )
		
		fgSizer18 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Avr Mass:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer18.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( fgSizer18, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"5‘-OH：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer3.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer8.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.OH = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		fgSizer4.Add( self.OH, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer8.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"5'-monophosphate：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.MONO = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.MONO, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.asd = wx.StaticText( self, wx.ID_ANY, u"5'-diphosphate：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asd.Wrap( -1 )
		fgSizer10.Add( self.asd, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer11.Add( fgSizer10, 1, wx.EXPAND, 5 )
		
		fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.DI = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer11.Add( self.DI, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer11.Add( fgSizer11, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"5'-triphosphate：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer8.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer16.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.TRI = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		fgSizer9.Add( self.TRI, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer16.Add( fgSizer9, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer111 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer111.SetFlexibleDirection( wx.BOTH )
		fgSizer111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"G-Cap：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer111.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer131.Add( fgSizer111, 1, wx.EXPAND, 5 )
		
		fgSizer13 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.GCAP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.GCAP, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer131.Add( fgSizer13, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer131, 1, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer14 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"Cap 0:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		fgSizer14.Add( self.m_staticText81, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer141.Add( fgSizer14, 1, wx.EXPAND, 5 )
		
		fgSizer15 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CAP0 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.CAP0, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer141.Add( fgSizer15, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer141, 1, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer19 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer19.SetFlexibleDirection( wx.BOTH )
		fgSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Cap 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer19.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer18.Add( fgSizer19, 1, wx.EXPAND, 5 )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CAP1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.CAP1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer18.Add( fgSizer21, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer31 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"5‘-OH：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		fgSizer31.Add( self.m_staticText31, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer81.Add( fgSizer31, 1, wx.EXPAND, 5 )
		
		fgSizer41 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.OH1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		fgSizer41.Add( self.OH1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer81.Add( fgSizer41, 1, wx.EXPAND, 5 )
		
		
		fgSizer12.Add( bSizer81, 1, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer51 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer51.SetFlexibleDirection( wx.BOTH )
		fgSizer51.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"5'-monophosphate：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		fgSizer51.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		
		bSizer101.Add( fgSizer51, 1, wx.EXPAND, 5 )
		
		fgSizer71 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.MONO1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.MONO1, 0, wx.ALL, 5 )
		
		
		bSizer101.Add( fgSizer71, 1, wx.EXPAND, 5 )
		
		
		fgSizer12.Add( bSizer101, 1, wx.EXPAND, 5 )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer101 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer101.SetFlexibleDirection( wx.BOTH )
		fgSizer101.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.asd1 = wx.StaticText( self, wx.ID_ANY, u"5'-diphosphate：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asd1.Wrap( -1 )
		fgSizer101.Add( self.asd1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer111.Add( fgSizer101, 1, wx.EXPAND, 5 )
		
		fgSizer112 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer112.SetFlexibleDirection( wx.BOTH )
		fgSizer112.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.DI1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer112.Add( self.DI1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer111.Add( fgSizer112, 1, wx.EXPAND, 5 )
		
		
		fgSizer12.Add( bSizer111, 1, wx.EXPAND, 5 )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer81 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer81.SetFlexibleDirection( wx.BOTH )
		fgSizer81.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"5'-triphosphate：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )
		fgSizer81.Add( self.m_staticText82, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer161.Add( fgSizer81, 1, wx.EXPAND, 5 )
		
		fgSizer91 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer91.SetFlexibleDirection( wx.BOTH )
		fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.TRI1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		fgSizer91.Add( self.TRI1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer161.Add( fgSizer91, 1, wx.EXPAND, 5 )
		
		
		fgSizer12.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer1311 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1111 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1111.SetFlexibleDirection( wx.BOTH )
		fgSizer1111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"G-Cap：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		fgSizer1111.Add( self.m_staticText71, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1311.Add( fgSizer1111, 1, wx.EXPAND, 5 )
		
		fgSizer131 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer131.SetFlexibleDirection( wx.BOTH )
		fgSizer131.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.GCAP1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer131.Add( self.GCAP1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1311.Add( fgSizer131, 1, wx.EXPAND, 5 )
		
		
		fgSizer12.Add( bSizer1311, 1, wx.EXPAND, 5 )
		
		bSizer1411 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer141 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer141.SetFlexibleDirection( wx.BOTH )
		fgSizer141.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText811 = wx.StaticText( self, wx.ID_ANY, u"Cap 0:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText811.Wrap( -1 )
		fgSizer141.Add( self.m_staticText811, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1411.Add( fgSizer141, 1, wx.EXPAND, 5 )
		
		fgSizer151 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer151.SetFlexibleDirection( wx.BOTH )
		fgSizer151.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CAP01 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer151.Add( self.CAP01, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1411.Add( fgSizer151, 1, wx.EXPAND, 5 )
		
		
		fgSizer12.Add( bSizer1411, 1, wx.EXPAND, 5 )
		
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer191 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer191.SetFlexibleDirection( wx.BOTH )
		fgSizer191.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"Cap 1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		fgSizer191.Add( self.m_staticText131, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer181.Add( fgSizer191, 1, wx.EXPAND, 5 )
		
		fgSizer211 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer211.SetFlexibleDirection( wx.BOTH )
		fgSizer211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.CAP11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer211.Add( self.CAP11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer181.Add( fgSizer211, 1, wx.EXPAND, 5 )
		
		
		fgSizer12.Add( bSizer181, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( fgSizer12, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer47 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer47.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer47, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.JI )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def JI( self, event ):
		event.Skip()
	

