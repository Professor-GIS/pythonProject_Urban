# Домашнее задание по теме "Клавиатура кнопок".

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb.row(button_1, button_2)

kb_inl = InlineKeyboardMarkup()
button_inl_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_inl_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_inl.row(button_inl_1, button_inl_2)


class UserState(StatesGroup):
	age = State()
	growth = State()
	weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
	await message.answer('Привет!', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
	await message.answer(text='Выберите опцию:', reply_markup=kb_inl)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
	await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n'
							  'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
	await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
	await call.message.answer('Введите свой возраст (лет):')
	await call.answer()
	await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
	await state.update_data(age=message.text)
	await message.answer('Введите свой рост (см):')
	await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
	await state.update_data(growth=message.text)
	await message.answer('Введите свой вес (кг):')
	await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
	await state.update_data(weight=message.text)
	data = await state.get_data()
	calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age'])
	await message.answer(f"Ваша норма калорий: {calories}")
	await state.finish()


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
