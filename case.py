import urwid

def on_ask_change(edit, new_edit_text):
    doubled_new_edit_text = new_edit_text*2
    reply.set_text("Вы тайно написали: %s" % doubled_new_edit_text)

ask = urwid.Edit('Тайный ввод: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()