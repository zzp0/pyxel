def load_library():
    import ctypes
    import os
    import platform

    lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
    lib_name = "libpyxelcore"
    system = platform.system()

    if system == "Darwin":
        lib_path = os.path.join(lib_dir, "macos", lib_name) + ".dylib"
    elif system == "Windows":
        win_dir = "win64" if platform.architecture()[0] == "64bit" else "win32"
        lib_path = os.path.join(lib_dir, win_dir, lib_name) + ".dll"
        dll_path = os.path.join(lib_dir, win_dir)
        os.environ["PATH"] = dll_path + os.pathsep + os.environ["PATH"]
    elif system == "Linux":
        lib_path = os.path.join(lib_dir, "linux", lib_name) + ".so"
    else:
        raise RuntimeError("unsupported platform: {}".format(system))

    return ctypes.cdll.LoadLibrary(lib_path)


lib = load_library()


if __name__ == "__main__":
    import pyxel

    class App:
        def __init__(self):
            pyxel.init(256, 256)  # noqa: F821

            self.x = 0

            pyxel.run(self.update, self.draw)  # noqa: F821

        def update(self):
            self.x += 1

        def draw(self):
            pyxel.cls(0)  # noqa: F821
            pyxel.rect(self.x, 30, 300, 50, 8)  # noqa: F821
            pyxel.rectb(10, 70, 300, 100, pyxel.frame_count % 16)  # noqa: F821
            pyxel.blt(30, 100, 3, 0, 0, 256, 256)
            pyxel.pix(self.x, 10, 7)  # noqa: F821
            pyxel.pix(pyxel.mouse_x, pyxel.mouse_y, 7)  # noqa: F821

    App()
