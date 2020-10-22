# wifi-bssid-chooser

small helper for choosing a bssid in a roaming network, which can be sometimes hard with macOS. The script does it by turning the wifi connection off and on, and comparison of the BSSIDs. 

for often used connections, change the BSSID in the wifi-bssid-chooser.py here:
```python
    aim =  '00:00:00:00:00:00'.lower()    #for often used connection
```
then it will try to connect to this network when pressing enter after the finished network scan. 
