#!/usr/bin/python

from gi.repository import Gtk
from os import listdir, system
from os.path import isfile, join

class convertor(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="GUI Avconv",)
		Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)
		Gtk.Window.set_default_size(self, 300, 200)

		
		self.set_titlebar(Gtk.HeaderBar(show_close_button=True, title="GUI Avconv"))

		grid = Gtk.Grid()
		self.add(grid)

		# the source
		self.label_source = Gtk.Label("Srce : ")
		self.source = Gtk.Entry()
		

		# the dest
		self.label_dest = Gtk.Label("Dest : ")
		self.dest = Gtk.Entry()
		

		self.confirm = Gtk.Button("Start")
		self.confirm.connect("clicked", self.when_confirm_clicked)

		grid.attach(self.label_source, 1,1,1,1)
		grid.attach_next_to(self.source, self.label_source,Gtk.PositionType.RIGHT ,1,1)
		grid.attach_next_to(self.label_dest, self.label_source, Gtk.PositionType.BOTTOM, 1,1)
		grid.attach_next_to(self.dest, self.label_dest, Gtk.PositionType.RIGHT, 1, 1)
		grid.attach_next_to(self.confirm, self.label_dest, Gtk.PositionType.BOTTOM, 1, 1)
		
	def when_confirm_clicked(self, confirm):
		source_folder = self.source.get_text()
		target_folder = self.dest.get_text()
		print "\n\nStarting\n\n"
		for f in listdir(source_folder):
			if isfile(join(source_folder, f)):
				command = "avconv -i \'{}{}\' -vn -f mp3 \'{}{}.mp3\'".format(source_folder,f, target_folder, f)
				system(command)


convertor = convertor()
convertor.show_all()
convertor.connect("delete-event", Gtk.main_quit)
Gtk.main()