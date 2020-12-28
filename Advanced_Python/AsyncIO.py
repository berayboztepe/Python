import asyncio
import time


async def find_divisibles(inrange, div_by):
    print(f'finding nums in range {inrange} divisible by {div_by}')
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.00001)
    print(f'Done w/ nums in range {inrange} divisible by {div_by}')
    return located


# as we can see, first div1 worked, then div2, then div3 but if inrange is a big number, it will hang!
# what about we do smt like, 3 of them work at the same time in another threads. after div2 and div3 finished,
# these threads help to finish div1 (div1 inrange = 500203901, a big number)
# we can also use yields instead of asyncIO
async def main():
    div1 = loop.create_task(find_divisibles(508000, 34113))
    div2 = loop.create_task(find_divisibles(100052, 3210))
    div3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.wait([div1, div2, div3])
    return div1, div2, div3


""" first step is async both of main and find_divisibles
 then we will import asyncIO
 we need to initialize loop in main!
 then we want to run main co-routine until it's done so loop.run_until_complete(main()) will be our code
 we could run_forever, run_until_complete. we can check is_running, stop() etc.
 then we will close the loop
 then we will add loop_create_task() to div1, div2 and div3
 then we're gonna await batches or single co-routine await asyncio.wait([div1, div2, div3])
 even though find_divisibles co-routine, everything that inside of that func is still runs synchronous
 we add if i % 50000, we will wait it 0.00001 sec. 50000 and sec can change.
 so now, div3 finished first because in 50000, div1 did sleep. also div2 did sleep. so div3 finished first.
 then div2 and div1 did sleep again for the second time. then div1 did sleep again and div2 finished. 
 finally div1 finished:
# finding nums in range 508000 divisible by 34113
# finding nums in range 100052 divisible by 3210
# finding nums in range 500 divisible by 3
# Done w/ nums in range 500 divisible by 3
# Done w/ nums in range 100052 divisible by 3210
# Done w/ nums in range 508000 divisible by 34113"""


async def coro(seq):
    await asyncio.sleep(max(seq))  # it will wait 10 sec
    return list(reversed(seq))


# another example
async def gather():
    t = asyncio.create_task(coro([3, 2, 1]))
    t2 = asyncio.create_task(coro([10, 5, 0]))
    print('Start : ', time.strftime('%X'))
    a = await asyncio.gather(t, t2)
    print('End : ', time.strftime('%X'))
    print(f'Both tasks done = {(all((t.done(), t2.done())))}')
    return a


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()  # it's gonna initialize loop for us
        loop.set_debug(False)
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())  # this is how we can get our results
    except Exception as e:
        pass
    finally:
        loop.close()
    a = asyncio.run(gather())
    print(a)


"""Start :  19:04:49
 res: [1, 2, 3] completed at 09:49:10
 res: [0, 5, 10] completed at 09:49:17
End :  19:04:59
Both tasks done = True
[[1, 2, 3], [0, 5, 10]]"""