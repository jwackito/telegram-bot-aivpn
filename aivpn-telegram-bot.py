from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from  telegram.ext import Updater
import logging

# initialization
bot_name = 'AIVPN'
token = 'TOKEN-PROVIDED-BY-BOTFATHER'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

# command definition
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! I'm the AIVPN Bot.\nHere is the list of posible commands.\n/getopenvpn to get an OpenVPN configuration file\n/getwireguard to get a WireGuard configuration file")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def getopenvpn(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Here you have. You profile will be valid for 5 hours.")
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('mock_openvpn.conf', 'r'))

openvpn_handler = CommandHandler('getopenvpn', getopenvpn)
dispatcher.add_handler(openvpn_handler)

def getwireguard(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Here you have. You profile will be valid for 5 hours.")
    context.bot.send_document(chat_id=update.effective_chat.id, document=open('mock_wireguard.conf', 'r'))

wireguard_handler = CommandHandler('getwireguard', getwireguard)
dispatcher.add_handler(wireguard_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.\nHere is the list of posible commands.\n/getopenvpn to get an OpenVPN configuration file\n/getwireguard to get a WireGuard configuration file")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
