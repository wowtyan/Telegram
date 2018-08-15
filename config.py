from aiogram.types import inline_keyboard

token = '658763297:AAGjIp1W_GerLXrx6WwxL0hVy4HVhuqswsk'
welcome_message = '''Привет! Я выгодно выделяю тебя среди менеджеров
за счет подачи сообщений с кнопками ответов для админов
					 
/help - инструкция, как мной управлять;
/donate - поблагодарить разработчиков и поддержать проект.

'''
stickerpack_name = 'PocketHelperBotStickers'
yes_sticker = 0
no_sticker = 1


keys = [
	'Y[N>B{7pu.$GG5mQJ_cpr4=}c5xcc;mq',
	'+-4-*_ZRs^xF.e+xtZPb;2DHoAQWOAof',
	'-%K#<TiH5-E~_|sb"72BcsE8l~Jqp$7w',
	'LFy8yx30,)sGr^93z)O}w${qs*0fU<a#',
	'iNDz?g@?XX1ttzzHE@6PKkFM42HovNgj',
	'WeVJj~ik?WG3gm$Ux7SAOcmhM0~4$vv$',
	'wy}i}IrLB%hQ@Om5sLwq8Rid7DgOvs$X',
	'CrV%jGr@}#kf2k0#Jt90koOuQqM?wmHM',
	'|8mTi9d}AvV3C$0kWlzKdK*s0AeJFbmQ',
	'pi~F9rFJXsXK?3zlWY6LwWMN4ZtkwxI{',
	'nH@GXjkpaRV}Z@2b*oMS?Uo~lVp}$lyY',
	'{|%}*mqAg04sldmolDz%y32~Scpue5k}',
	'RS#c9?lsd5Oe#B{Cm8gYtJAlgLb~@NsW',
	'?{#FuJgOGaG{EnJT6Ps4X4Ay9OF1lNrw',
	'pOvo16@8X9J7F5|s{MpY~#0k8nK~wMPV',
	'Hbar1@UXKn*M4QrCZ7XxTv1nj~q8$i40',
	'~SawCi3fnCr?|NIb?xW7F9kWXQ~{vMFX',
	'$03t~V%$8Got8*oem}5~zKODmrKNFFoa',
	'jy#k3W74Y#N$MWiWlp0OLF6x2Oom*wJg',
	'6ZnyC7pGNLI4$*lSr~z5ZJRlKKn%QS%x',
	'970H#jF2asfEe3kH1XVmB3VJd8LBxlZT',
	'~SWJlOuH#P*o{UcHu?q{F#NuMs3o#xWf',
	'tsxK~ko}o|~6Vjx2z5eo*HdN2$#~SuB#',
	'nfMPL@zjA~D|9rc|7HgEc|BK%jT*I0~i']

donate_key_message = '''Если тебе понравился бот, то
лучшая благодарность для
нас - поддержка рублём :)
						
От твоей обратной связи зависит скорость
разработки новых ботов для менеджеров и
админов. Принимаем: Visa/MasterCard,
ЯндексДеньги, Qiwi, WebMoney, PayPal,
VKpay, с баланса мобильного телефона.'''

donate_message = '''Благодарю тебя, дорогой друг, что пользуешься ботом!
Если тебе понравился бот, то лучшая благодарность для нас - поддержка рублём :)

Чтобы отключить это авто-сообщение, жми "Выключить".'''

autodonate_keyboard = inline_keyboard.InlineKeyboardMarkup(2)
autodonate_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='Выключить', url='https://telegra.ph/Kak-otklyuchit-avto-soobshchenie-08-14'))
autodonate_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='Поддержать', url='http://www.donationalerts.ru/r/tyanevgeniy'))
	
donate_keyboard = inline_keyboard.InlineKeyboardMarkup(1)
donate_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='Поддержать', url='http://www.donationalerts.ru/r/tyanevgeniy'))

help_message = '''Команды:
/help - инструкция, как мной управлять;

/donate - поблагодарить и поддержать команду проекта.

Инструкция по использованию бота тут:'''
help_keyboard = inline_keyboard.InlineKeyboardMarkup(1)
help_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='Прочитать', url='http://telegra.ph/Instrukciya-po-ispolzovaniyu-bota-08-03'))
	
about_message = '''Все вопросы, пожелания и замечания по
улучшению бота можно написать напрямую разработчику:'''
about_keyboard = inline_keyboard.InlineKeyboardMarkup(1)
about_keyboard.insert(inline_keyboard.InlineKeyboardButton(
	text='Написать', url='t.me/superdev'))
	
