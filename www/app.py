import logging
logging.basicConfig(level=logging.INFO)
import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(text='周公瑾52的博客')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), "172.16.60.236", 9000)
    logging.info('server started at http://172.16.60.236:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
