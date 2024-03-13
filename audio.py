import json
import subprocess

def lower_dict(d: dict) -> dict:
    return {k.lower():v for k,v in d.items()}

def audio_stream_names(file_path: str) -> list[str]:
    audio_flag = False
    ffprobe_cmd = "ffprobe -hide_banner -show_streams -print_format json " + f'"{file_path}"'
    process = subprocess.Popen(ffprobe_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
    output = json.loads(process.communicate()[0])
    for stream in output["streams"]:
        if(stream['codec_type'] == 'audio'):
            audio_flag = True
            break;

    # if(audio_flag):
    #     print("audio present in the file")
    # else:
    #     print("audio not present in the file")

    audio_streams = []
    # loop through the output streams for more detailed output 
    for stream in output["streams"]:
        stream = lower_dict(stream)
        tags = stream.get("tags")
        if tags:
            tags = lower_dict(tags)
            audio_stream = tags.get("language")
            if audio_stream:
                audio_streams.append(audio_stream)
    return list(set(audio_streams))

def audio_stream_names_safe(file_path: str) -> list[str]:
    try:
        return audio_stream_names(file_path)
    except:
        return []

if __name__ == "__main__":
    print(audio_stream_names("/run/media/felix/hdd/movies/Jurassic World (2015)/Jurassic World.mkv"))