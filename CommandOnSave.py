import sublime
import sublime_plugin
import subprocess


class CommandOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        settings = view.settings()
        folders = settings.get("commands")
        current_file = view.file_name()

        for entry in folders:
            s = entry.index('::')
            c = entry[s:][2:]
            f = entry[:s]

            if current_file[:len(f)] == f:
                if len(c) > 0:
                    subprocess.call([c], shell=True)


def debug(message):
    debug = 'echo "' + message + '" >> ~/.sublime/command_on_save_debug.txt'
    subprocess.call([debug], shell=True)
    return
