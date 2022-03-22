#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
import re

import dotenv
import imdb
import telebot

from OMDB import get_movie_info

dotenv.load_dotenv()

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

pattern = "^(?:(?!movie_recommend)(?!tv_series_recommend).)*?$"

instance = imdb.IMDb()


@bot.message_handler(commands=["start"])
def start_command(message):
    start_message = "MovieBot v1.0:\n" \
                    "/help - show commands and usage"
    bot.send_message(chat_id=message.chat.id, text=start_message)


@bot.message_handler(commands=["help"])
def help_command(message):
    help_message = "MovieBot v1.0:\n" \
                   "/help - show this info\n" \
                   "/start - start command\n" \
                   "/movie_recommend - movie recommendation\n" \
                   "/tv_series_recommend - tv series recommendation\n" \
                   "your_title - typical usage"
    bot.send_message(chat_id=message.chat.id, text=help_message)


@bot.message_handler(regexp=pattern)
def title_information(your_title):
    if re.fullmatch(pattern, your_title.text):
        bot.send_chat_action(chat_id=your_title.chat.id, action='typing')
        movie_name = your_title.text
        movie_info = get_movie_info(movie_name)

        if movie_info:
            rating_string = f"IMDb Rating: {movie_info['imdb_rating']}\n"
            for rating in movie_info['ratings']:
                rating_string += f"{rating['Source']}: {rating['Value']}\n"

            message_text = (
                        f"{movie_info['title']} ({movie_info['year']}):\n\n" +
                        f"Plot:\n{movie_info['plot']}\n\n" +
                        f"Starring:\n{movie_info['actors']}\n\n" +
                        f"Ratings:\n{rating_string}"
                        )
        else:
            message_text = f"'{movie_name}' не найден. Введите название на \
                            английском языке."

        bot.send_message(chat_id=your_title.chat.id, text=message_text)


@bot.message_handler(content_types=['text'])
def movie_recommendation(movie_recommend):
    bot.send_chat_action(chat_id=movie_recommend.chat.id, action='typing')
    movie = instance.get_top250_movies()
    random.shuffle(movie)

    title = movie[0]
    movie_id = movie[0].movieID
    movie_url = f'https://www.imdb.com/title/tt{movie_id}/'

    msg_text = f'Советую посмотреть: {title} {movie_url}\n'

    bot.send_message(chat_id=movie_recommend.chat.id, text=msg_text)


@bot.message_handler(content_types=['text'])
def tv_series_recommendation(tv_recommend):
    bot.send_chat_action(chat_id=tv_recommend.chat.id, action='typing')
    tv_series = instance.get_top250_tv()
    random.shuffle(tv_series)

    title = tv_series[0]
    tv_series_id = tv_series[0].movieID
    tv_series_url = f'https://www.imdb.com/title/tt{tv_series_id}/'

    msg_text = f'Советую посмотреть: {title} {tv_series_url}\n'

    bot.send_message(chat_id=tv_recommend.chat.id, text=msg_text)


if __name__ == '__main__':
    bot.infinity_polling()
