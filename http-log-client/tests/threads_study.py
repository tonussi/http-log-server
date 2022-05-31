from time import sleep, perf_counter
import threading

def task():
    if threading.current_thread().name == '1': sleep(1)

start_time = perf_counter()

threads = []

for i in range(4):
    threads.append(threading.Thread(target=task, name=i))

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
print('All work completed')
