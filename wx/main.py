#!/usr/bin/env python3

import wx
import appForm
import appActions

print(wx.version())

words = appActions.get_words('../words.json')

app = appForm.MainWindow(None)

appActions.fill_data(app.frame, words)
# print(app.frame.text_ctrl_21.GetValue())

app.MainLoop()
