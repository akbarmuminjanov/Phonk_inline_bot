from aiogram import types
from loader import dp
from utils.manage_db import read_musics as MUSIC_DATA
from uuid import uuid4


@dp.inline_handler()
async def empty_query(query: types.InlineQuery):


    my_music = []
    for data in await MUSIC_DATA():
        if query.query in data["title"]:
            my_music.append(types.InlineQueryResultCachedAudio(
                audio_file_id=data["file_id"],
                caption=data["title"],
                id= str(uuid4()),
            ))


    if not my_music:
        # Create a not found query result
        not_found_result = types.InlineQueryResultArticle(
            id=str(uuid4()),
            title= "Music not found",
            description=f"No music matching '{query.query}' was found.",
            input_message_content=types.InputTextMessageContent(
                message_text="Sorry, I couldn't find any music matching your query."
            ),
            thumb_url="https://avatars.steamstatic.com/e5e0c924f026256f96917f4f4e90fa956f0099a6_full.jpg",
            thumb_height=300,
            thumb_width=300,
            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'

        )
        await query.answer([not_found_result])
        # Return only the not found query result

    # my_music.insert(0, not_found_result)
    await query.answer(my_music)