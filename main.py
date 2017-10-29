import botometer

mashape_key = "QhjGzCLDY4mshX8m9kIubTv6KLb4p1TtzLJjsntXV9HI5WYc3q"
twitter_app_auth = {
    'consumer_key': '2NVO6JJl1Yig7XXuKMoa2PSkl',
    'consumer_secret': 'c9H6PAY9io3IlU3P3H44wihWCX80Ngo25d0RNGDWwGR9Zn6Utn',
    'access_token': '3131597903-eJp1XGXfXJj3iTnPYT0k50chm5p7RMCrZJJPPjG',
    'access_token_secret': 'Wo3iZaFhtDmdhHCAZNjYjFzjf14XwRb8ak93Qd0nVc1Dj',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

# Check a single account
# result = bom.check_account('@clayadavis')
# print result
# Check a sequence of accounts
# accounts = ['@clayadavis', '@onurvarol', '@jabawack', '@ZephrFish', '@DeepDrumpf', '@OfficialKat']

bots = ['@DearAssistant', '@WhatTheFare', '@dscovr_epic', '@pentametron', '@_grammar_']

celebrities = ['@AnnaKendrick47', '@VancityReynolds', '@cher', '@JamesBlunt', '@robdelaney']

additional = ['@sunneversets100', '@BlackManTrump']

trumps = ['@realDonaldTrump', '@DeepDrumpf']

accounts = [bots, celebrities, trumps, additional]


# for i in accounts:
#     for screen_name, result in bom.check_accounts_in(i):
#         # Do stuff
#         pass
#         print screen_name
#         print result
#         print result['scores']['english']
#         print result['scores']['universal']
#     print ""


from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from twitter import process_tweets, compare_accounts
import threading
import Queue

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("view.html")

def func_with_queue(q, f, param):
    res = f(param)
    q.put(res)

@app.route("/check_account", methods=["POST"])
def check_account():
    result = request.json
    if(result and result['user']):
        q1 = Queue.Queue()
        q2 = Queue.Queue()
        processThread1 = threading.Thread(target=func_with_queue, args=(q1,bom.check_account,result['user'],))  # <- note extra ','
        # acc = bom.check_account(result['user'])
        processThread2 = threading.Thread(target=func_with_queue, args=(q2, process_tweets, result['user'],))  # <- note extra ','        
        # pt = process_tweets(result['user'])
        processThread1.start()
        processThread2.start()

        acc_trust = compare_accounts(result['user'])

        processThread1.join()
        processThread2.join()

        acc = q1.get()
        pt = q2.get()
        
        # print acc
        for tweet in pt:
            print tweet[1:]
            val1 = 0
            val2 = 0

            conf = (min(len(tweet[1]),1)*45 + min(len(tweet[2]),1)*45 + min(len(tweet[3]),1)*10 + \
                    min(len(tweet[3]),1)*45 + min(len(tweet[4]),1)*45 + min(len(tweet[5]),1)*10)/2.0

            # link in tweet
            val1 += 10 if len(tweet[1])>0 else 0
            val1 += len(tweet[2])*(-2)
            val1 += len(tweet[3])*(-0.5)

            val2 += len(tweet[4])*2
            val2 += len(tweet[5])*(-2)
            val2 += len(tweet[6])*(-0.5)
            
            val = (1.5*val1 + val2 )/2
            print "val1 %s, val2 %s, VAL %s"%(val1, val2, val)
            print "conf: ", conf

        # print pt
        print acc_trust

    return jsonify({"account":acc, "processed_tweets":pt, "acc_trust":acc_trust, "evaluation":val, "eval_conf":conf})
