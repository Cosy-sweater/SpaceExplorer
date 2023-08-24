def create_directory(HWND=None):
    import os
    import ctypes
    import shutil

    appdata_path = os.getenv('LOCALAPPDATA')
    dir_path = appdata_path + r"\SpaceExplorer"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        popup_resp = ctypes.windll.user32.MessageBoxW(HWND,
                                                      "Overwrite old directory?",
                                                      "Directory already exist",
                                                      0x1)

        if popup_resp == 1:
            for root, dirs, files in os.walk(dir_path):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))


if __name__ == "__main__":
    create_directory(None)
