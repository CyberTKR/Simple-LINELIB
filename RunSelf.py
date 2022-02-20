# -*- coding: utf-8 -*-

from talk_functions import *
import allCommands
import codecs,livejson

botData = codecs.open("Data.json","r","utf-8")
botData = json.load(botData)

_tkr = APP("androidlite",
           botData=botData)


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




