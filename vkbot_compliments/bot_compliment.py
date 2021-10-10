from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
from data_base import get_data

bot = Bot(token="48992a539d8978fa62c65ab7eda662156b2b0800c4977cb91423eb8ed74913044782a9e326346485c0b4f")

KEYBOARD = Keyboard(one_time=True).add(Text("Комплимент", {"cmd": "compliment"}), color=KeyboardButtonColor.NEGATIVE)


@bot.on.message(text="Комплимент")
@bot.on.message(payload={"cmd": "compliment"})
async def say_compliment(message: Message):
	c = get_data()
	await message.answer(c, keyboard=KEYBOARD)


bot.run_forever()
