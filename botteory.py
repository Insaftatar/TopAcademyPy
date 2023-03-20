from time import time ,sleep


# def do_log(func):
#     def wrapper(*args, **kwargs):
#         start_time = time()
#         result = func
#         result()
#         print(result.__name__, " time = ", time() - start_time)
#         return result
#     return wrapper
#
# @do_log
# def func():
#     sleep(1)
#     print(123)
#
# func()
#
# import asyncio
# from time import sleep
#
# async def do_something():
#     print("Hi")
#     await asyncio.sleep(3)
#     print("bay!")
#
# async def do_GOOD():
#     print("HiQW")
#     await asyncio.sleep(2)
#     print("bay!QW")
#
# async def do_BAD():
#     print("HiQWE")
#     await asyncio.sleep(1)
#     print("bay!QWE")
#
# loop = asyncio.get_event_loop()
#
# # for i in range(10):
# #     loop.create_task(do_something())
#
# loop.create_task(do_something())
# loop.create_task(do_GOOD())
# loop.create_task(do_BAD())
#
# loop.run_until_complete(asyncio.gather(do_something()))

