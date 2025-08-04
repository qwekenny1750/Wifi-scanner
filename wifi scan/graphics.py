import matplotlib.pyplot as plt
from scan import WiFiScanner

class GraficWifi:
    def __init__(self, wifiDict: dict):
        d1s = dict(sorted(wifiDict.items(), key=lambda item: item[1], reverse=True))
        d2ss = dict(sorted(wifiDict.items(), key=lambda item: item[1], reverse=True))
        speed_list: list[int] = [s for ss, s  in d1s.items()]
        ssid_list: list[str] = [ss for ss, s  in d2ss.items()]

        self.speed = speed_list[:5]
        self.ssid = ssid_list[:5]

    def __call__(self):
        plt.style.use('ggplot')
        fig, ax = plt.subplots()
        ax.bar(self.ssid, self.speed, color='blue')
        ax.set_title("WI-FI Analityc")
        ax.set_ylabel("Speed (dBm+100)")
        ax.set_xlabel("SSID")
        return fig

