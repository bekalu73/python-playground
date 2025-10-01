"""
ASYNCHRONOUS I/O (async/await)
==============================

Key Points:
- Asynchronous programming with async/await
- Event loop and asyncio module
- Coroutines and tasks
- Concurrent execution vs parallel execution
- Common async patterns and best practices
- Error handling in async code
"""

import asyncio
import time
import random

print("=== BASIC ASYNC/AWAIT ===")
# Note: async/await enables concurrent programming - good for I/O bound tasks

async def hello_async():
    """Simple async function"""
    print("Hello")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("World")
    return "Async function completed"

# Running async function
print("Running basic async function:")
result = asyncio.run(hello_async())
print(f"Result: {result}")

print("\n=== ASYNC VS SYNC COMPARISON ===")
# Note: Async runs tasks concurrently (not parallel) - one thread, cooperative multitasking

def sync_task(name, duration):
    """Synchronous task"""
    print(f"Sync task {name} started")
    time.sleep(duration)  # Blocking sleep
    print(f"Sync task {name} completed")
    return f"Sync {name} done"

async def async_task(name, duration):
    """Asynchronous task"""
    print(f"Async task {name} started")
    await asyncio.sleep(duration)  # Non-blocking sleep
    print(f"Async task {name} completed")
    return f"Async {name} done"

# Synchronous execution (sequential)
print("Synchronous execution:")
start_time = time.time()
sync_task("A", 1)
sync_task("B", 1)
sync_task("C", 1)
sync_time = time.time() - start_time
print(f"Sync total time: {sync_time:.2f} seconds\n")

# Asynchronous execution (concurrent)
async def run_async_tasks():
    """Run multiple async tasks concurrently"""
    print("Asynchronous execution:")
    start_time = time.time()
    
    # Create tasks
    task_a = asyncio.create_task(async_task("A", 1))
    task_b = asyncio.create_task(async_task("B", 1))
    task_c = asyncio.create_task(async_task("C", 1))
    
    # Wait for all tasks to complete
    results = await asyncio.gather(task_a, task_b, task_c)
    
    async_time = time.time() - start_time
    print(f"Async total time: {async_time:.2f} seconds")
    print(f"Results: {results}")

asyncio.run(run_async_tasks())

print("\n=== CREATING AND MANAGING TASKS ===")
# Note: Tasks run concurrently - create with create_task(), wait with gather()

async def countdown(name, count):
    """Countdown task"""
    for i in range(count, 0, -1):
        print(f"{name}: {i}")
        await asyncio.sleep(0.5)
    print(f"{name}: Done!")
    return f"{name} finished"

async def task_management_demo():
    """Demonstrate task creation and management"""
    print("Creating multiple tasks:")
    
    # Method 1: Using asyncio.create_task()
    task1 = asyncio.create_task(countdown("Task1", 3))
    task2 = asyncio.create_task(countdown("Task2", 4))
    
    # Method 2: Using asyncio.gather()
    results = await asyncio.gather(task1, task2)
    print(f"All tasks completed: {results}")

asyncio.run(task_management_demo())

print("\n=== ASYNC CONTEXT MANAGERS ===")
# Note: Async context managers use __aenter__ and __aexit__ for async resource management

class AsyncFileManager:
    """Async context manager example"""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    async def __aenter__(self):
        """Async enter method"""
        print(f"Opening file: {self.filename}")
        await asyncio.sleep(0.1)  # Simulate async file opening
        self.file = open(self.filename, 'w')
        return self.file
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async exit method"""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
            await asyncio.sleep(0.1)  # Simulate async cleanup

async def async_context_demo():
    """Demonstrate async context manager"""
    async with AsyncFileManager("async_test.txt") as f:
        f.write("Hello from async context manager!")
        await asyncio.sleep(0.5)
    print("File operations completed")

asyncio.run(async_context_demo())

print("\n=== ASYNC GENERATORS ===")
# Note: Async generators yield values asynchronously - use 'async for' to iterate

async def async_number_generator(start, end):
    """Async generator"""
    for i in range(start, end + 1):
        await asyncio.sleep(0.2)  # Simulate async work
        yield i

async def async_generator_demo():
    """Demonstrate async generator"""
    print("Async generator:")
    async for number in async_number_generator(1, 5):
        print(f"Generated: {number}")

asyncio.run(async_generator_demo())

print("\n=== ERROR HANDLING IN ASYNC CODE ===")
# Note: Handle async errors with try/except or return_exceptions=True in gather()

async def risky_task(task_id, should_fail=False):
    """Task that might fail"""
    await asyncio.sleep(random.uniform(0.5, 1.5))
    
    if should_fail:
        raise ValueError(f"Task {task_id} failed!")
    
    return f"Task {task_id} succeeded"

async def error_handling_demo():
    """Demonstrate error handling in async code"""
    tasks = [
        asyncio.create_task(risky_task(1, False)),
        asyncio.create_task(risky_task(2, True)),   # This will fail
        asyncio.create_task(risky_task(3, False)),
    ]
    
    # Method 1: Handle errors individually
    print("Method 1: Individual error handling")
    for i, task in enumerate(tasks, 1):
        try:
            result = await task
            print(f"  {result}")
        except ValueError as e:
            print(f"  Error in task {i}: {e}")
    
    # Method 2: Use asyncio.gather with return_exceptions=True
    print("\nMethod 2: Gather with return_exceptions")
    new_tasks = [
        asyncio.create_task(risky_task(4, False)),
        asyncio.create_task(risky_task(5, True)),
        asyncio.create_task(risky_task(6, False)),
    ]
    
    results = await asyncio.gather(*new_tasks, return_exceptions=True)
    for i, result in enumerate(results, 4):
        if isinstance(result, Exception):
            print(f"  Task {i} failed: {result}")
        else:
            print(f"  Task {i}: {result}")

asyncio.run(error_handling_demo())

print("\n=== PRACTICAL EXAMPLE: WEB SCRAPING SIMULATION ===")
# Note: Async shines for I/O operations like web requests - much faster than sequential

async def fetch_url(session_id, url, delay):
    """Simulate fetching a URL"""
    print(f"Session {session_id}: Starting to fetch {url}")
    await asyncio.sleep(delay)  # Simulate network delay
    
    # Simulate different response types
    if "error" in url:
        raise Exception(f"Failed to fetch {url}")
    
    content_length = random.randint(1000, 5000)
    print(f"Session {session_id}: Fetched {url} ({content_length} bytes)")
    return {"url": url, "content_length": content_length, "session": session_id}

async def web_scraping_demo():
    """Simulate concurrent web scraping"""
    urls = [
        "https://example.com/page1",
        "https://example.com/page2", 
        "https://example.com/error",  # This will fail
        "https://example.com/page3",
        "https://example.com/page4"
    ]
    
    print("Concurrent web scraping simulation:")
    start_time = time.time()
    
    # Create tasks for all URLs
    tasks = []
    for i, url in enumerate(urls):
        delay = random.uniform(0.5, 2.0)  # Random delay
        task = asyncio.create_task(fetch_url(i+1, url, delay))
        tasks.append(task)
    
    # Wait for all tasks with error handling
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Process results
    successful = 0
    failed = 0
    total_bytes = 0
    
    for result in results:
        if isinstance(result, Exception):
            print(f"  Error: {result}")
            failed += 1
        else:
            successful += 1
            total_bytes += result["content_length"]
    
    elapsed_time = time.time() - start_time
    print(f"\nScraping completed in {elapsed_time:.2f} seconds")
    print(f"Successful: {successful}, Failed: {failed}")
    print(f"Total bytes fetched: {total_bytes}")

asyncio.run(web_scraping_demo())

print("\n=== ASYNC PATTERNS ===")
# Note: Producer-consumer pattern with async queues - common for processing workflows

async def producer(queue, name, count):
    """Producer that adds items to queue"""
    for i in range(count):
        item = f"{name}-item-{i}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)
    
    # Signal completion
    await queue.put(None)

async def consumer(queue, name):
    """Consumer that processes items from queue"""
    while True:
        item = await queue.get()
        if item is None:
            break
        
        print(f"Consumer {name} processing: {item}")
        await asyncio.sleep(0.2)  # Simulate processing time
        queue.task_done()

async def producer_consumer_demo():
    """Demonstrate producer-consumer pattern"""
    print("Producer-Consumer pattern:")
    
    # Create queue
    queue = asyncio.Queue(maxsize=5)
    
    # Create tasks
    producer_task = asyncio.create_task(producer(queue, "Producer1", 5))
    consumer_task1 = asyncio.create_task(consumer(queue, "Consumer1"))
    consumer_task2 = asyncio.create_task(consumer(queue, "Consumer2"))
    
    # Wait for producer to finish
    await producer_task
    
    # Wait for queue to be empty
    await queue.join()
    
    # Cancel consumers
    consumer_task1.cancel()
    consumer_task2.cancel()
    
    print("Producer-Consumer demo completed")

asyncio.run(producer_consumer_demo())

print("\n=== TIMEOUTS AND CANCELLATION ===")
# Note: Use wait_for() for timeouts, cancel() to stop tasks - important for robust apps

async def long_running_task(name, duration):
    """Task that takes a long time"""
    try:
        print(f"{name}: Starting long task ({duration}s)")
        await asyncio.sleep(duration)
        print(f"{name}: Task completed")
        return f"{name} finished"
    except asyncio.CancelledError:
        print(f"{name}: Task was cancelled")
        raise

async def timeout_demo():
    """Demonstrate timeouts and cancellation"""
    print("Timeout and cancellation demo:")
    
    # Test timeout
    try:
        result = await asyncio.wait_for(
            long_running_task("Task1", 3), 
            timeout=2.0
        )
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("Task1: Timed out!")
    
    # Test cancellation
    task = asyncio.create_task(long_running_task("Task2", 5))
    await asyncio.sleep(1)  # Let it run for a bit
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Task2: Successfully cancelled")

asyncio.run(timeout_demo())

print("\n=== EXAM FOCUS: KEY CONCEPTS ===")

exam_concepts = """
Essential async/await concepts for exams:

1. Basic syntax:
   - async def function_name(): defines coroutine
   - await expression: waits for coroutine to complete
   - asyncio.run(): runs async function from sync code

2. Key functions:
   - asyncio.sleep(): non-blocking sleep
   - asyncio.create_task(): create task from coroutine
   - asyncio.gather(): run multiple coroutines concurrently
   - asyncio.wait_for(): add timeout to coroutine

3. Concurrency vs Parallelism:
   - Async = concurrent (single thread, cooperative)
   - Parallel = multiple threads/processes

4. Common patterns:
   - Multiple tasks with gather()
   - Producer-consumer with Queue
   - Error handling with return_exceptions=True
   - Timeouts and cancellation

5. When to use async:
   - I/O bound operations (file, network, database)
   - NOT for CPU-bound tasks (use multiprocessing)

6. Important notes:
   - Can't use await in regular functions
   - Can't call async functions directly (need await or asyncio.run)
   - Event loop handles scheduling
"""

print(exam_concepts)

# Quick exam example
async def exam_example():
    """Simple exam-style async function"""
    print("Starting async task")
    await asyncio.sleep(1)
    print("Async task completed")
    return "Success"

print("\nExam example:")
result = asyncio.run(exam_example())
print(f"Result: {result}")

print("\n=== CLEANUP ===")
import os
try:
    os.remove("async_test.txt")
except:
    pass

print("\nAsynchronous I/O mastered! ✓")