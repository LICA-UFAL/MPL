import platform

config = None

if platform.system().lower() == "windows":
    from .windows import config
elif platform.system().lower() == "linux":
    from .unix import config
else:
    raise Exception("your system platform isn't supported by mpl")