### code by gnzng

import objc, os, time, subprocess

process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-s'], stdout=subprocess.PIPE)
out, err = process.communicate()
process.wait()
print(out)

print('make sure it is the only network your mac is able to connect to\n\n')

aim =  str(raw_input('enter bssid to connect to in roaming network:\n')).lower()

if aim == '':
    aim =  'xx:xx:xx:xx:xx:xx'.lower()    #for often used connection
    print('try to connect to {}'.format(aim))

def connect():
    objc.loadBundle('CoreWLAN',
                    bundle_path = '/System/Library/Frameworks/CoreWLAN.framework',
                    module_globals = globals())
    os.system("networksetup -setairportpower airport off")
    os.system("networksetup -setairportpower airport on")
    time.sleep(10) #can be optimized
    t1 = subprocess.Popen(('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'), stdout=subprocess.PIPE)
    global output 
    output = str(subprocess.check_output(('awk', '/ BSSID/ {print substr($0, index($0, $2))}'), stdin=t1.stdout)).lower()
    output = output.rstrip()
    print(output)
connect()

while output != aim:
    connect()


if output == aim:
    print('successfully connected to {}'.format(aim))
    os.system('say "successfully connected"')
else:
    print('please restart, something bad happened')
