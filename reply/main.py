#!/usr/bin/python
import itchat

on = True
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def text_reply(msg):
    print(msg.fromUserName)
    if msg.toUserName == "filehelper":
        msg.fromUserName = msg.toUserName
        if msg.text == "on":
            on = True
        elif msg.text == "off":
            on = False

    if on:
        m = "对方是诺基亚手机，暂时收不到微信信息，如有急事请拨打短号123456,不便之处，敬请谅解"
        itchat.send_msg(m,msg.fromUserName)
        return
# itchat.auto_login(enableCmdQR=0, hotReload=True) # 如果是在window上或者有可视化界面的ubuntu系统上，可以用这个
itchat.auto_login(enableCmdQR=1,hotReload=True)   # enableCmdQR=1是在控制台输出微信登录二维码
itchat.run()

