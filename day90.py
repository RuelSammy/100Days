#Concurrency and parallelism(Threading and multi-processing)
import threading
import time

# Function to be run in a separate thread
def task(name):
    print(f"{name} starting")
    time.sleep(2)  # Simulates a blocking I/O operation
    print(f"{name} done")

# Create two threads
thread1 = threading.Thread(target=task, args=("Thread-1",))
thread2 = threading.Thread(target=task, args=("Thread-2",))

# Start both threads; they run concurrently
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

import multiprocessing
import time

# Function to be run in a separate process
def compute(name):
    print(f"{name} computing")
    time.sleep(2)  # Simulates a CPU-bound task for demonstration
    print(f"{name} done")

# Protects the entry point for Windows compatibility
if __name__ == '__main__':
    # Create two processes
    process1 = multiprocessing.Process(target=compute, args=("Process-1",))
    process2 = multiprocessing.Process(target=compute, args=("Process-2",))

    # Start both processes; they run in true parallelism (if multiple CPU cores are available)
    process1.start()
    process2.start()

    # Wait for both to finish
    process1.join()
    process2.join()

import asyncio

# An async function (coroutine)
async def fetch_data(name):
    print(f"{name} fetching")
    await asyncio.sleep(2)  # Non-blocking sleep, yields control to event loop
    print(f"{name} done")

# Main coroutine to gather and run tasks concurrently
async def main():
    # Runs multiple async tasks concurrently
    await asyncio.gather(fetch_data("Task-1"), fetch_data("Task-2"))

# Starts the asyncio event loop
asyncio.run(main())
