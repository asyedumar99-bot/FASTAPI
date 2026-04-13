import asyncio

async def slow():
    print("I need to wait for sometime")
    await asyncio.sleep(2)
    print("I was waiting for 2 seconds")
    return "Done"

async def main():
    result = await slow()
    print(result)

asyncio.run(main())