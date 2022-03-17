import os
import subprocess
import time 

found_pin = ""
for index in range(0, 8):
    times_taken = []
    for i in range(0, 10):
        PIN = found_pin + str(i) + (8 - len(found_pin) - 1) * '0'
        print(f"Testing PIN: {PIN}\r", end='')
        
        start_time = time.time()
        res = os.popen(f"echo \"{PIN}\" | ./pin_checker").read()
        time_taken = time.time() - start_time

        # print(f"time taken: {time_taken}")
        times_taken.append(time_taken)

    # Find outlier in times taken
    max_time = max(times_taken)
    # print(f"DIGIT AT POSITION {index}: {times_taken.index(max_time)}")
    found_pin += str(times_taken.index(max_time))
    # breakpoint()

print(f"PIN FOUND: {found_pin}. Trying~")
res = os.popen(f"echo \"{found_pin}\" | ./pin_checker").read()
print(res)
