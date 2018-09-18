# -*- coding: utf-8 -*-
import ctypes
from os.path import join, dirname, abspath

INVALID_VALUE = 0xffff

WM_IMESUPPORT_SET_INLINE_POSITION = -1
imesupport_dll = None


def setup(arch_x64, dll_dir=dirname(dirname(abspath(__file__)))):
    # Default DLL location: ../imesupport_hook_xxx.dll
    global imesupport_dll
    global WM_IMESUPPORT_SET_INLINE_POSITION
    if imesupport_dll is not None:
        return True

    imesupport_dll = ctypes.cdll.LoadLibrary(
        join(dll_dir,
            'imesupport_hook_x64.dll' if arch_x64 else
            'imesupport_hook_x86.dll'
            ))
    WM_IMESUPPORT_SET_INLINE_POSITION = imesupport_dll.GetMessageId()
    return imesupport_dll.StartHook()


def set_inline_position(hwnd, x, y, font_face, font_height):
    # TODO Use font_face
    if imesupport_dll is not None:
        ctypes.windll.user32.PostMessageW(
            hwnd, WM_IMESUPPORT_SET_INLINE_POSITION, x << 16 | y, font_height)


def clear_inline_position(hwnd):
    if imesupport_dll is not None:
        ctypes.windll.user32.PostMessageW(
            hwnd, WM_IMESUPPORT_SET_INLINE_POSITION, INVALID_VALUE, INVALID_VALUE)
