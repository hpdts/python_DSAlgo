import threading
import time

def greet(name):
	print(f"Hello, {name}")
	time.sleep(2)
	print(f"Goodbye, {name}")



thread = threading.Thread(target=greet, args=("Alice",))

thread.start()

thread.join()

print("Main thread finished.")


names = ["Alice", "Bob", "Charlie"]
threads = []

for name in names:
    thread = threading.Thread(target=greet, args=(name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("All threads finished.")



counter = 0
lock = threading.Lock()

def increment():
	global counter
	for _ in range(100000):
		with lock:
			counter+=1

threads = []
for _ in range(2):
	thread = threading.Thread(target=increment)
	threads.append(thread)
	thread.start()

for thread in threads:
	thread.join()

print(f"Final counter value: {counter}")




