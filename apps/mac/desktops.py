import contextlib
import time

from talon import actions, ctrl, Module, ui


def amethyst_running():
    return bool(ui.apps(bundle="com.amethyst.Amethyst"))


@contextlib.contextmanager
def drag_window(win=None):
    if win is None:
        win = ui.active_window()
    fs = win.children.find(AXSubrole="AXFullScreenButton")[0]
    rect = fs.AXFrame["$rect2d"]
    x = rect["x"] + rect["width"] + 5
    y = rect["y"] + rect["height"] / 2
    ctrl.mouse_move(x, y)
    ctrl.mouse_click(button=0, down=True)
    yield
    time.sleep(0.1)
    ctrl.mouse_click(button=0, up=True)


mod = Module()


@mod.action_class
class user_actions:
    def desktop(number: int):
        "change the current desktop"
        if number < 10:
            actions.key("ctrl-{}".format(number))

    def window_move_desktop_left():
        """move the current window to the desktop to the left"""
        with drag_window():
            actions.key("ctrl-cmd-alt-left")

    def window_move_desktop_right():
        """move the current window to the desktop to the right"""
        with drag_window():
            actions.key("ctrl-cmd-alt-right")

    def window_move_desktop(desktop_number: int):
        """move the current window to a different desktop"""
        if amethyst_running():
            actions.key(f"ctrl-alt-shift-{desktop_number}")
        else:
            with drag_window():
                actions.key(f"ctrl-{desktop_number}")
