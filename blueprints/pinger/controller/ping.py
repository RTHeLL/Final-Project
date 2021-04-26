import subprocess, platform


def ping(address) -> bool:
    """
    Return True/False for ping request to server
    :param address:
    :return:
    """

    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + address
    need_sh = False if platform.system().lower() == "windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0
