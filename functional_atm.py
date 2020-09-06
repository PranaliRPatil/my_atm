from user import users


def display_msg(msg, show_input=0):
    if show_input:
        return input(f'{msg}')
    else:
        return print(msg)


def display_options(opt_list):
    for opt_idx, opt in enumerate(opt_list, start=1):
        print(f'{opt_idx}. {opt}')


print('Welcome to My Bank....!!')
card_insert = display_msg('Press I to insert your Card: ', 1)

if card_insert in ('I', 'i'):
    attempts = 0
    while attempts < 3:
        pin_inp = display_msg('Please Enter your PIN: ', 1)
        if int(pin_inp) not in users:
            display_msg('PIN is wrong. Please recheck it.')
            attempts += 1
        else:
            break

    languages = ['Marathi', 'Hindi', 'English']
    display_options(languages)

    lang = display_msg('Please select the Language: ', 1)

    if lang in ('2', '1'):
        display_msg(
            'Not available now. Sorry for inconvinience. English will be by  default')

    options = ['Withdraw Cash', 'Change PIN', 'Check Balance']
    display_options(options)
    opt_inp = display_msg('What you want to do: ', 1)
    if opt_inp is '3':
        user_bal = users[int(pin_inp)]['balance']
        print(f'Dear user, your Account balance is: $ {user_bal} only')
    elif opt_inp is '2':
        previous_pin_inp = int(display_msg('Please Enter previous PIN: ', 1))
        new_pin_inp = int(display_msg('Please Enter new PIN: ', 1))

        if previous_pin_inp != new_pin_inp:
            if previous_pin_inp in users:
                users[int(new_pin_inp)] = users.pop(int(previous_pin_inp))
                # print(users)
                display_msg(
                    'Dear user, your PIN has been updated successfully..!')
            else:
                display_msg('Invalid PIN')
    # else:
else:
    display_msg('Card is necessary.')

display_msg('Thanks for visiting our Bank. Please Revisit...!!')
