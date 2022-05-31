from time import sleep, time_ns
import threading

def task():
    if threading.current_thread().name == '1': sleep(1)

start_time = time_ns()

threads = []

for i in range(4):
    threads.append(threading.Thread(target=task, name=i))

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time_ns()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
print('All work completed')
