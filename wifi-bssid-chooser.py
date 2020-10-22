### code by gnzng
import objc, os, time, subprocess



os.system("networksetup -setairportpower en0 on")
process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-s'], stdout=subprocess.PIPE)
out, err = process.communicate()
process.wait()
print(out)

print('make sure it is the only network your mac is able to connect to\n\n')

aim =  str(raw_input('enter bssid to connect to in roaming network:\n')).lower()

if aim == '':
    aim =  '00:00:00:00:00:00'.lower()    #for often used connection
    print('try to connect to {}'.format(aim))

def get_bssid():
    t1 = subprocess.Popen(('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'), stdout=subprocess.PIPE)
    global output 
    output = str(subprocess.check_output(('awk', '/ BSSID/ {print substr($0, index($0, $2))}'), stdin=t1.stdout)).lower()
    output = output.rstrip()

def connect():
    objc.loadBundle('CoreWLAN',
                    bundle_path = '/System/Library/Frameworks/CoreWLAN.framework',
                    module_globals = globals())
    os.system("networksetup -setairportpower en0 off")
    time.sleep(5)
    os.system("networksetup -setairportpower en0 on")
    time.sleep(5) 
    get_bssid()
    if output == '0:0:0:0:0:0':
        time.sleep(30)    #the 5ghz takes longer to connect to in my experience
        get_bssid()
    print('connected to '+ output)

get_bssid()

while output != aim:
    connect()


if output == aim:
    print('successfully connected to {}'.format(aim))
else:
    print('please restart, something bad happened')

try:
    os.system('say "successfully connected"')
except:
    pass

