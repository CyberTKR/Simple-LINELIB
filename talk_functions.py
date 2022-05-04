# -*- coding: utf-8 -*-
from thrift.transport.THttpClient import THttpClient
from CyberTK import talkFuncs
from CyberTK.aLLTypes import *
from CyberTKAPI.api import API
from thrift.protocol import TCompactProtocol

from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
import json,threading,requests,time


    
class APP(object):
    def __init__(self,App=None,AccessToken=None,botData=None):
        
        self._linehost = "https://ga2.line.naver.jp"
        self._h = {
            'x-lal': 'tr_TR'
        }
        self.app = App
        self.apiKey = "LosAngeles"
        self.version = "v2"    
        self.botData = botData
        self._unsend = 0
                
        self._completeHeaders()
    
        if AccessToken is not None:
            self._tokenLogin(AccessToken)
        else:
            self._qrLogin()
            
        if self.app != "androidlite":
            try:
                self.gLiffControlGroup()
                self.gLiffControlToken()
            except:pass
        self._tpath = self._RunTransPort("/S4")
        self._ppath = self._RunTransPort("/P4")
        self.liff  = self._LiffTransPort()
        self.revision = -1
        self.globRevison = 0
        self.indRevision = 0
        self.profile = self.getProfile()
        botRunnig = """
        
        CyberTK-Lib/Self/Protect- Mode
        
        
                 * Bot Runnig *
                 
UserName: {}
UserMid: {}
AppName: {}
UserAgent: {}
UserToken: {}
        """
        print(botRunnig.format(self.profile.displayName,self.profile.mid,self._h['X-Line-Application'],self._h['User-Agent'],self._Access))
        self.is_login = True
        if self.is_login:
          Message.__init__(self)
          OperationType.__init__(self)
        

    
################  LOGIN-START #############################

    def _tokenLogin(self,token):
        self._h['X-Line-Access'] = token
        self._Access = token
        
    def _qrLogin(self):
        _appss = self._app(self.app)
        _app = _appss['AppName']
        _uagnt = _appss['UserAgent']

        a = API(self.apiKey,self.version)
        qrResult = a._lineqr(_app,_uagnt)
        print(f'QRCode Image: {qrResult["QrImage"]}')
        print(f'QR: {qrResult["QR"]}')
        pinResult = a._linepin(qrResult['Key'],qrResult['Session'],_app,_uagnt)
        print(f'Pincode: {pinResult["Pincode"]}')
        authResult = a._lineauthToken(qrResult['Key'],qrResult['Session'],_app,_uagnt)
        authToken,certificate = authResult["authToken"],authResult["Certificate"]
        print(f'authToken: {authToken}')
        print(f'Certificate: {certificate}')
        if authToken:
            self._tokenLogin(authToken)
            self.botData["UserToken"] = authToken
            self.backupData()
        
        
    def _app(self,appid):
        _a = API(self.apiKey,self.version)
        _r = _a._appuseragent(appid) # ANDROIDLITE, CHROMEOS, DESKTOPWIN, DESKTOPMAC
        return _r
    
################  LOGIN-END #############################

################  KICK - START #############################

    def _KickeR(self,datas: dict):
        _a = API(self.apiKey,self.version)
        _r = _a._kicker(datas) # ANDROIDLITE, CHROMEOS, DESKTOPWIN, DESKTOPMAC
        return _r

################  KICK - END #############################

################  FETCH & POLL & TRANSPORT - START #############################


    def _r(self, sonuc, Threads=True):
            try:
                while self.is_login:
                    for _o in self._f():
                      if _o.type != 0 and _o.type != -1:
                         if Threads:
                            _td = threading.Thread(target=sonuc(_o))
                            _td.daemon = True
                            _td.start()
            except Exception as e:
                print(f"Error: {e}")
                

    def _f(self):
        while True:
            try:
                __o = self.fetchOps()
                for _o in __o:
                    #print(_o)
                    ___op = _o.type
                    if ___op != -1:
                        self._strv(_o.revision)
                    yield _o
            except Exception as e:
                print(f"Error: {e}")
                
    def _strv(self, revision):
        self.revision = max(revision, self.revision)
        
    def fetchOps(self):
        data=  self._tpath.fetchOps(self.revision,100,self.globRevison,self.indRevision)
        for op in data:
            if op.type == 0:
                if op.revision == -1 and op.param1 != None:
                    a = op.param1.split('\x1e')
                    self._invrv = int(a[0])
                if op.revision == -1 and op.param2 != None:
                    b = op.param2.split('\x1e')
                    self._glbrev = int(b[0])
        return data
    
    def _completeHeaders(self):
        if self.app == "chrome":
                getAppChrome = self._app("chrome")
                self._h['X-Line-Application'] = getAppChrome['AppName']
                self._h['User-Agent'] = getAppChrome['UserAgent']
        elif self.app == "desktopmac":
                getAppMac = self._app("desktopmac")
                self._h['X-Line-Application'] = getAppMac['AppName']
                self._h['User-Agent'] = getAppMac['UserAgent']
        elif self.app == "androidlite":
                getAppAndroid = self._app("androidlite")
                self._h['X-Line-Application'] = getAppAndroid['AppName']
                self._h['User-Agent'] = getAppAndroid['UserAgent']
                
    def _RunTransPort(self, baglam, transPort=True):
        self._runTrans = THttpClient(self._linehost + baglam)
        self._runTrans.setCustomHeaders(self._h)

        self._proto = TCompactProtocol.TCompactProtocol(self._runTrans)
        self._TransData  = talkFuncs.Client(self._proto)
        if transPort:
            self._runTrans.open()

        return self._TransData
    
    def _LiffTransPort(self, isopen=True):
        from liff import LiffService
        self.transport = THttpClient(self._linehost + "/LIFF1")
        self.transport.setCustomHeaders(self._h)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._liff  = LiffService.Client(self.protocol)

        if isopen:
            self.transport.open()

        return self._liff
################  FETCH & POLL & TRANSPORT - END #############################


################  BACKUP - START #############################

    def backupData(self):
        try:
            import codecs
            backup = self.botData
            f = codecs.open('Data.json','w','utf-8')
            json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
            return True
        except Exception as error:
            print(error)
            return False
        
################  BACKUP - END #############################
        
################  LIFF - START #############################
    def SendFlexMessage(self,messages,lifftoken):
        try:
            liff_headers = {
                'Accept' : 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; G730-U00 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Line/9.8.0',
                'Accept-Encoding': 'gzip, deflate',
                'content-Type': 'application/json',
                'X-Requested-With': 'jp.naver.line.android'
            }
            liff_headers["authorization"] = 'Bearer %s'%(lifftoken)
            if type(messages) == list:
                messages = {"messages":messages}
            else:
                messages = {"messages":[messages]}
            _session = requests.Session()
            resp = _session.post("https://api.line.me/message/v3/share", headers=liff_headers, data=json.dumps(messages))
            return resp.text
        except Exception as e:
            print(e)
            
    def TokenCreate(self):
      try:
          self.botData["GroupLiffToken"] = {}
          for groups in self.getAllChatMids().memberChatMids:
                print(groups)
                xyz = LiffChatContext(groups)
                xyzz = LiffContext(chat=xyz)
                view = LiffViewRequest('1656820974-jwLYk4JB', xyzz)
                token = self.liff.issueLiffView(view)
                chatsname = self.getChats([groups]).chats[0].chatName
                self.botData['GroupLiffToken'][groups] = {'Group': chatsname,'Token': token.accessToken}
                self.backupData()
                print(f"Group: {chatsname} \n Token: {token.accessToken}")
      except Exception as e:
          print(e)
          
    def TokenSingle(self,chatMid):
      try:
            xyz = LiffChatContext(chatMid)
            xyzz = LiffContext(chat=xyz)
            view = LiffViewRequest('1656820974-jwLYk4JB', xyzz)
            token = self.liff.issueLiffView(view)
            chatsname = self.getChats([chatMid]).chats[0].chatName
            self.botData['GroupLiffToken'][chatMid] = {'Group': chatsname,'Token': token.accessToken}
            self.backupData()
            print(f"Group: {chatsname} \n Token: {token.accessToken}")
      except Exception as e:
          print(e)
    
################  LIFF - END #############################

################  LIFF TOKEN CONTROL GROUP - START #############################

    def gLiffControlGroup(self):
        for TokenData in self.botData["GroupLiffToken"]:
            if TokenData not in self.getAllChatMids().memberChatMids:
                del self.botData["GroupLiffToken"][TokenData]
                self.backupData()
                break
    def gLiffControlToken(self):
        for groups in self.getAllChatMids().memberChatMids:
            if groups not in self.botData["GroupLiffToken"]:
                self.TokenSingle(groups)
        
################  LIFF TOKEN CONTROL GROUP - END #############################

################  ALL_OPERATIONS - START #############################
    def acceptChatInvitation(self, chatMid):
        return self._tpath.acceptChatInvitation(AcceptChatInvitationRequest(0,chatMid))
    
    def acceptChatInvitation(self, chatMid):
        return self._tpath.acceptChatInvitation(AcceptChatInvitationRequest(0,chatMid))
    
    def acceptChatInvitationByTicket(self, chatMid, ticketId):
        return self._tpath.acceptChatInvitationByTicket(AcceptChatInvitationByTicketRequest(0,chatMid,ticketId))

    def blockContact(self, mid):
        return self._tpath.blockContact(0,mid)
    
    def cancelChatInvitation(self,chatMid, targetUserMids):
        return self._tpath.cancelChatInvitation(CancelChatInvitationRequest(0,chatMid,targetUserMids))
    
    def createChat(self, name, targetUserMids, picturePath=""):
        return self._tpath.createChat(CreateChatRequest(0,0,name,targetUserMids,picturePath))

    def deleteSelfFromChat(self, chatMid):
        return self._tpath.deleteSelfFromChat(DeleteSelfFromChatRequest(0,chatMid,"","","",""))
                                     
    def deleteOtherFromChat(self, chatMid, targetUserMids):
        return self._tpath.deleteOtherFromChat(DeleteOtherFromChatRequest(0,chatMid,targetUserMids))
    
    def fetchOperations(self, deviceId, offsetFrom):
        return self._ppath.fetchOperations(FetchOperationsRequest(deviceId,offsetFrom))

    def findAndAddContactsByMid(self, mid, reference=""):
        return self._tpath.findAndAddContactsByMid(0,mid,0,reference)
    
    def findAndAddContactsByUserid(self, searchId, reference=""):
        return self._tpath.findAndAddContactsByUserid(0,searchId,reference)
    
    def findContactByUserid(self, userid):
        return self._tpath.findContactByUserid(userid)

    def findChatByTicket(self, ticketId):
        return self._tpath.findChatByTicket(FindChatByTicketRequest(ticketId))

    def getAllChatMids(self, withMemberChats=True, withInvitedChats=True, syncReason=0):
        return self._tpath.getAllChatMids(GetAllChatMidsRequest(withMemberChats,withInvitedChats),syncReason)

    def getProfile(self, syncReason=0):
        return self._tpath.getProfile(syncReason)

    def getContact(self, mid):
        return self._tpath.getContact(mid)

    def getCountryWithRequestIp(self):
        return self._tpath.getCountryWithRequestIp()

    def getServerTime(self):
        return self._tpath.getServerTime()

    def getContacts(self, mids):
        return self._tpath.getContacts(mids)

    def getAllContactIds(self, syncReason=0):
        return self._tpath.getAllContactIds(syncReason)

    def getChats(self, chatMids, withMembers=True, withInvitees=True):
        return self._tpath.getChats(GetChatsRequest(chatMids,withMembers,withInvitees))

    def inviteIntoChat(self, chatMid, targetUserMids=[]):
        return  self._tpath.inviteIntoChat(InviteIntoChatRequest(0,chatMid,targetUserMids))
    
    def reissueChatTicket(self, chatMid):
        return self._tpath.reissueChatTicket(ReissueChatTicketRequest(0,chatMid))
    
    def rejectChatInvitation(self, chatMid):
        return self._tpath.rejectChatInvitation(RejectChatInvitationRequest(0,chatMid))
    
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        return self._tpath.sendMessage(0,msg)
    
    def sendMessageReply(self, to, text, msgId):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = 0, {}
        msg.relatedMessageId = msgId
        msg.messageRelationType = 3
        msg.relatedMessageServiceCode = 1
        return self._tpath.sendMessage(0,msg)
    
    def sendMention(self,to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@CyberTK "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
               raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            for mid in mids:
                textx += str(texts[mids.index(mid)])
                slen = len(textx)
                elen = len(textx) + 15
                arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ""
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        return self.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

    def unsendMessage(self, messageId):
        self._unsend += 1
        return self._tpath.unsendMessage(self._unsend, messageId)
    
    def getResend(self, msgid, count=1000):
        return self._tpath.getRecentMessagesV2(msgid, count)
    def updateChat(self, chat, updatedAttribute):
        return self._tpath.updateChat(UpdateChatRequest(0,chat,updatedAttribute))
    
    def updateProfileAttribute(self, attr, value):
        return self._tpath.updateProfileAttribute(0,attr,value)
    
    
################  ALL_OPERATIONS - END #############################
