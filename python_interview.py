"""
Create a system to read and process a file containing millions of nodes, 
ensuring optimal performance through file reading/writing techniques and multi-threading?
Big files, binary text

use list
"""
import threading

def read_chunks(file_name, chunk_size=1024):
	with open(file_name, 'r') as file:
		chunk = file.read(chunk_size)
		if not chunk:
			return
		yield chunk


#chunks = []
def process():
	for chunk in read_chunks('filename.txt'):
		#print(f"chunk: {chunk}")
#		chunks.append(chunks)
		return chunk


threads=[]

for _ in range(10):
	thread = threading.Thread(target=process)
	threads.append(thread)


for thread in threads:
	thread.start()
	thread.join()


