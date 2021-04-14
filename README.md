# wifi-bssid-chooser

Small code snippet for choosing a specific BSSID in roaming networks, which can be sometimes hard with versions of macOS. The script does it by turning the WIFI connection off and on, reconnecting, and comparing the BSSIDs. It gives an audio feedback. 

For often used connections, you can change the BSSID in the wifi-bssid-chooser.py here:
```python
    aim =  '12:12:12:23:43:4a'.lower()    #for often used connection
```
Then you will try to connect to this network when pressing enter after the finished network scan automatically.
