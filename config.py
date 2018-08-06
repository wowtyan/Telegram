from aiogram.types import inline_keyboard

token = '646915682:AAFWy0MHUlRZ_im220ahihOSXgohAM6EVhc'
welcome_message = '''Привет! Я выгодно выделяю Вас среди менеджеров Telegram.
За счет подачи сообщений сразу с кнопками ответов для админов..
Воспользуйтесь командами для управления:
					 
/help - инструкция, как мной управлять;
/about - почитать историю моего рождения;
/donate - поблагодарить разработчиков и поддержать проект.

'''
stickerpack_name = 'JeanJacques'
yes_sticker = 2
no_sticker = 12


keys = [
	'Y[N>B{7pu.$GG5mQJ_cpr4=}c5xcc;mq',
	'+)4(*_ZRs^xF.e+xtZPb;2DHoAQWOAof',
	')%K#<TiH5-E~_|sb"72BcsE8l~Jqp$7w',
	'LFy8yx30,)sGr^93z)O}w${qs*0fU<a#']

donate_message = '''Вы можеете поблагодарить команду
разработчиков, отправив донейшн.
Напишите в комментариях к переводу @имя своего аккаунта. И
вам придёт придёт лицензионный ключ. Отправьте его мне и я
удалю автопостинг этого сообщения. Оставлю тебе только
команду /donate если вдруг захочешь снова поддержать
проект. Принимаем Visa/MasterCard, ЯндексДеньги, Qiwi,
WebMoney, PayPal, VKpay, с баланса мобильного телефона.'''

donate_keyboard = inline_keyboard.InlineKeyboardMarkup(1)
donate_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='150 руб', url='http://www.donationalerts.ru/r/tyanevgeniy'))
donate_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='Другая сумма', url='http://www.donationalerts.ru/r/tyanevgeniy'))


help_message = '''Команды:
/help - инструкция, как мной управлять;
/about - почитать историю моего рождения;
/donate - поблагодарить разработчиков и поддержать проект.

Инструкция по использованию бота тут:'''
help_keyboard = inline_keyboard.InlineKeyboardMarkup(1)
help_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='Прочитать', url='http://telegra.ph/Instrukciya-po-ispolzovaniyu-bota-08-03'))
	
about_message = '''Бот был готов через 2 дня после
того, как 5 менеджеров сказали,
что у них появилась проблема.
Всю историю созздания и идею
бота почитать тут:'''
about_keyboard = inline_keyboard.InlineKeyboardMarkup(1)
about_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='Прочитать', url='http://telegra.ph/Kak-ya-poyavilsya-na-svet-bez-kesareva-08-03'))
	
