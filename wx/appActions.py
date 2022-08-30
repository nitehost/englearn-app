import json
import random
import wx

def get_words(filename):
    with open(filename, "r") as f:
        data = f.read()
    # print("Data type before:", type(data))
    js = json.loads(data)
    # print("Data type after:", type(js))
    return js


def fill_data(fillbox, json_data):
    print("Fill box:", fillbox)
    print("Fill data...")
    print(json_data)
    # random.shuffle(json_data)
    data = sorted(json_data.items(), key=lambda x: random.random())
    for (label, value) in data:
        # row = row_create(fillbox.panel, word[0], word[1])

        # sizebox
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        fillbox.sizer.Add(sizer, 0, wx.EXPAND, 0)

        label_l = wx.StaticText(fillbox.panel, wx.ID_ANY, label, style=wx.ALIGN_RIGHT)
        sizer.Add(label_l, 1, wx.ALIGN_CENTER_VERTICAL, 0)

        text_ctrl = wx.TextCtrl(fillbox.panel, wx.ID_ANY, "123")
        sizer.Add(text_ctrl, 1, wx.EXPAND, 0)

        label_r = wx.StaticText(fillbox.panel, wx.ID_ANY, value, style=wx.ALIGN_LEFT)
        sizer.Add(label_r, 1, wx.ALIGN_CENTER_VERTICAL, 0)

        # fillbox.sizer.Add((0, 0), 0, 0, 0)
        pass


# def row_create(parent, label, value):
#     print(label, value)
    # self.entries.append({
    #     "word": label_text,
    #     "object": entry,
    #     "translate": correct_value,
    #     "helper": helper
    # })
