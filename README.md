# windows-auto-locker
Automatc Lock Windows when you leave with your device(ping IPs)

People usually has wifi(private network) in their own house, and take smart phones with themself everywhere

Although there're some lock-helper already, but they usually comes with bluetooth, which is not necessary in my daily use

so here comes a **ip**-lock-helper

# Module used
`OS` `time` `ctypes`, written in python 3, should also work in python2 

# Usage

Change DEVICE_IP to your cellphone's or anythings you'll leave with

run `pythonw lock.py` when windows start

# Feature
* support multiple IPs
* check every 15s (you can change by yourself)
* Define idling by checking last input time (60s default) (you can set the threshold yourself)

