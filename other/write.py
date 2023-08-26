import os


def write_config(cfg: dict) -> None:
    appdata_path = os.getenv('LOCALAPPDATA')
    dir_path = appdata_path + r"\SpaceExplorer"
    try:
        with open(f"{dir_path}/config", "w") as f:
            print(cfg, file=f)
    except Exception as e:
        print(e)
