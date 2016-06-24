import sublime

import sublime_plugin


class AllformatterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        allcontent = sublime.Region(0, self.view.size())
        self.view.replace(edit, allcontent, 'hello world')
