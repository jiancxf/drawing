# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"抽签助手", pos = wx.DefaultPosition, size = wx.Size( 1200,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		main_layout = wx.BoxSizer( wx.VERTICAL )

		self.menu_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.menu_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		menu_layout = wx.FlexGridSizer( 1, 3, 0, 0 )
		menu_layout.SetFlexibleDirection( wx.BOTH )
		menu_layout.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		menu_layout.SetMinSize( wx.Size( 800,-1 ) )
		self.main_btn = wx.Button( self.menu_panel, wx.ID_ANY, u"抽签", wx.DefaultPosition, wx.DefaultSize, 0 )
		menu_layout.Add( self.main_btn, 0, wx.ALL, 5 )

		self.data_btn = wx.Button( self.menu_panel, wx.ID_ANY, u"数据集", wx.DefaultPosition, wx.DefaultSize, 0 )
		menu_layout.Add( self.data_btn, 0, wx.ALL, 5 )

		self.log_btn = wx.Button( self.menu_panel, wx.ID_ANY, u"抽签记录", wx.DefaultPosition, wx.DefaultSize, 0 )
		menu_layout.Add( self.log_btn, 0, wx.ALL, 5 )


		self.menu_panel.SetSizer( menu_layout )
		self.menu_panel.Layout()
		menu_layout.Fit( self.menu_panel )
		main_layout.Add( self.menu_panel, 0, wx.EXPAND |wx.ALL, 5 )

		content_layout = wx.BoxSizer( wx.VERTICAL )

		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		content_layout.Add( self.main_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.data_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.data_panel.Hide()

		data_layout = wx.BoxSizer( wx.VERTICAL )


		data_layout.Add( ( 12, 0), 0, wx.EXPAND, 5 )

		data_prm_layout = wx.FlexGridSizer( 0, 6, 0, 0 )
		data_prm_layout.SetFlexibleDirection( wx.BOTH )
		data_prm_layout.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		data_prm_layout.Add( ( 10, 0), 0, wx.EXPAND, 5 )

		table_select_comboChoices = []
		self.table_select_combo = wx.ComboBox( self.data_panel, wx.ID_ANY, u"请选择表格", wx.DefaultPosition, wx.Size( 150,-1 ), table_select_comboChoices, wx.CB_DROPDOWN )
		data_prm_layout.Add( self.table_select_combo, 0, wx.ALL, 5 )

		self.table_check_btn = wx.Button( self.data_panel, wx.ID_ANY, u"查看", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.table_check_btn.SetMinSize( wx.Size( 60,-1 ) )

		data_prm_layout.Add( self.table_check_btn, 0, wx.ALL, 5 )

		self.import_tb_btn = wx.Button( self.data_panel, wx.ID_ANY, u"导入数据表", wx.DefaultPosition, wx.DefaultSize, 0 )
		data_prm_layout.Add( self.import_tb_btn, 0, wx.ALL, 5 )

		self.refresh_grid_btn = wx.Button( self.data_panel, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
		data_prm_layout.Add( self.refresh_grid_btn, 0, wx.ALL, 5 )


		data_prm_layout.Add( ( 0, 0), 0, 0, 5 )


		data_layout.Add( data_prm_layout, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.data_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		data_layout.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		table_layout = wx.FlexGridSizer( 0, 3, 0, 0 )
		table_layout.SetFlexibleDirection( wx.BOTH )
		table_layout.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		table_layout.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.table_opt_panel = wx.Panel( self.data_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1160,-1 ), wx.TAB_TRAVERSAL )
		self.table_opt_panel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.table_opt_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		table_opt_inner_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		table_opt_inner_sizer.SetFlexibleDirection( wx.BOTH )
		table_opt_inner_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.add_table_data_btn = wx.Button( self.table_opt_panel, wx.ID_ANY, u"添加数据", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.add_table_data_btn.Enable( False )

		table_opt_inner_sizer.Add( self.add_table_data_btn, 0, wx.ALL, 5 )

		self.delete_table_data_btn = wx.Button( self.table_opt_panel, wx.ID_ANY, u"删除整行", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.delete_table_data_btn.Enable( False )

		table_opt_inner_sizer.Add( self.delete_table_data_btn, 0, wx.ALL, 5 )

		self.update_table_btn = wx.Button( self.table_opt_panel, wx.ID_ANY, u"确认修改", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.update_table_btn.Enable( False )

		table_opt_inner_sizer.Add( self.update_table_btn, 0, wx.ALL, 5 )


		self.table_opt_panel.SetSizer( table_opt_inner_sizer )
		self.table_opt_panel.Layout()
		table_layout.Add( self.table_opt_panel, 1, wx.EXPAND |wx.ALL, 5 )


		table_layout.Add( ( 0, 0), 0, wx.EXPAND, 5 )


		table_layout.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.table_grid = wx.grid.Grid( self.data_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.table_grid.CreateGrid( 0, 0 )
		self.table_grid.EnableEditing( True )
		self.table_grid.EnableGridLines( True )
		self.table_grid.EnableDragGridSize( False )
		self.table_grid.SetMargins( 0, 0 )

		# Columns
		self.table_grid.EnableDragColMove( False )
		self.table_grid.EnableDragColSize( True )
		self.table_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.table_grid.EnableDragRowSize( True )
		self.table_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.table_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.table_grid.SetMinSize( wx.Size( 1150,560 ) )

		table_layout.Add( self.table_grid, 0, wx.ALL, 5 )


		table_layout.Add( ( 0, 0), 0, wx.EXPAND, 5 )


		table_layout.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.pagation_panel = wx.Panel( self.data_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pagation_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		pageButtonSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		pageButtonSizer.SetFlexibleDirection( wx.BOTH )
		pageButtonSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.grid_pre_page_btn = wx.Button( self.pagation_panel, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.grid_pre_page_btn.Enable( False )

		pageButtonSizer.Add( self.grid_pre_page_btn, 0, wx.ALL, 5 )

		self.grid_next_page_btn = wx.Button( self.pagation_panel, wx.ID_ANY, u"下一页", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.grid_next_page_btn.Enable( False )

		pageButtonSizer.Add( self.grid_next_page_btn, 0, wx.ALL, 5 )


		self.pagation_panel.SetSizer( pageButtonSizer )
		self.pagation_panel.Layout()
		pageButtonSizer.Fit( self.pagation_panel )
		table_layout.Add( self.pagation_panel, 1, wx.EXPAND |wx.ALL, 5 )


		table_layout.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		data_layout.Add( table_layout, 0, wx.ALIGN_CENTER, 5 )


		self.data_panel.SetSizer( data_layout )
		self.data_panel.Layout()
		data_layout.Fit( self.data_panel )
		content_layout.Add( self.data_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.log_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.log_panel.Hide()

		content_layout.Add( self.log_panel, 0, wx.EXPAND |wx.ALL, 5 )


		main_layout.Add( content_layout, 1, wx.EXPAND, 5 )


		self.SetSizer( main_layout )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.main_btn.Bind( wx.EVT_BUTTON, self.show_main_panel )
		self.data_btn.Bind( wx.EVT_BUTTON, self.show_data_panel )
		self.log_btn.Bind( wx.EVT_BUTTON, self.show_log_panel )
		self.table_select_combo.Bind( wx.EVT_COMBOBOX, self.choose_table )
		self.table_check_btn.Bind( wx.EVT_BUTTON, self.load_table_data )
		self.import_tb_btn.Bind( wx.EVT_BUTTON, self.show_import_dialog )
		self.refresh_grid_btn.Bind( wx.EVT_BUTTON, self.refresh_grid_table )
		self.add_table_data_btn.Bind( wx.EVT_BUTTON, self.add_table_data )
		self.delete_table_data_btn.Bind( wx.EVT_BUTTON, self.delete_table_data )
		self.update_table_btn.Bind( wx.EVT_BUTTON, self.update_table_data )
		self.table_grid.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.on_table_data_change )
		self.table_grid.Bind( wx.grid.EVT_GRID_RANGE_SELECT, self.on_table_data_select )
		self.table_grid.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_table_data_select )
		self.grid_pre_page_btn.Bind( wx.EVT_BUTTON, self.grid_pre_page )
		self.grid_next_page_btn.Bind( wx.EVT_BUTTON, self.grid_next_page )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def show_main_panel( self, event ):
		event.Skip()

	def show_data_panel( self, event ):
		event.Skip()

	def show_log_panel( self, event ):
		event.Skip()

	def choose_table( self, event ):
		event.Skip()

	def load_table_data( self, event ):
		event.Skip()

	def show_import_dialog( self, event ):
		event.Skip()

	def refresh_grid_table( self, event ):
		event.Skip()

	def add_table_data( self, event ):
		event.Skip()

	def delete_table_data( self, event ):
		event.Skip()

	def update_table_data( self, event ):
		event.Skip()

	def on_table_data_change( self, event ):
		event.Skip()

	def on_table_data_select( self, event ):
		event.Skip()


	def grid_pre_page( self, event ):
		event.Skip()

	def grid_next_page( self, event ):
		event.Skip()


###########################################################################
## Class import_dialog
###########################################################################

class import_dialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"导入数据", pos = wx.DefaultPosition, size = wx.Size( 309,146 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )
		self.Hide()

		impt_main_layout = wx.BoxSizer( wx.VERTICAL )


		impt_main_layout.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.file_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.xlsx;*.xls;*.xlsm;", wx.DefaultPosition, wx.Size( 260,-1 ), wx.FLP_DEFAULT_STYLE )
		impt_main_layout.Add( self.file_picker, 0, wx.ALIGN_CENTER, 5 )


		impt_main_layout.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		impt_btn_layout = wx.FlexGridSizer( 0, 2, 0, 0 )
		impt_btn_layout.SetFlexibleDirection( wx.BOTH )
		impt_btn_layout.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.impt_confirm_btn = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.impt_confirm_btn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		impt_btn_layout.Add( self.impt_confirm_btn, 0, wx.ALL, 5 )

		self.impt_cancel_btn = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		impt_btn_layout.Add( self.impt_cancel_btn, 0, wx.ALL, 5 )


		impt_main_layout.Add( impt_btn_layout, 0, wx.ALIGN_CENTER, 5 )


		self.SetSizer( impt_main_layout )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.file_picker.Bind( wx.EVT_FILEPICKER_CHANGED, self.select_data_source )
		self.impt_confirm_btn.Bind( wx.EVT_BUTTON, self.import_data )
		self.impt_cancel_btn.Bind( wx.EVT_BUTTON, self.cancel_import_data )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def select_data_source( self, event ):
		event.Skip()

	def import_data( self, event ):
		event.Skip()

	def cancel_import_data( self, event ):
		event.Skip()


