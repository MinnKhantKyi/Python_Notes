import asyncio

async def main():                       # async keyword return coroutine obj
    print("Asynchronous...")
    # task say that run this code as fast as it can be,
    # but let allow other code(in thi case, print("Finished...")) to run while it wait
    task = asyncio.create_task(Foo("Await...")) 
    # If task is run first and other code can run after it had done,
    # use await
    await task
    print("Finished...")

# await excutes coroutine obj and run it
# await can only be used in async defined func.
async def Foo(text):
    print(text)
    await asyncio.sleep(2)              # asyncio.sleep(1) return coroutine obj

# asyncio.run(coroutine obj)
# asyncio create Event Loop
# Event Loop handle all the background stuff of asynchronous programming
asyncio.run(main())