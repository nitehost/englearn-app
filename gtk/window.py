import gi
import json
import random

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk


class MainWindow(Gtk.Window):

    entries = []

    def __init__(self, title='MainWindow'):
        super().__init__(title=title)
        print("Create main window...")

        # form style
        self.set_border_width(10)
        self.set_default_size(640, 480)

        # hb = Gtk.HeaderBar()
        # hb.set_show_close_button(True)
        # hb.props.title = title
        # self.set_titlebar(hb)

        self.outer_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        # self.add(self.outer_box)

        # outer_box.add(self.hrow_create("first"))
        # outer_box.add(self.hrow_create("second"))
        # outer_box.add(self.hrow_create("third"))

        sw = Gtk.ScrolledWindow()
        self.add(sw)
        sw.add_with_viewport(self.outer_box)

        btn_reset = Gtk.Button(label="Reset")
        btn_reset.connect('clicked', self.reset_result)

        btn_check = Gtk.Button(label="Check")
        btn_check.connect('clicked', self.check_result)
        self.btn_check = btn_check

        box_btns = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box_btns.pack_end(btn_reset, True, True, 10)
        box_btns.pack_end(btn_check, True, True, 10)

        self.outer_box.pack_end(box_btns, True, True, 10)

        actionbar = Gtk.ActionBar()
        self.outer_box.pack_start(actionbar, True, True, 0)

        # btn1 = Gtk.Button(label="test1")
        # btn2 = Gtk.Button(label="test2")
        # btn3 = Gtk.Button(label="test3")
        # actionbar.pack_start(btn1)
        # actionbar.pack_start(btn2)
        # actionbar.pack_start(btn3)

        # self.outer_box.pack_end(status_bar, True, True, 0)


    def hrow_create(self, label_text, correct_value):

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.set_halign(Gtk.Align.CENTER)

        label = Gtk.Label(label=label_text)
        label.set_xalign(0.9)
        label.set_width_chars(25)
        box.pack_start(label, False, False, 0)

        entry = Gtk.Entry()
        entry.set_width_chars(25)
        box.pack_start(entry, False, False, 0)

        helper = Gtk.Label(label="")
        helper.set_xalign(0.1)
        helper.set_width_chars(25)
        box.pack_start(helper, False, False, 0)

        self.entries.append({
            "word": label_text,
            "object": entry,
            "translate": correct_value,
            "helper": helper
        })

        self.outer_box.add(box)
        return box


    def get_words(self, filename):
        with open(filename, "r") as f:
            data = f.read()
        print("Data type before:", type(data))
        js = json.loads(data)
        print("Data type after:", type(js))
        return js


    def fill_data(self, json_data):
        print("Fill data...")
        print(json_data)
        # random.shuffle(json_data)
        data = sorted(json_data.items(), key=lambda x: random.random())
        for word in data:
            self.hrow_create(word[0], word[1])


    def check_result(self, widget, data=None):
        print('Check result...')
        widget.set_state_flags(Gtk.StateFlags.INSENSITIVE, True)

        amount = 0
        success = 0
        for name in self.entries:
            amount += 1
            name["object"].set_state_flags(Gtk.StateFlags.INSENSITIVE, True)
            value = name['object'].get_text().strip().lower()
            # print(
            #     "word:", name["word"],
            #     "value:", value,
            #     "correct", name["translate"]
            # )
            if name["translate"] == value:
                success += 1
                color = Gdk.Color.parse("#4a7a51")
                name["object"].modify_bg(Gtk.StateType.NORMAL, color[1])
            else:
                color = Gdk.Color.parse("#7a4c4b")
                name["object"].modify_bg(Gtk.StateType.NORMAL, color[1])
                name["helper"].set_label(name["translate"])
        print("amount:", amount, "success:", success)

        percents = int(success / amount * 100)
        dialog = Gtk.MessageDialog(
            transient_for = self,
            flags = 0,
            message_type = Gtk.MessageType.INFO,
            buttons = Gtk.ButtonsType.OK,
            text = "Результат {}%".format(percents),
        )
        dialog.format_secondary_text(
            "Всего слов: {}, правильных: {}".format(amount, success)
        )
        dialog.run()
        print("INFO dialog closed")
        dialog.destroy()


    def reset_result(self, widget, data=None):
        print("Reset result...")
        self.btn_check.set_state_flags(Gtk.StateFlags.NORMAL, True)
        for name in self.entries:
            name["object"].set_text("")
            name["object"].modify_bg(Gtk.StateType.NORMAL, None)
            name["object"].set_state_flags(Gtk.StateFlags.NORMAL, True)
            name["helper"].set_label("")
