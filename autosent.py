#coding:utf-8
import itchat
import os
import bus as B
import time
import datetime
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
            content.append(r_name +"等待发车\n\r")
        else:
            content.append(r_name+"  还有"+r["stop_interval"]+"站  "+ str(round(int(r["time"])/60.0,2))+"分\n\r")
    return "".join(content)


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    from_friend = itchat.search_friends(userName=msg["FromUserName"])
    print(from_friend)
    print(from_friend["RemarkName"])
    customer = ["王志鹏"]
    if from_friend["NickName"] in customer:
        default="没消息"
        print("auto reply")
        reply = yindu()
        return reply or default
    else:
        print(from_friend["UserName"])
        pass 

if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    #itchat.run()
   
    while True:
        d_time = datetime.datetime.strptime(str(datetime.datetime.now().date())+'6:45', '%Y-%m-%d%H:%M')
        d_time1 =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'7:10', '%Y-%m-%d%H:%M')
        
        now_time = datetime.datetime.now()
        if now_time > d_time and now_time < d_time1:
            reply = yindu()
            itchat.send(reply, toUserName='filehelper')
            time.sleep(60)
        else:
            os.system('echo notrighttime')
            print("not right time")
            time.sleep(60)
