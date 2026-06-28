# Asynchronous I/O

> 📄 **Related code file:** [`16_async_io.py`](16_async_io.py)

## Overview

**Asynchronous programming** lets a single thread handle many tasks concurrently by switching between them whenever one is waiting (for a network response, file, etc.). Python's `asyncio` module and the `async`/`await` keywords make this possible. Async is ideal for **I/O-bound** work — not for CPU-heavy computation.

```python
import asyncio
```

## Basic async/await

- `async def` defines a **coroutine**.
- `await` pauses the coroutine until the awaited operation completes, letting other tasks run.
- `asyncio.run()` starts the event loop and runs a coroutine.

```python
async def hello_async():
    print("Hello")
    await asyncio.sleep(1)    # non-blocking pause
    print("World")
    return "Done"

result = asyncio.run(hello_async())
```

## Concurrency vs Parallelism

| | Async (concurrency) | Parallelism |
|--|--------------------|-------------|
| How | One thread, cooperative switching | Multiple threads/processes |
| Best for | I/O-bound (network, disk, DB) | CPU-bound (heavy math) |
| Module | `asyncio` | `threading`, `multiprocessing` |

> ⚠️ Async does **not** make CPU-bound code faster. It shines when tasks spend time *waiting*.

## Running Tasks Concurrently

The real power comes from running multiple coroutines at once.

```python
async def task(name, duration):
    print(f"{name} started")
    await asyncio.sleep(duration)
    print(f"{name} done")
    return f"{name} result"

async def main():
    # All three run concurrently — total time ≈ 1s, not 3s
    results = await asyncio.gather(
        task("A", 1),
        task("B", 1),
        task("C", 1),
    )
    print(results)

asyncio.run(main())
```

### create_task vs gather
```python
# create_task schedules a coroutine to run concurrently
task1 = asyncio.create_task(task("A", 2))
task2 = asyncio.create_task(task("B", 1))
await task1
await task2

# gather runs several and collects all results
results = await asyncio.gather(task1, task2)
```

## Error Handling

```python
async def risky(should_fail):
    await asyncio.sleep(0.5)
    if should_fail:
        raise ValueError("Task failed!")
    return "Success"

async def main():
    # return_exceptions=True keeps one failure from cancelling the rest
    results = await asyncio.gather(
        risky(False), risky(True), risky(False),
        return_exceptions=True
    )
    for r in results:
        if isinstance(r, Exception):
            print(f"Failed: {r}")
        else:
            print(r)
```

## Timeouts and Cancellation

```python
async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2.0)
    except asyncio.TimeoutError:
        print("Timed out!")

    # Cancellation
    task = asyncio.create_task(long_task())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Cancelled")
```

## Async Context Managers & Generators

```python
# Async context manager: async with
class AsyncResource:
    async def __aenter__(self):
        await asyncio.sleep(0.1)   # async setup
        return self
    async def __aexit__(self, *args):
        await asyncio.sleep(0.1)   # async cleanup

async def use_it():
    async with AsyncResource() as r:
        ...

# Async generator: async for
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def consume():
    async for value in async_range(5):
        print(value)
```

## Producer-Consumer with asyncio.Queue

```python
async def producer(queue, count):
    for i in range(count):
        await queue.put(f"item-{i}")
    await queue.put(None)   # sentinel to signal completion

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Processing {item}")
        queue.task_done()
```

## Common Mistakes

❌ **Using `await` outside an `async` function:**
```python
def f():
    await something()   # SyntaxError
```

❌ **Calling a coroutine without awaiting it:**
```python
hello_async()           # Creates a coroutine but never runs it (warning)
await hello_async()     # Correct (inside async), or asyncio.run(...)
```

❌ **Using blocking calls in async code:**
```python
time.sleep(1)           # Blocks the entire event loop!
await asyncio.sleep(1)  # Correct — non-blocking
```

❌ **Expecting async to speed up CPU-bound work** — use `multiprocessing` instead.

## Best Practices

✅ Use async for I/O-bound tasks (network requests, file/DB access).
✅ Use `asyncio.gather()` to run independent coroutines concurrently.
✅ Never call blocking functions (`time.sleep`, heavy loops) inside coroutines.
✅ Handle `TimeoutError` and `CancelledError` for robust code.
✅ Use `return_exceptions=True` when one task's failure shouldn't stop others.

## Exercises

1. **Concurrent delays:** Write three coroutines that each `await asyncio.sleep` for different times and run them with `gather`. Measure total time.

2. **Timeout guard:** Wrap a coroutine that sleeps 5 seconds in `asyncio.wait_for` with a 2-second timeout and handle the `TimeoutError`.

3. **Async countdown:** Write an async generator that counts down from `n` to `1` with a short delay, consumed via `async for`.

4. **Simulated fetch:** Write a coroutine `fetch(url)` that sleeps a random time and returns a fake result, then fetch several URLs concurrently.

<details>
<summary>💡 Solution hints</summary>

```python
import asyncio

async def delay(name, t):
    await asyncio.sleep(t)
    return name

async def main():
    results = await asyncio.gather(
        delay("A", 1), delay("B", 2), delay("C", 0.5)
    )
    print(results)

asyncio.run(main())
```
</details>

## Key Takeaways

- `async def` defines coroutines; `await` yields control while waiting.
- `asyncio.run()` starts the event loop; `asyncio.gather()` runs tasks concurrently.
- Async = **concurrency** (great for I/O-bound), not parallelism (CPU-bound).
- Never use blocking calls inside coroutines; use `asyncio.sleep`, not `time.sleep`.

---

▶️ **Run the examples:** `python advanced/16_async_io.py`
⏮️ **Previous:** [Regular Expressions](15_regular_expressions.md) | 🎉 **You've completed the Python Playground!**
