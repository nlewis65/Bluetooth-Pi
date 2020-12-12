import subprocess

N = 4
txPower = 12

def calculate_distance(txpower, rssi):
        dist_meters = 10 ** ((txpower - rssi)/(10*N))
        dist_feet = dist_meters * 3.2808
        return dist_feet

# if dev.addr == "be:89:60:00:02:df":
s = subprocess.check_output('hcitool rssi B8:27:EB:7E:92:76', shell=True)
print(s[-4]+s[-3])
dist = calculate_distance(txPower, int(s[-4]+s[-3]))
print ("Device Distance = %s" % (dist))
