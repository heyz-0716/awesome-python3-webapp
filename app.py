import logging; logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import  datetime
from aiohttp import web

async def  index(request):
    await asyncio.sleep(1)
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'),content_type='text/html')

# @asyncio.coroutine
async def init(loop):
    app = web.Application()
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app._make_handler(),host='127.0.0.1',port=9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

# from aiohttp import web
#
#
# async def handle(request):
#     # name = request.match_info.get('name', "Anonymous")
#     # text = "Hello, " + name
#     return web.Response(body="<h1>加油!何莹钊</h1>".encode('gbk'),content_type='text/html')
#
#
# app = web.Application()
# app.router.add_route('GET','/',handle)
# web.run_app(app,host='127.0.0.1',port=9000)