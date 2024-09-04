import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball_number in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f'Силач {name} поднял {ball_number}')
        ball_number += 1
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    first = asyncio.create_task(start_strongman('Pasha', 3))
    second = asyncio.create_task(start_strongman('Denis', 4))
    third = asyncio.create_task(start_strongman('Appollon', 5))
    await first
    await second
    await third

asyncio.run(start_tournament())
