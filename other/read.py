import os


def read_config() -> dict:
    appdata_path = os.getenv('LOCALAPPDATA')
    dir_path = appdata_path + r"\SpaceExplorer"
    try:
        with open(f"{dir_path}/config", "r") as f:
            res = f.readline()
            return eval(res)
    except Exception as e:
        print(e, "config not found")
        with open(f"{dir_path}/config", "w") as f:
            from config import base_config
            print(base_config, file=f)


