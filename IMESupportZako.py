import sublime
import sublime_plugin


# class ExampleCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		self.view.insert(edit, 0, "Hello, World!")


class WindowLayout(object):
	@staticmethod
	def calc_cursor_position(view, cursor):
		# from zcodes/IMESupport
		p = view.text_to_window(cursor)
		font_face, font_height = WindowLayout.get_font_info(view)
		return (int(p[0]), int(p[1]), font_face, font_height)

	@staticmethod
	def get_font_info(view):
		font_face = view.settings().get('font_face', '')
		font_height = int(view.line_height())
		font_height -= (view.settings().get("line_padding_top", 0)
			+ view.settings().get("line_padding_bottom", 0))
		return (font_face, font_height)


class ImeSupportEventListener(sublime_plugin.EventListener):
	def __init__(self):
		self.initialized = False

	def on_activated(self, view):
		self.update(view)

	def on_selection_modified(self, view):
		self.update(view)

	def update(self, view):
		if not self.initialized:
			setup()
			self.initialized = True

		if view is None:
			return
		window = view.window()
		if window is None:
			return

		"""
		Memo: The original code of chikatoike creates and caches all the 
		WindowLayout objects like this:
		id = window.id()
		if id not in self.layouts:
		    self.layouts[id] = WindowLayout(window)

		For now I don't understand this part and don't find it useful, so it is removed
		"""

		cursor = view.sel()[0].a
		pos = WindowLayout.calc_cursor_position(view, cursor)

		print(pos)
		set_pos(window.hwnd(), pos)


try:
	from imesupport import globalhook
except ImportError:
	from .imesupport import globalhook


def setup():
	if int(sublime.version()) < 3000:
		# Sublime Text 2 & Python 2.6
		pass
	else:
		# Sublime Text 3 & Python 3.3
		globalhook.setup(sublime.arch() == 'x64')


def set_pos(hwnd, pos):
	if int(sublime.version()) < 3000:
		set_pos_st2(hwnd, pos)
	else:
		set_pos_st3(hwnd, pos)


def set_pos_st2(hwnd, pos):
	"""
	Original code of chikatoike/IMESupport here:
	# set position directly here. (Not handle IME messages.)
	set_inline_position(hwnd, *pos)

	Sorry I don't use ST2 so I'll skip this part
	"""
	pass


def set_pos_st3(hwnd, pos):
	globalhook.set_inline_position(hwnd, *pos)
	pass
