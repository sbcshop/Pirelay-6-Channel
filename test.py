import PiRelay
import time

r1 = PiRelay.Relay("RELAY1")
r2 = PiRelay.Relay("RELAY2")
r3 = PiRelay.Relay("RELAY3")
r4 = PiRelay.Relay("RELAY4")
r5 = PiRelay.Relay("RELAY5")
r6 = PiRelay.Relay("RELAY6")

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
