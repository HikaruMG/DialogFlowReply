from flask import Flask, request
from linebot.models import *
from linebot import *

app = Flask(__name__)

line_bot_api = LineBotApi('7p9J2v5He+oKYAPYC+S7tc5/+/3A3FP8zQucXZVHE91EXHzy0D3PcrTMdCOOeSgNnWFGVOearvtHZXHthYbQIfToWJoOzTXpC13fjBUwBVKmD/Idd644LrpSWjLDXuLWJqBiTZbn6GcWm9GTpV2jtQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33afa2d28583bcd3b9cb13b8a925b32d')

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)

    reply(intent,text,reply_token,id,disname)

    return 'OK'

image_message = ImageSendMessage(
            original_content_url='https://www.img.in.th/images/541e47964516df946bc2626b460a06bf.jpg',
            preview_image_url='https://www.img.in.th/images/541e47964516df946bc2626b460a06bf.th.jpg'
            )

def reply(intent,text,reply_token,id,disname):
    if intent == 'mj':
        #text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        #line_bot_api.reply_message(reply_token,text_message)
        line_bot_api.reply_message(reply_token, image_message)
    elif intent == 'intent 5':
        text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        line_bot_api.reply_message(reply_token,text_message)

#def reply(intent,text,reply_token,id,disname):
    #if intent == 'intent 5':
        #text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        #line_bot_api.reply_message(reply_token,text_message)

if __name__ == "__main__":
    app.run()
