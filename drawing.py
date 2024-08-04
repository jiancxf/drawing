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
		mainSizer = wx.BoxSizer( wx.VERTICAL )

		self.title_panel = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		title_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		title_sizer.SetFlexibleDirection( wx.BOTH )
		title_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		self.title_panel.SetSizer( title_sizer )
		self.title_panel.Layout()
		title_sizer.Fit( self.title_panel )
		mainSizer.Add( self.title_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.selection_panel = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		selection_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		selection_sizer.SetFlexibleDirection( wx.BOTH )
		selection_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		selection_sizer.Add( ( 30, 0), 0, wx.EXPAND, 5 )

		drawing_table_comboChoices = []
		self.drawing_table_combo = wx.ComboBox( self.selection_panel, wx.ID_ANY, u"选择数据表", wx.DefaultPosition, wx.Size( 200,-1 ), drawing_table_comboChoices, 0 )
		selection_sizer.Add( self.drawing_table_combo, 0, wx.ALL, 5 )

		self.confirm_draw_table_btn = wx.Button( self.selection_panel, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0 )
		selection_sizer.Add( self.confirm_draw_table_btn, 0, wx.ALL, 5 )


		selection_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.selection_panel.SetSizer( selection_sizer )
		self.selection_panel.Layout()
		selection_sizer.Fit( self.selection_panel )
		mainSizer.Add( self.selection_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.basic_condition_panel = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		basic_condition_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		basic_condition_sizer.SetFlexibleDirection( wx.BOTH )
		basic_condition_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		basic_condition_sizer.Add( ( 35, 0), 1, wx.EXPAND, 5 )

		self.drawing_num_label = wx.StaticText( self.basic_condition_panel, wx.ID_ANY, u"选择抽取数量: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.drawing_num_label.Wrap( -1 )

		basic_condition_sizer.Add( self.drawing_num_label, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.drawing_num_ctrl = wx.SpinCtrl( self.basic_condition_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		basic_condition_sizer.Add( self.drawing_num_ctrl, 0, wx.ALL, 5 )


		basic_condition_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.basic_condition_panel.SetSizer( basic_condition_sizer )
		self.basic_condition_panel.Layout()
		basic_condition_sizer.Fit( self.basic_condition_panel )
		mainSizer.Add( self.basic_condition_panel, 0, wx.EXPAND |wx.ALL, 5 )

		self.adv_condition_panel = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.adv_condition_panel.Hide()

		drawing_sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		drawing_sizer.SetFlexibleDirection( wx.BOTH )
		drawing_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		self.adv_condition_panel.SetSizer( drawing_sizer )
		self.adv_condition_panel.Layout()
		drawing_sizer.Fit( self.adv_condition_panel )
		mainSizer.Add( self.adv_condition_panel, 1, wx.EXPAND |wx.ALL, 5 )

		self.date_view_panel = wx.Panel( self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		date_view_sizer = wx.FlexGridSizer( 0, 5, 0, 0 )
		date_view_sizer.SetFlexibleDirection( wx.BOTH )
		date_view_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		date_view_sizer.Add( ( 30, 0), 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.data_view_title = wx.StaticText( self.date_view_panel, wx.ID_ANY, u"基础数据表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.data_view_title.Wrap( -1 )

		self.data_view_title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.data_view_title, 1, wx.ALIGN_CENTER, 5 )

		self.base_data_view = wx.grid.Grid( self.date_view_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,540 ), 0 )

		# Grid
		self.base_data_view.CreateGrid( 0, 0 )
		self.base_data_view.EnableEditing( False )
		self.base_data_view.EnableGridLines( True )
		self.base_data_view.EnableDragGridSize( False )
		self.base_data_view.SetMargins( 0, 0 )

		# Columns
		self.base_data_view.EnableDragColMove( False )
		self.base_data_view.EnableDragColSize( True )
		self.base_data_view.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.base_data_view.EnableDragRowSize( False )
		self.base_data_view.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.base_data_view.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.base_data_view, 0, wx.ALL, 5 )


		date_view_sizer.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.drawing_btn = wx.BitmapButton( self.date_view_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.drawing_btn.SetBitmap( wx.Bitmap( u"static/arrow.png", wx.BITMAP_TYPE_ANY ) )
		self.drawing_btn.Enable( False )

		bSizer7.Add( self.drawing_btn, 0, wx.ALL, 5 )

		self.drawing_btn_label = wx.StaticText( self.date_view_panel, wx.ID_ANY, u"点击开始抽取", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.drawing_btn_label.Wrap( -1 )

		bSizer7.Add( self.drawing_btn_label, 0, wx.ALIGN_CENTER, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		date_view_sizer.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		result_btn_sizer = wx.FlexGridSizer( 0, 4, 0, 0 )
		result_btn_sizer.SetFlexibleDirection( wx.BOTH )
		result_btn_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.result_title = wx.StaticText( self.date_view_panel, wx.ID_ANY, u"抽签结果", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.result_title.Wrap( -1 )

		self.result_title.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		result_btn_sizer.Add( self.result_title, 0, wx.ALIGN_CENTER, 5 )


		result_btn_sizer.Add( ( 15, 0), 0, wx.EXPAND, 5 )

		self.export_result_btn = wx.Button( self.date_view_panel, wx.ID_ANY, u"导出结果", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.export_result_btn.Enable( False )

		result_btn_sizer.Add( self.export_result_btn, 0, wx.ALIGN_CENTER, 5 )

		self.restart_btn = wx.Button( self.date_view_panel, wx.ID_ANY, u"[]", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		result_btn_sizer.Add( self.restart_btn, 0, wx.ALL, 5 )


		bSizer8.Add( result_btn_sizer, 0, wx.ALIGN_CENTER, 5 )

		self.result_view = wx.grid.Grid( self.date_view_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,540 ), 0 )

		# Grid
		self.result_view.CreateGrid( 0, 0 )
		self.result_view.EnableEditing( False )
		self.result_view.EnableGridLines( True )
		self.result_view.EnableDragGridSize( False )
		self.result_view.SetMargins( 0, 0 )

		# Columns
		self.result_view.EnableDragColMove( False )
		self.result_view.EnableDragColSize( False )
		self.result_view.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.result_view.EnableDragRowSize( True )
		self.result_view.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.result_view.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.result_view, 0, wx.ALL, 5 )


		date_view_sizer.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.date_view_panel.SetSizer( date_view_sizer )
		self.date_view_panel.Layout()
		date_view_sizer.Fit( self.date_view_panel )
		mainSizer.Add( self.date_view_panel, 1, wx.ALL|wx.EXPAND, 5 )


		self.main_panel.SetSizer( mainSizer )
		self.main_panel.Layout()
		mainSizer.Fit( self.main_panel )
		content_layout.Add( self.main_panel, 0, wx.ALL|wx.EXPAND, 5 )

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
		table_layout.Add( self.pagation_panel, 0, wx.EXPAND |wx.ALL, 5 )


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
		self.confirm_draw_table_btn.Bind( wx.EVT_BUTTON, self.confirm_draw_table )
		self.drawing_btn.Bind( wx.EVT_BUTTON, self.do_drawing )
		self.export_result_btn.Bind( wx.EVT_BUTTON, self.export_result )
		self.restart_btn.Bind( wx.EVT_BUTTON, self.restart_panel )
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

	def confirm_draw_table( self, event ):
		event.Skip()

	def do_drawing( self, event ):
		event.Skip()

	def export_result( self, event ):
		event.Skip()

	def restart_panel( self, event ):
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


###########################################################################
## Class error_dialog
###########################################################################

class error_dialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 250,150 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer14 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.error_message = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.error_message.Wrap( -1 )

		fgSizer14.Add( self.error_message, 0, wx.ALIGN_CENTER, 5 )


		fgSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer9.Add( fgSizer14, 1, wx.ALIGN_CENTER, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		fgSizer16 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.error_confirm_btn = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16.Add( self.error_confirm_btn, 0, wx.ALL, 5 )


		fgSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer9.Add( fgSizer16, 1, wx.ALIGN_CENTER, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.error_confirm_btn.Bind( wx.EVT_BUTTON, self.err_confirm )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def err_confirm( self, event ):
		event.Skip()


