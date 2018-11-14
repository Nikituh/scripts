from wireless import Wireless
wireless = Wireless()
connected = wireless.connect(ssid='musework', password='matahaninternetti')

print(connected)
