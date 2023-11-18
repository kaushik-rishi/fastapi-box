import asyncio

async def count():
	print("one")
	await asyncio.sleep(1)
	print("two")

async def main():
	await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
	import time
	start_time = time.perf_counter()

	asyncio.run(main())

	elapsed_time = time.perf_counter() - start_time
	print(f"{__file__} executed in {elapsed_time:0.2f} seconds")
