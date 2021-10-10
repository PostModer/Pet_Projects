from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
from data_base import get_data, upload_data

bot = Bot(token="48992a539d8978fa62c65ab7eda662156b2b0800c4977cb91423eb8ed74913044782a9e326346485c0b4f")

KEYBOARD = Keyboard(one_time=True)
KEYBOARD.add(Text("Комплимент", {"cmd": "compliment"}), color=KeyboardButtonColor.NEGATIVE)


@bot.on.private_message(text="Комплимент")
@bot.on.private_message(payload={"cmd": "compliment"})
async def say_compliment(message: Message):
    answ = get_data()
    await message.answer(answ, keyboard=KEYBOARD)


@bot.on.private_message(text="<text>")
async def add_compliment(message: Message, text):
    up_data = upload_data(text)
    await message.answer(f"Добавлен новый комплимент: {up_data}", keyboard=KEYBOARD)


bot.run_forever()
