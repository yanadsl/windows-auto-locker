# windows-auto-locker
Automatc Lock Windows when you leave with your device(ping IPs)

People usually has wifi(private network) in their own house, and take smart phones with themself everywhere

Although there're some lock-helper already, but they usually need bluetooth, which eats battery and not my daily usage

so here comes an **ip**-lock-helper

# Module used
`OS` `time` `ctypes`, written in python 3, should also work in python2 

# Usage
Change DEVICE_IP to your cellphone's or anythings you'll leave with

run `pythonw locker.py` when windows start and just leave it alone

# Feature
* support multiple IPs
* check every 15s (you can change by yourself)
* Define idling by checking last input time (60s default) (you can set the threshold yourself)

# How does it work?
By calling `ctype.windll.user32.GetLastInputInfo` to check if user's idling time > `IDLE_TIME`

ping the whole `DEVICE_IP` list, lock the computer `ctype.windll.user32.LockWorkStation()` when every IP is unreachable
