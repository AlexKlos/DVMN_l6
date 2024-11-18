import urwid


def has_digit(password):
    is_digit_tedected = False
    for char in password:
        if char.isdigit():
            is_digit_tedected = True
            break
    return is_digit_tedected

def has_letters(password):
    is_letter_detected = False
    for char in password:
        if char.isalpha():
            is_letter_detected = True
            break
    return is_letter_detected

def has_upper_letters(password):
    is_upper_letter_detected = False
    for char in password:
        if char.isupper():
            is_upper_letter_detected = True
            break
    return is_upper_letter_detected

def has_lower_letters(password):
    is_lower_letter_detected = False
    for char in password:
        if char.islower():
            is_lower_letter_detected = True
            break
    return is_lower_letter_detected

def has_symbols(password):
    is_symbols_detected = False
    for char in password:
        if not char.isdigit() and not char.isalpha():
            is_symbols_detected = True
            break
    return is_symbols_detected

def is_very_long(password):
    return len(password) > 12

def password_rate(password):
    score = 0
    functions_list = (
                      has_digit,
                      has_letters,
                      has_lower_letters,
                      has_upper_letters,
                      has_symbols,
                      is_very_long
    )
    for function in functions_list:
        if function(password):
            score = score + 2
    return score

def on_ask_change(edit, new_edit_text):
    reply.set_text("Рейтинг этого пароля: %s" % password_rate(new_edit_text))

def main():
    ask = urwid.Edit('Введите пароль: ', mask='*')
    global reply
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()

if __name__ == '__main__':
    main()
