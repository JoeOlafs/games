drinkingGameRules = ('A:	Never Have I Ever',
'2:	Two Sips',
'3:	Hand Out 3 Sips',
'4:	Question Master',
'5:	Sneaky Eyes',
'6:	Thumb',
'7:	Hitler',
'8:	Story',
'9:	Rule',
'10:	Category',
'J:	Two Truths, One Lie',
'Q:	Whore',
'K:	King')
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
def PrintRule(string):
    if string == 'A':
        print('Never Have I Ever')
    elif string == '2':
        print('Two Sips')
    elif string == '3':
        print('Hand Out 3 Sips')
    elif string == '4':
        print('Question Master')
    elif string == '5':
        print('Sneaky Eyes')
    elif string == '6':
        print('Thumb')
    elif string == '7':
        print('Hitler')
    elif string == '8':
        print('Story')
    elif string == '9':
        print('Rule')
    elif string == '10':
        print('Category')
    elif string == 'J':
        print('Two Truths, One Lie')
    elif string == 'Q':
        print('Whore')
    elif string == 'K':
        print('King')
    else:
        print('error')
