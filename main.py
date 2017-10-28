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
result = bom.check_account('@clayadavis')
# print result
# Check a sequence of accounts
# accounts = ['@clayadavis', '@onurvarol', '@jabawack', '@ZephrFish', '@DeepDrumpf', '@OfficialKat']

bots = ['@DearAssistant', '@WhatTheFare', '@dscovr_epic', '@pentametron', '@_grammar_']

celebrities = ['@AnnaKendrick47', '@VancityReynolds', '@cher', '@JamesBlunt', '@robdelaney']

additional = ['@sunneversets100', '@BlackManTrump']

trumps = ['@realDonaldTrump', '@DeepDrumpf']

accounts = [bots, celebrities, trumps, additional]


for i in accounts:
    for screen_name, result in bom.check_accounts_in(i):
        # Do stuff
        pass
        print screen_name
        print result
        print result['scores']['english']
        print result['scores']['universal']
    print ""
