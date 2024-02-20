import telebot
from telebot import types
from config import *


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text='Викторина: кто ты из животных', callback_data='quiz'),
               types.InlineKeyboardButton(text='Возьми животное под опеку', callback_data='adoption'),
               types.InlineKeyboardButton(text='Контактная информация', callback_data='contacts'))
    file = open('фото/logo.png', 'rb')
    bot.send_photo(message.chat.id, file, 'Приветствуем вас в телеграм боте зоопарка\n'
                                          'Давайте узнаем что-то новое:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['quiz', 'adoption', 'contacts'])
def callback_query(call):
    if call.data == 'quiz':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Mammals/Birds'),
                    types.InlineKeyboardButton(text='Нет', callback_data='Fishes'),
                    types.InlineKeyboardButton(text='Не определился', callback_data='Amphibians'))
        file = open('фото/images.jfif', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Тебе нравится дышать воздухом?)', reply_markup=markup)

    elif call.data == 'contacts':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Пройти викторину', callback_data='quiz'),
                   types.InlineKeyboardButton(text='Подробнее об опекунстве', callback_data='adoption'))
        bot.send_message(call.message.chat.id, 'Для получения более детальной информации\n'
                                               'Звоните по номеру 8-800-555-35-35,\n'
                                               'или посетите сайт зоопарка', reply_markup=markup)

    elif call.data == 'adoption':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Стать опекуном', callback_data='become_guardian'),
               types.InlineKeyboardButton(text='Пройти викторину', callback_data='quiz'),
               types.InlineKeyboardButton(text='Контактная информация', callback_data='contacts'))
        file = open('фото/20151104112611.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, adopt_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "become_guardian")
def become_guardian_callback(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text='пройти викторину ещё раз', callback_data='quiz'),
               types.InlineKeyboardButton(text='Контакты', callback_data='contacts'))

    user_id = call.from_user.id
    bot.send_message(user_id, 'С вами скоро свяжутся')

    another_user_id = 12345  # Заменить на ID сотрудника зоопарка
    bot.send_message(another_user_id, f'Пользователь {user_id} хочет стать опекуном.')


@bot.callback_query_handler(func=lambda call: call.data in ['Mammals/Birds', 'Fishes', 'Amphibians'])
def callback_quiz1(call):
    if call.data == 'Mammals/Birds':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Birds'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Mammals'))

        file = open('фото/1575189885127892731.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'У тебя есть страх высоты?', reply_markup=markup)

    elif call.data == 'Fishes':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Clown'),
                   types.InlineKeyboardButton(text='Нет', callback_data='WingZebra'))
        file = open('фото/images (1).jfif', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Ты любишь шутки смешные?', reply_markup=markup)

    elif call.data == 'Amphibians':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Croc/Tiger'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Zhaba'))
        file = open('фото/images (2).jfif', 'rb')
        bot.send_photo(call.message.chat.id, file, 'ты любил ползать в детстве?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['Birds', 'Mammals', 'Croc/Tiger'])
def callback_quiz2(call):
    if call.data == 'Birds':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Sun'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Glaza'))
        file = open('фото/1541844990165759734.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Ты любишь грется на солныке?', reply_markup=markup)

    elif call.data == 'Mammals':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Vegan'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Hunter'))
        file = open('фото/214774.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Ты вегетарианец?', reply_markup=markup)


    elif call.data == 'Croc/Tiger':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='StupidCroc'),
                   types.InlineKeyboardButton(text='Нет', callback_data='TigerSnake'))
        file = open('фото/Стасяо сан.mp4', 'rb')
        bot.send_video(call.message.chat.id, file,caption='Ты любишь смотреть "Вот такими глазами"???', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['Sun', 'Glaza', 'Vegan', 'Hunter'])
def callback_quiz3(call):
    if call.data == 'Sun':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Goose'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Pechkin'))
        file = open('фото/5ed727c100332565640376.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Ты любишь купатся?', reply_markup=markup)

    elif call.data == 'Glaza':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Splusha'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Butterfly'))
        file = open('фото/Стасяо сан.mp4', 'rb')
        bot.send_video(call.message.chat.id, file, caption='Ты любишь смотреть "Вот такими глазами"???',
                       reply_markup=markup)

    elif call.data == 'Vegan':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Enot'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Banana'))
        file = open('фото/3.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Ты воруешь обьедки с праздничного стола?', reply_markup=markup)

    elif call.data == 'Hunter':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Shakal'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Cold'))
        file = open('фото/3.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Любишь воровать еду из праздничного стола?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['Banana', 'Cold','Pechkin'])
def callback_quiz4(call):
    if call.data == 'Banana':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Makaka'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Squirel'))
        file = open('фото/detail_4c9fd519bc66e04b4a6eb24307a025ad.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Ты любишь бананы?', reply_markup=markup)

    elif call.data == 'Cold':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Bars'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Tiger'))
        file = open('фото/3yv7f.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Ты любишь холод?', reply_markup=markup)
    elif call.data == 'Pechkin':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Да', callback_data='Popugai'),
                   types.InlineKeyboardButton(text='Нет', callback_data='Straus'))
        file = open('фото/3yv7f.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Тебе нравится почтальйон печкин?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['Clown', 'WingZebra', 'Zhaba', 'StupidCroc', 'TigerSnake', 'Splusha',
                                                            'Butterfly', 'Enot', 'Shakal', 'Makaka','Squirel','Bars',
                                                            'Tiger','Goose', 'Popugai', 'Straus'])
def callback_quizresult(call):
    if call.data == 'Clown':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/clown.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Рыба-Клоун!\n'
                                                    f'{text_clown}', reply_markup=markup)
    elif call.data == 'WingZebra':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/wingzebra.jfif', 'rb')
        bot.send_photo(call.message.chat.id, file, f'Вы - Крылатка зебра!\n'
                                                   f'{text_wingzebra}', reply_markup=markup)
    elif call.data == 'Zhaba':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/zhaba.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Жаба!\n'
                                                    f'{text_zhaba}', reply_markup=markup)
    elif call.data == 'StupidCroc':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/crock.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Тупорылый крокодил! (не ну типо вид такой а не ты тупой)))\n'
                                                   f'{text_croc}', reply_markup=markup)
    elif call.data == 'TigerSnake':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/snake.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Тигровый уж!\n'
                                                   f'{text_tigersnake}', reply_markup=markup)
    elif call.data == 'Splusha':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/Splusha_e3019c23a773cf8cee1eef5f8614e30e.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Сплюшка!\n'
                                                   f'{text_splushka}', reply_markup=markup)
    elif call.data == 'Butterfly':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/butterfly.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Совиная бабочка!\n'
                                                   f'{text_butterfly}', reply_markup=markup)
    elif call.data == 'Enot':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/Глад Валакас - Я Енотик - Полоскун.mp4', 'rb')
        bot.send_video(call.message.chat.id, file, caption='Вы - Енотик полоскун!\n'
                                                   f'{text_enot}', reply_markup=markup)
    elif call.data == 'Shakal':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/shakal.jfif', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Обыкновенный шакал!\n'
                                                   f'{text_shakal}', reply_markup=markup)
    elif call.data == 'Makaka':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/makaka.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Японский макак!\n'
                                                   f'{text_makaka}', reply_markup=markup)
    elif call.data == 'Squirel':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/squirel.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Каспийская земляная белка!\n'
                                                   f'{text_squirel}', reply_markup=markup)
    elif call.data == 'Bars':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/bars.png', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Снежный барс!\n'
                                                   f'{text_bars}', reply_markup=markup)
    elif call.data == 'Tiger':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/tiger.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Амурский тигр!\n'
                                                   f'{text_tiger}', reply_markup=markup)
    elif call.data == 'Goose':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/goose.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Серый гусь!\n'
                                                   f'{text_goose}', reply_markup=markup)
    elif call.data == 'Popugai':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/popugai.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Сливочный попугай!\n'
                                                   f'{text_popugai}', reply_markup=markup)
    elif call.data == 'Straus':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text='Поделится результатом в соц сетях', callback_data='.....'),
                   types.InlineKeyboardButton(text='Взять животное под опеку', callback_data='become_guardian'),
                   types.InlineKeyboardButton(text='Хотите попробовать ещё раз?', callback_data='quiz'))
        file = open('фото/straus.jfif', 'rb')
        bot.send_photo(call.message.chat.id, file, 'Вы - Африканский страус!\n'
                                                   f'{text_straus}', reply_markup=markup)





if __name__ == '__main__':
    bot.polling(none_stop=True)