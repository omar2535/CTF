import os
import subprocess
import time 

NUM_TRIALS = 5
found_pins = []

found_pin = ""
for index in range(0, 8):
    times_taken = []
    for i in range(0, 10):
        PIN = found_pin + str(i) + (8 - len(found_pin) - 1) * '0'
        print(f"Trying PIN: {PIN}")
        
        start_time = time.time()
        res = os.system(f"echo \"{PIN}\" | ./pin_checker")
        time_taken = time.time() - start_time

        print(f"time taken: {time_taken}")
        times_taken.append(time_taken)

    # Find outlier in times taken
    # LOOK FOR PIN ACCEPTED STRING!
    max_time = max(times_taken)
    print(times_taken.index(max_time))
    found_pin += str(times_taken.index(max_time))
    breakpoint()

found_pins.append(found_pin)

print(f"FOUND PINS: {found_pins}")
print(f"Trying pins!")

for pin in found_pins:
    os.system(f"echo \"{pin}\" | ./pin_checker")
