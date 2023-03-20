# from aiogram import Bot, Dispatcher, executor
# from aiogram.types import Message
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext

# TOKEN = '6025622403:AAFtKYXGSEdXCdrze36B-264ypX2CatwsbI'

# bot = Bot(token=TOKEN)
# my_storage = MemoryStorage()
# disp = Dispatcher(bot, storage=my_storage)

# class MyStates(StatesGroup):
#     firstQ = State()
#     # readName = State()
#     secondQ = State()
#     threeQ = State()

# @disp.message_handler(commands=['start'])
# async def startCmd(message : Message, state : FSMContext) :
#     await message.answer("Привет путник\nОтветь на три вопроса!(ок)")
#     await message.answer("1 вопрос:\n7*121=?")
#     await state.update_data(n=0)
#     await MyStates.firstQ.set()

# @disp.message_handler(content_types='text', state=MyStates.firstQ)
# async def FIRSTQ(message : Message, state : FSMContext):
#     first1 = message.text
#     otvet1 = 847
#     await state.update_data(user1=first1)
#     user_data = await state.get_data()
#     n = int(user_data['n'])
#     if int(first1) == otvet1:
#         n = n + 1
#         await message.answer("1 правельный")
#     await state.update_data(n=n)
#     await message.answer("2 вопрос:\nСтолица Египта?")
#     await MyStates.secondQ.set()

# @disp.message_handler(content_types='text', state=MyStates.secondQ)
# async def SECONDQ(message : Message, state : FSMContext):
#     second2 = message.text
#     otvet2 = "Каир"
#     await state.update_data(user2=second2)
#     user_data = await state.get_data()
#     n = int(user_data['n'])
#     if str(second2) == otvet2:
#         n = n + 1
#         await message.answer("2 правельный")
#     await state.update_data(n=n)
#     await message.answer("3 вопрос:\nСколько костей в человеке?")
#     await MyStates.threeQ.set()

# @disp.message_handler(content_types='text', state=MyStates.threeQ)
# async def SECONDQ(message : Message, state : FSMContext):
#     three2 = message.text
#     otvet3 = 205
#     user_data = await state.get_data()
#     n = int(user_data['n'])
#     if int(three2) == otvet3:
#         n = n + 1
#         await message.answer("3 правельный")
#     await state.update_data(n=n)
#     await state.update_data(user3=three2)
#     user_data = await state.get_data()
#     await message.answer(f"Ответил {user_data['n']}")

# if __name__ == '__main__':
#     executor.start_polling(disp, skip_updates=True)