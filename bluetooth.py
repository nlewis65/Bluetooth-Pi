from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(5.0)

N = 4

def calculate_distance(txpower, rssi):
    dist_meters = 10 ** ((-txpower - rssi)/(10*N))
    dist_feet = dist_meters * 3.2808
    return dist_feet

for dev in devices:
        txPower = 0
    #if dev.addr == "fa:0d:ac:3d:13:f2":
        print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            print("  %s = %s" % (desc, value))
            if desc == "Tx Power":
                txPower = int(value, 16)
        dist = calculate_distance(txPower, dev.rssi)
        if txPower != 0:
            print ("Device Distance = %s" % (dist))