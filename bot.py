import random
import string
import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import config
import sql


def random_string(chars):
	return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(chars))


bot = Bot(token=config.token)
dp = Dispatcher(bot)
conn = sqlite3.connect('db.sqlite')
c = conn.cursor()


@dp.message_handler(commands=['start'])
async def send_welcome(message):
	await bot.send_message(message.chat.id, config.welcome_message)
	sql.add_user(c, message.from_user)
	conn.commit()


@dp.message_handler(commands=['help'])
async def send_help(message):
	await bot.send_message(message.chat.id, config.help_message, reply_markup=config.help_keyboard)
	
@dp.message_handler(commands=['empty'])
async def send_about(message):
	await bot.send_message(message.chat.id, config.about_message, reply_markup=config.about_keyboard)

@dp.message_handler(commands=['donate'])
async def send_about(message):
	await bot.send_message(message.chat.id, config.donate_key_message, reply_markup=config.donate_keyboard)
	

@dp.message_handler(content_types=['text'])
async def save_msg(message):
	if message.text in config.keys:
		sql.reg_user(c, message.from_user.id)
		conn.commit()
		await bot.send_message(message.chat.id, 'Лицензионный ключ активирован. Авто-ссобщение отключено.')
		return

	keyboard = types.inline_keyboard.InlineKeyboardMarkup()
	msg_id = random_string(16)
	keyboard.insert(types.inline_keyboard.InlineKeyboardButton(
		text='Отправить', switch_inline_query=msg_id))
	sql.save_message(c, msg_id, message.text)
	conn.commit()
	await bot.send_message(
		message.chat.id, 'Ваше сообщение готово к отправке', reply_markup=keyboard)


@dp.inline_handler(func=lambda inline_query: True)
async def send(query):
	user_id = query.from_user.id
	text = sql.get_message(c, query.query)[1]
	keyboard = types.inline_keyboard.InlineKeyboardMarkup()
	keyboard.insert(types.inline_keyboard.InlineKeyboardButton(
		text='Интересно!', callback_data=f'yes,{user_id}'))
	keyboard.insert(types.inline_keyboard.InlineKeyboardButton(
		text='Не интересно', callback_data=f'no,{user_id}'))
	message = types.input_message_content.InputTextMessageContent(text)
	answer = [types.inline_query_result.InlineQueryResultArticle(
		id=random_string(10),
		title='Отправить',
		input_message_content=message,
		reply_markup=keyboard)]
	await bot.answer_inline_query(query.id, answer)


@dp.callback_query_handler(func=lambda callback_query: True)
async def answer(query):
	stickerpack = await bot.get_sticker_set(config.stickerpack_name)
	yes_sticker = stickerpack.stickers[config.yes_sticker]
	no_sticker = stickerpack.stickers[config.no_sticker]
	answer = query.data.split(',')[0]
	user_id = query.data.split(',')[1]
	user = sql.get_user(c, user_id)
	if not user[4]:
		await bot.send_message(
			user_id, config.donate_message, reply_markup=config.autodonate_keyboard)
	if answer == 'yes':
		await bot.send_message(
			user_id,
			f'@PocketHelperBot: Ответ от [{query.from_user.first_name}](tg://user?id={query.from_user.id})',
			parse_mode='markdown')
		await bot.send_sticker(user_id, yes_sticker.file_id)
	else:
		await bot.send_message(
			user_id,
			f'@PocketHelperBot: Ответ от [{query.from_user.first_name}](tg://user?id={query.from_user.id})',
			parse_mode='markdown')
		await bot.send_sticker(user_id, no_sticker.file_id)
	await query.answer('Ответ отправлен')

if __name__ == '__main__':
	print('bot started')
	executor.start_polling(dp)
