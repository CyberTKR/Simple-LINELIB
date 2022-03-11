# -*- coding: utf-8 -*-

from talk_functions import *
import allCommands,codecs

botData = codecs.open("Data.json","r","utf-8")
botData = json.load(botData)

# if you will use template don't use androidlite

AppName = "desktopmac"

def runTokenBot(botData, AppName):
    class TokenControl():
      def UserToken(self):
        if botData["UserToken"] != "":
            return True
        else:
            return False
    
    Token = TokenControl()

    try:
       if Token.UserToken() == True:
           _tkr = APP(AppName,botData["UserToken"],botData=botData)
       else:
            _tkr = APP(AppName,botData=botData)
    except TalkException as LineTalkExcept:
        if LineTalkExcept.code == 8:
            try:
                _tkr = APP(AppName,botData=botData)
            except:
                  APP.GoodLinerror(LineTalkExcept)
        else:
            APP.GoodLinerror(LineTalkExcept)
    return _tkr

_tkr = runTokenBot(botData, AppName)


def _p(_tk):
 ############ ALL_USER_SEND_MESSAGE ###############
        if _tk.type == OperationType.SEND_MESSAGE:
            allCommands.Commands(botData,_tkr)._UserSendMessage(_tk)
 ############ ALL_USER_RECEIVE_MESSAGE ###############
        elif _tk.type == OperationType.RECEIVE_MESSAGE:
            allCommands.Commands(botData,_tkr)._UserReceiveMessage(_tk)
 ############ ALL_USER_OPERATIONS ###############
        elif _tk.type == OperationType.NOTIFIED_INVITE_INTO_CHAT:
            allCommands.Commands(botData,_tkr)._NotifInviteIntoChat(_tk)

        elif _tk.type == OperationType.NOTIFIED_LEAVE_CHAT:
            allCommands.Commands(botData,_tkr)._UserNotifLeaveChat(_tk)
            
        elif _tk.type == OperationType.NOTIFIED_UPDATE_CHAT:
            allCommands.Commands(botData,_tkr)._UserNotifUpdateChat(_tk)
            
        elif _tk.type == OperationType.NOTIFIED_ADD_FOLLOW:
            allCommands.Commands(botData,_tkr)._UserNotifAddFolow(_tk)
            
        elif _tk.type == OperationType.NOTIFIED_DELETE_FOLLOW:
            allCommands.Commands(botData,_tkr)._UserNotifDellFolow(_tk)
            
        elif _tk.type == OperationType.NOTIFIED_CHATAPP_UPDATED:
            allCommands.Commands(botData,_tkr)._LineUpdateApp(_tk)
            
        elif _tk.type == OperationType.NOTIFIED_CANCEL_CHAT_INVITATION:
            allCommands.Commands(botData,_tkr)._UserNotifCancelChat(_tk)
            
        elif _tk.type == OperationType.NOTIFIED_ACCEPT_CHAT_INVITATION:
            allCommands.Commands(botData,_tkr)._UserNotifJoinChat(_tk)
            
        elif _tk.type == OperationType.NOTIFIED_REJECT_GROUP_INVITATION:
            allCommands.Commands(botData,_tkr)._UserNotifRejectChat(_tk)
            
        elif _tk.type == OperationType.NOTIFIED_DELETE_OTHER_FROM_CHAT:
            allCommands.Commands(botData,_tkr)._UserDeleteOtherFromChat(_tk)
_tkr._r(_p)
