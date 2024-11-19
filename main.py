import urwid


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isdigit() and not char.isalpha() for char in password)


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
