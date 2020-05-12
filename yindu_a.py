#coding:utf-8
import itchat
import bus as B
def yindu():
    content = []
    router_name = ["143路","莘南专线","闵行41路","庄莘线","闵行30路"]

    direction = ['1','1','1','0','1']

    stop_id = ['36','25','31','40','15']

    bus = B.Bus()

    for i in range(len(router_name)):
        r_name = router_name[i]
        stop = stop_id[i]
        dire = direction[i]
    #info = bus.query_router(r_name,direction=dire)
    #print(info)
        r = bus.query_stop(r_name,dire,stop)
        if r["stop_interval"]=="" and r["time"] =="":
            content.append(r_name +"已停运\n\r")
        else:
            content.append(r_name+"  还有"+r["stop_interval"]+"站  "+ str(round(int(r["time"])/60.0,2))+"分\n\r")
    return "".join(content)


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    default="没消息"
    print("auto reply")
    reply = yindu()
    return reply or default 

if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    itchat.run()
