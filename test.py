import PiRelay6
import time

r1 = PiRelay6.Relay("RELAY1")
r2 = PiRelay6.Relay("RELAY2")
r3 = PiRelay6.Relay("RELAY3")
r4 = PiRelay6.Relay("RELAY4")
r5 = PiRelay6.Relay("RELAY5")
r6 = PiRelay6.Relay("RELAY6")

r1.on()
time.sleep(0.5)
r1.off()
time.sleep(0.5)

r2.on()
time.sleep(0.5)
r2.off()
time.sleep(0.5)

r3.on()
time.sleep(0.5)
r3.off()
time.sleep(0.5)

r4.on()
time.sleep(0.5)
r4.off()
time.sleep(0.5)

r5.on()
time.sleep(0.5)
r5.off()
time.sleep(0.5)

r6.on()
time.sleep(0.5)
r7.off()
time.sleep(0.5)
