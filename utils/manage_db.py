import json

musics_file = "data\\music.json"

async def read_musics():
    with open(musics_file, 'r') as openfile:
        json_object = json.load(openfile)
        return json_object
    

async def add_music(object:dict):
    old_data = await read_musics()
    old_data.append(object)

    json_object = json.dumps(old_data, indent=4)
    with open(musics_file, 'w') as outfile:
        outfile.write(json_object)

