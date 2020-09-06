from user import users

print('Welcome to My Bank')

card_insert = input('Press I to insert your Card: ')

if card_insert in ('I', 'i'):
    attempts = 0
    while attempts < 3: 
        pin_inp = input('Please Enter your PIN: ')
        if int(pin_inp) not in users:
            print('PIN is wrong. Please recheck it.')
            attempts += 1
        else:
            break
    
    # print('Please select the Language')
    languages  = ['Marathi', 'Hindi', 'English']
    for lang_idx, lang in enumerate(languages, start=1):
        print(f'{lang_idx}. {lang}')
    lang = input('Please select the Language: ')
    if lang in ('2', '1'):
        print('Not available now. Sorry for inconvinience. English will be by defalut')
    options =['Withdraw Cash', 'Change PIN', 'Check Balance']
    for opt_idx, opt in enumerate(options, start=1):
        print(f'{opt_idx}. {opt}')
    opt_inp = input('What you want to do: ')
    if opt_inp is '3':
        user_bal = users[int(pin_inp)]['balance']
        print(f'Dear user, your Account balance is: $ {user_bal} only')
    elif opt_inp is '2':
        previous_pin_inp = int(input('Please Enter previous PIN: '))
        new_pin_inp = int(input('Please Enter new PIN: '))

        if previous_pin_inp != new_pin_inp:
            if previous_pin_inp in users:
                users[int(new_pin_inp)] = users.pop(int(previous_pin_inp))
                print(users)
                print('Dear user, your PIN has been updated successfully..!')
            else:
                print('Invalid PIN')
    # else:
else:
    print('Card is necessary')

print('Thanks for visiting our Bank')