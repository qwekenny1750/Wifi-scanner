import time
import pywifi

class WiFiScanner:
    def __init__(self):
        self.widiDict = {}
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]

    def __call__(self) -> dict:
        self.iface.scan()
        time.sleep(5)

        results = self.iface.scan_results()
        for r in results:
            if not any(x in r.ssid for x in ["x00", "xd0", "xa"]):
                self.ssid = r.ssid 
                self.speed = r.signal+100
                self.widiDict[self.ssid] = self.speed
        return self.widiDict

