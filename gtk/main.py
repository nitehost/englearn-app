#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import window

win = window.MainWindow("English Learning...")
win.connect("destroy", Gtk.main_quit)

words = win.get_words("../words.json")
win.fill_data(words)

win.show_all()
Gtk.main()
