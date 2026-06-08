import os
import sys
import subprocess

def compare_versions(current_version, latest_version):
    current_version = current_version.lstrip("v")
    latest_version = latest_version.lstrip("v")

    current = list(map(int, current_version.split(".")))
    latest = list(map(int, latest_version.split(".")))

    for cur, lat in zip(current, latest):
        if lat > cur:
            return True
        elif lat < cur:
            return False

    if len(latest) > len(current):
        return any(x > 0 for x in latest[len(current) :])

    return False

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def install_package(*args):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", *args]
    )

def is_termux():
    termux_prefix = os.environ.get("PREFIX")
    termux_home = os.environ.get("HOME")

    if termux_prefix and "com.termux" in termux_prefix:
        return True
    elif termux_home and "com.termux" in termux_home:
        return True
    else:
        return os.path.isdir("/data/data/com.termux")
    
def install_termux_package(package_name, display_name=None):
    display_name = display_name or package_name

    print(f"\033[1;36m[0]Attempting to install {display_name}\033[m")

    try:
        subprocess.check_call(["pkg", "install", package_name, "-y"])
        print(f"\033[1;36m[0]Installed {display_name} successfully!\033[m")
    except Exception as e:
        print(f"\033[1;31m[x]Error installing {display_name}:\n{e}\033[m")
