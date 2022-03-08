from talk_functions import *
import os,sys

class Commands(object):
    def __init__(self,botData,_tkr):
        self.laylay = _tkr
        self.botData = botData
            
    def _UserReceiveMessage(self,_tk):
        pass

    def _UserSendMessage(self,_tk):
        try:
            opMessage = _tk.message
            opText = str(opMessage.text).lower()
            opTo = opMessage.to
            opFrom = opMessage._from
            
            if opText.startswith("hello"):
                self.laylay.sendMessage(opTo,"Hello I'm CyberTK?")
                
                
                ############## GROUP - LIST ##############
                
            elif opText.startswith("glist"):
                forNum = 1
                header = " * Chat List * \n\n"
                for groups in self.laylay.getAllChatMids().memberChatMids:
                    header += f"{forNum}. Chat: {self.laylay.getChats([groups]).chats[0].chatName}\n{self.laylay.getChats([groups]).chats[0].chatMid}\n"
                    forNum += 1
                self.laylay.sendMessage(opTo,header)
                
                ############## LIFF - CHECK ##############
                
            elif opText.startswith("liff"):
                self.laylay.sendMessage(opTo,"https://liff.line.me/1656820974-jwLYk4JB")

                ############## TAGALL - MESSAGE ##############
                
            elif opText.startswith("tagall"):
                group=self.laylay.getChats([opTo]).chats[0].extra.groupExtra.memberMids;_mntmd=[]
                for midss in group:_mntmd.append(midss)
                _mdmmbrs=_mntmd;_mdslct=len(_mdmmbrs)//20
                for _mntmmbrs in range(_mdslct+1):
                    ret_='* Mention List *\n';_n=1;_dtmd=[]
                    for _dtmnt in _mntmd[_mntmmbrs*20:(_mntmmbrs+1)*20]:_dtmd.append(_dtmnt);ret_+='\n\n{}. @!\n'.format(str(_n));_n=_n+1
                    ret_+='\n\n\n「 Toplam {} Kullanici 」'.format(str(len(_dtmd)));self.laylay.sendMention(opTo,ret_,_dtmd)
                
                ############## CANCELALL - FUNCTION ##############
                
            elif opText.startswith('laylaycancel'):
                _m = self.laylay.getChats([opTo]).chats[0].extra.groupExtra.inviteeMids
                _d = []
                for i in _m:
                    _d.append(i)
                    self.laylay.cancelChatInvitation(opTo,[i])
                    time.sleep(1)
                self.laylay.sendMessage(opTo,f"Total {len(_d)} User Cancelled")
                
                ############## KICKALL - FUNCTION ##############
                
            elif opText.startswith('laylayshut'):
                _m = self.laylay.getChats([opTo]).chats[0].extra.groupExtra.memberMids
                _d = []
                for i in _m:
                    _d.append(i)
                    if i != opFrom:
                      self.laylay.deleteOtherFromChat(opTo,[i])
                self.laylay.sendMessage(opTo,f"Total {len(_d)} User Kicked")
                
                ############## BROADCAST - MESSAGE ##############
                
            elif opText.startswith("broadcast "):
                _txt = len('' + 'broadcast') + 1
                bcText = opText[_txt:]
                if time.time()  - self.botData["LiffTokenTime"] > int(86400):
                    self.laylay.TokenCreate()
                    self.botData["LiffTokenTime"] = time.time()
                    self.backupData()
                    print("True")
                else:print("False")
                for groups in self.laylay.getAllChatMids().memberChatMids:
                    if groups not in self.botData["GroupLiffToken"]:
                        self.laylay.TokenSingle(groups)
                    limg = 'https://i.hizliresim.com/ts0xzxx.png'
                    label = "CyberTK ©"
                    data = {
                        "type": "text",
                        "text": "{}".format(bcText),
                        "sentBy": {
                            "label": "%s"%label,
                            "iconUrl": '%s'%limg,
                            "linkUrl": "line://nv/profilePopup/mid=u84e53963a1e708c353e4b16d932e0da0"
                        }
                    }
                    lifftoken = self.botData["GroupLiffToken"][groups]["Token"]
                    self.laylay.SendFlexMessage(data,lifftoken)
                    time.sleep(1)
                self.laylay.sendMessage(opTo,"Tamamdir")
               
                
                ############## UNSEND - MESSAGE ##############
                
            elif opText.startswith('unsend'):
                args=opText.replace('unsend ','');mes=0
                try:mes=int(args)
                except:mes=1
                M=self.laylay.getResend(opTo,101);MId=[]
                for (ind,i) in enumerate(M):
                    if ind==0:pass
                    elif i._from==self.laylay.profile.mid:
                        MId.append(i.id)
                        if len(MId)==mes:break
                def unsMes(id):self.laylay.unsendMessage(id)
                for i in MId:thread1=threading.Thread(target=unsMes,args=(i,));thread1.start();thread1.join()
                self.laylay.sendMessage(opTo,'「 {} message successfully retrieved 」'.format(len(MId)))

            elif opText.startswith('reboot'):
                print ("[ REBOOT-INFO ] BOT REBOOT")
                python = sys.executable
                os.execl(python, python, *sys.argv)
                
        except Exception as r:
               print(r)
                
    def _UserDeleteOtherFromChat(self,_tk):
           pass
    def _NotifInviteIntoChat(self,_tk):
        if _tk.param3 in self.laylay.profile.mid:
            self.laylay.acceptChatInvitation(_tk.param1)
    def _UserNotifLeaveChat(self,_tk):
           pass
    def _UserNotifJoinChat(self,_tk):
           pass
    def _UserNotifUpdateChat(self,_tk):
           pass
    def _UserNotifCancelChat(self,_tk):
           pass
    def _UserNotifRejectChat(self,_tk):
           pass
    def _UserNotifAddFolow(self,_tk):
           pass
    def _UserNotifDellFolow(self,_tk):
           pass
    def _LineUpdateApp(self,_tk):
           pass
