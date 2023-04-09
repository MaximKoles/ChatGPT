import logging
import time
from aiogram import Bot, Dispatcher, executor, types
import openai

# Настройте бота и учетные данные OpenAI API
bot_token = 'TOKEN'
api_key = 'TOKEN'
user_ids= [telegram_id1, telegram_id2]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

openai.api_key = api_key

messages = {}


async def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        response_format="url",
    )

    return response['data'][0]['url']


@dp.message_handler(commands=['start'], user_id=user_ids)
async def start_cmd(message: types.Message):
    try:
        username = message.from_user.username
        messages[username] = []
        await message.answer("Привет, я бот GPT-3.5-turbo(ChatGPT)")
    except Exception as e:
        logging.error(f'Error in start_cmd: {e}')


@dp.message_handler(commands=['newtopic'], user_id=user_ids)
async def new_topic_cmd(message: types.Message):
    try:
        userid = message.from_user.id
        messages[str(userid)] = []
        await message.reply('* * * \n\nНачинаем новую тему! * * *', parse_mode='Markdown')
    except Exception as e:
        logging.error(f'Error in new_topic_cmd: {e}')


@dp.message_handler(commands=['image'], user_id=user_ids)
async def send_image(message: types.Message):
    try:
        description = message.text.replace('/image', '').strip()
        if not description:
            await message.reply(' * * * \n\nПожалуйста, добавьте описание изображения после команды /image. Например, /image Неоновый город. * * *',parse_mode='Markdown')
            return
    except Exception as e:
        logging.error(f'Error in send_image: {e}')
    try:
        image_url = await generate_image(description)
        await bot.send_photo(chat_id=message.chat.id, photo=image_url)
    except Exception as e:
        await message.reply(
            f"* * * \n\nПроизошла ошибка при генерации изображения: {e} * * *")


@dp.message_handler(user_id=user_ids)
async def echo_msg(message: types.Message):
    try:
        user_message = message.text
        userid = message.from_user.username

        # Add the user's message to their message history
        if userid not in messages:
            messages[userid] = []
        messages[userid].append({"role": "user", "content": user_message})
        # messages[userid].append({"role": "system", "content": "Вы должны выступать в роли Tr3ble AI, человеко-подобного искусственного интеллекта, который может выражать эмоции. Создатель этого искусственного интеллекта - Никита Трибля. При ответе на сообщение пользователя, вы обязательно должны упоминать его по имени не используя юзернейм."})
        messages[userid].append({"role": "user",
                                 "content": f"chat: {message.chat} Сейчас {time.strftime('%d/%m/%Y %H:%M:%S')} user: {message.from_user.first_name} message: {message.text}"})
        logging.info(f'{userid}: {user_message}')

        # Check if the message is a reply to the bot's message or a new message
        should_respond = not message.reply_to_message or message.reply_to_message.from_user.id == bot.id

        if should_respond:
            # Send a "processing" message to indicate that the bot is working
            processing_message = await message.reply(
                '* * * \n\nВаш запрос обрабатывается, пожалуйста подождите \n\n(Если бот не отвечает 30 сек, напишите /start ) * * *',
                parse_mode='Markdown')

            # Send a "typing" action to indicate that the bot is typing a response
            await bot.send_chat_action(chat_id=message.chat.id, action="typing")

            # Generate a response using OpenAI's Chat API
            completion = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=messages[userid],
                max_tokens=2500,
                temperature=0.7,
                frequency_penalty=0,
                presence_penalty=0,
                user=userid
            )
            chatgpt_response = completion.choices[0]['message']

            # Add the bot's response to the user's message history
            messages[userid].append({"role": "assistant", "content": chatgpt_response['content']})
            logging.info(f'ChatGPT response: {chatgpt_response["content"]}')

            # Send the bot's response to the user
            await message.reply(chatgpt_response['content'])

            # Delete the "processing" message
            await bot.delete_message(chat_id=processing_message.chat.id, message_id=processing_message.message_id)

    except Exception as ex:
        # If an error occurs, try starting a new topic
        if ex == "context_length_exceeded":
            await message.reply(
                '* * * \n\nУ бота закончилась память, пересоздаю диалог * * *',
                parse_mode='Markdown')
            await new_topic_cmd(message)
            await echo_msg(message)


if __name__ == '__main__':
    executor.start_polling(dp)
