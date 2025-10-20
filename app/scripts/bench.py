import asyncio
import statistics
import time
import httpx


URL = "http://127.0.0.1:8000/fib"
PAYLOAD = {"n": 2000}
CONCURRENCY = 50
REQUESTS = 500




async def worker(client, latencies):
t0 = time.perf_counter()
r = await client.post(URL, json=PAYLOAD)
r.raise_for_status()
latencies.append((time.perf_counter() - t0) * 1000)




async def main():
latencies = []
async with httpx.AsyncClient(timeout=10) as client:
tasks = [worker(client, latencies) for _ in range(REQUESTS)]
t0 = time.perf_counter()
await asyncio.gather(*tasks)
elapsed = time.perf_counter() - t0
p95 = statistics.quantiles(latencies, n=100)[94]
print(f"Completed {REQUESTS} req in {elapsed:.2f}s")
print(f"Throughput: {REQUESTS/elapsed:.1f} req/s, p95: {p95:.1f} ms")




if __name__ == "__main__":
asyncio.run(main())