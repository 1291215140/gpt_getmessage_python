import asyncio
import websockets
import time
import requests
import sendmessage
import connectredis
bool = "true"
async def echo(socket, path):
    print('客户端{}已连接！'.format(socket.remote_address))
    try:
        while  True:
            # 等待接收客户端发送的消息
            message = await socket.recv()
            #将字符串转换成字典
            message = eval(message)
            print(message)
            #{"message","username"}
            if(connectredis.getvalue(message["username"])==None):
                import requests
                bool = requests.get(url="http://localhost:8080/loadmessage?username={}".format(message["username"])).text
                print(bool)
                if(bool=="false"):
                    print("初始化中")
                    import json
                    list = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
                    connectredis.setvalue(message["username"],json.dumps(list))
            # 向客户端发送消息
            await socket.send(sendmessage.SendMessage(message))
    except Exception as e:
        print(str(e))
        await socket.close()
start_server = websockets.serve(echo, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



