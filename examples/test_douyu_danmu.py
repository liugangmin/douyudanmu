import asyncio
import os
import sys

sys.path.append("..")
from examples.douyu.ws_douyu_danmu_client import WsDanmuClient

 # https://www.douyu.com/123455
room_id = input("请输入房间id:")
area_id = 0


async def test_danmu_client(client):
    connection = client(room_id, area_id)
    asyncio.ensure_future(connection.run_forever())
    await asyncio.sleep(1000)
    await connection.reset_roomid(room_id)
    print('RESTED')
    connection.pause()
    await asyncio.sleep(200)
    print('resume')
    connection.resume()
    await asyncio.sleep(20)
    print('close')
    await connection.close()
    print('END')


async def test_tcp_danmu_client():
    await test_danmu_client(0)
    
    
async def test_ws_danmu_client():
    await test_danmu_client(WsDanmuClient)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(test_ws_danmu_client())
loop.close()
