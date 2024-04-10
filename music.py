



# import os
# from mutagen.id3 import ID3
# from mutagen.flac import FLAC
# from mutagen.mp4 import MP4
# from mutagen.oggvorbis import OggVorbis

# # if "cover_art" in metadata:
# #     cover_art_data = metadata["cover_art"]
# #     cover_art_path = os.path.splitext(filename)[0] + ".jpg"  # Generate image path based on filename
# #     with open(cover_art_path, "wb") as f:
# #         f.write(cover_art_data)
# #     metadata["backgroundImage"] = cover_art_path  # Update backgroundImage path

# def extract_metadata(filename):
#     """Extracts metadata from various audio file formats."""

#     if filename.endswith(".mp3"):
#         audio = ID3(filename)
#     elif filename.endswith(".flac"):
#         audio = FLAC(filename)
#     elif filename.endswith(".m4a"):
#         audio = MP4(filename)
#     elif filename.endswith(".ogg"):
#         audio = OggVorbis(filename)
#     else:
#         raise ValueError("Unsupported file format")

#     metadata = {}
#     for key in audio:
#         if key.startswith("TPE"):  # Artist
#             metadata["artist"] = audio[key].text[0]
#         elif key.startswith("TALB"):  # Album
#             metadata["album"] = audio[key].text[0]
#         elif key.startswith("TIT2"):  # Title
#             metadata["title"] = audio[key].text[0]
#         elif key.startswith("TDRC"):  # Year (TDRC for ID3v2.4, TYER for ID3v2.3)
#             metadata["year"] = audio[key].text[0]
#         elif key.startswith("APIC"):  # Cover art
#             metadata["cover_art"] = audio[key].data

#     return metadata


# def write_song_data(song_data, output_file):
#     """Writes song data in the desired format to the output file."""

#     with open(output_file, "a") as f:
#         f.write(str(song_data) + ",\n")

# # Replace with your actual music folder path
# music_folder = r"C:\Users\harib\Documents\music-player-master\assets\music"

# # Output text file
# output_file = "song_data.txt"

# # Clear the output file if it exists
# if os.path.exists(output_file):
#     os.remove(output_file)

# for filename in os.listdir(music_folder):
#     if filename.endswith((".mp3", ".flac", ".m4a", ".ogg")):
#         filepath = os.path.join(music_folder, filename)
#         metadata = extract_metadata(filepath)
#         if "cover_art" in metadata:
#             with open(metadata.get("album", "Unknown")+".jpg", "wb") as f:
#                 f.write(metadata["cover_art"])

#         song_data = {
#             "backgroundImage": metadata.get("album", "Unknown")+".jpg",
#             "title": metadata.get("title", "Unknown"),
#             "album": metadata.get("album", "Unknown"),
#             "year": metadata.get("year", "Unknown"),
#             "artist": metadata.get("artist", "Unknown"),
#             "musicPath": "./assets/music/" + filename
#         }

#         write_song_data(song_data, output_file)
import re
name = "01 - hello-::(helo.com): - | example"  # Example with pipe symbol
if(name.startswith(tuple('0123456789'))==0):
    extracted_name = re.match(r"^(.*?)[\(:\-\|].*$", name).group(1)
    print(extracted_name)  # Output: hello
else:
    name=name[::-1]
    extracted_name = re.match(r"^(.*?)[\(:\-\|].*$", name).group(1)
    print(extracted_name)  # Output: hello
