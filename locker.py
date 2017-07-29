import time
import os
from ctypes import Structure, windll, c_uint, sizeof, byref

DEVICE_IP = ["192.168.50.197"]


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


user32 = windll.User32
OpenDesktop = user32.OpenDesktopW
SwitchDesktop = user32.SwitchDesktop
DESKTOP_SWITCHDESKTOP = 0x0100

while True:
    time.sleep(15)
    if get_idle_duration() < 60:  # user should be idle at least 1 min
        continue
    print("Idleing")

    hDesktop = OpenDesktop("default", 0, False, DESKTOP_SWITCHDESKTOP)
    result = SwitchDesktop(hDesktop)
    if not result:  # screen locked already
        continue

    print("scanning ip")
    all_offline = 1
    for IP in DEVICE_IP:
        if not os.system("ping -n 1 -w 6000 " + IP):  # if device is offline 0=succeed
            all_offline = 0
    if all_offline:
        windll.user32.LockWorkStation()
