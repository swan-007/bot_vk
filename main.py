import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from conf import access_token
from decorator import logger
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token=access_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


@logger
def send_some_ms(user_id, message_text, keyboard):
    vk_session.method('messages.send', {'user_id': user_id,
                                        'message': message_text,
                                        'random_id': 0,
                                        'keyboard': keyboard.get_keyboard()})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        ser_id = event.user_id
        keyboard = VkKeyboard()
        keyboard.add_button('start', VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('да', VkKeyboardColor.POSITIVE)
        keyboard.add_button('нет', VkKeyboardColor.NEGATIVE)
        if msg == 'start':
            send_some_ms(ser_id, 'Хочешь найду для тебя идеальную пару?', keyboard)
        elif msg == 'да':
            send_some_ms(ser_id, 'Вот подходящие пары для тебя', keyboard)
        elif msg == 'нет':
            send_some_ms(ser_id, 'Приходи когда будешь готов', keyboard)
