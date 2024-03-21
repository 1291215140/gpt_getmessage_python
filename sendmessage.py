from openai import OpenAI
with open("api_key","r") as f:
        api_key = f.readline()
client = OpenAI(api_key=api_key)
import connectredis
import json
def SendMessage(message):
    messages = ""
    #等待数据引入
    messages=connectredis.getvalue(message["username"])
    if messages=="" or messages==None:
        return "没有历史记录"
    messages.append({"role":"user", "content":message["content"]})
    print(messages)
    #发送数据
    completion = client.chat.completions.create(model="gpt-3.5-turbo",messages=messages)
	#返回message对象(content='{}', role='assistant', 	#function_call=None, tool_calls=None)
    mess = completion.choices[0].message.content
    #print(completion.choices[0])
    #追加返回数据
    messages.append({"role":"assistant","content":mess})
    #更新数据
    connectredis.setvalue(message["username"],json.dumps(messages))
    #测试
    print(mess)
    return mess