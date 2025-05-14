import threading

with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)

print("Read line by line")
with open('filename.txt', 'r') as file:
    for line in file:
        print(line.strip())

print("Read lines into a list")
with open('filename.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

print("Read specific number lines")
with open('filename.txt', 'r') as file:
    content = file.read(100)
    print(content)


def read_chunks(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

for chunk in read_chunks('filename.txt'):
    print(f"chunk: {chunk}")


print("Read on threads")

def read_chunk(file_path, start, size, thread_id):
    with open(file_path, 'r') as file:
        file.seek(start)  # Move to the start position
        chunk = file.read(size)  # Read the specified chunk size
        print(f"Thread {thread_id} read:\n{chunk}\n")

def read_file_in_chunks(file_path, chunk_size):
    file_size = 0
    with open(file_path, 'r') as file:
        file.seek(0, 2)  # Move to the end of the file
        file_size = file.tell()  # Get the total file size
    print("file_size: ", file_size)

    threads = []
    start = 0
    thread_id = 1

    while start < file_size:
        size = min(chunk_size, file_size - start)  # Ensure we don't read beyond the file
        thread = threading.Thread(target=read_chunk, args=(file_path, start, size, thread_id))
        threads.append(thread)
        thread.start()
        start += chunk_size
        thread_id += 1

    for thread in threads:
        thread.join()

# Example usage
file_path = "filename.txt"  # Replace with your file path
chunk_size = 10  # Read 1024 bytes (1 KB) per thread
read_file_in_chunks(file_path, chunk_size)