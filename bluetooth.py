import subprocess

N = 4
txPower = 12

def calculate_distance(txpower, rssi):
    dist_meters = 10 ** ((-txpower - rssi)/(10*N))
    dist_feet = dist_meters * 3.2808
    return dist_feet

#if dev.addr == "be:89:60:00:02:df":
s = subprocess.call('hcitool rssi be:89:60:00:02:df', shell=True)
print("%s" % (s))
dist = calculate_distance(txPower, int(s))
print ("Device Distance = %s" % (dist))
