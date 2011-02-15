#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join, exists
import json
import wx, wx.grid

class Config(object):
    def __init__(self, path):
        self._configpath = join(path, 'xtags.conf')
        self._config = {}
        
        #try:
        with open(self._configpath, 'r') as fp:
            self._config = json.load(fp)

class Editor(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame5.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_13 = wx.StaticText(self, -1, "Source directory ")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "")
        self.button_2 = wx.Button(self, -1, "...")
        self.label_14 = wx.StaticText(self, -1, "Max depth")
        self.spin_ctrl_1 = wx.SpinCtrl(self, -1, "", min=0, max=100)
        self.grid_1 = wx.grid.Grid(self, -1, size=(200, 500))
        self.grid_sizer_1 = wx.FlexGridSizer(2, 1, 0, 0)
        self.grid_sizer_2 = wx.FlexGridSizer(2, 3, 0, 0)
        self.Bind(wx.EVT_SIZE, self.on_resize)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        
    def on_resize(self, event):
        print 'resize'
        print event.m_size, self.grid_sizer_2.GetSize()
        self.grid_1.SetSize((event.m_size[0], event.m_size[1] - self.grid_sizer_2.GetSize()[1]))

    def __set_properties(self):
        # begin wxGlade: MyFrame5.__set_properties
        self.SetTitle("frame_6")
        self.text_ctrl_3.SetMinSize((260, 28))
        self.button_2.SetMinSize((30, 30))
        self.grid_1.CreateGrid(10, 4)
        self.grid_1.EnableDragRowSize(0)
        self.grid_1.SetColLabelValue(0, "Tag")
        self.grid_1.SetColLabelValue(1, "Type")
        self.grid_1.SetColLabelValue(2, "Nest")
        self.grid_1.SetColLabelValue(3, "Unset")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame5.__do_layout
        self.grid_sizer_2.Add(self.label_13, 0, 0, 0)
        self.grid_sizer_2.Add(self.text_ctrl_3, 0, 0, 0)
        self.grid_sizer_2.Add(self.button_2, 0, 0, 0)
        self.grid_sizer_2.Add(self.label_14, 0, 0, 0)
        self.grid_sizer_2.Add(self.spin_ctrl_1, 0, 0, 0)
        self.grid_sizer_1.Add(self.grid_sizer_2, 1, 0, 0)
        self.grid_sizer_1.Add(self.grid_1, 1, 0, 0)
        self.SetSizer(self.grid_sizer_1)
        self.grid_sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

def editor(target='.'):
    config = Config(target)
    
    app = wx.App(False)
    frame = Editor(None, -1, "xtags configuration")
    frame.Show()
    app.MainLoop()

    