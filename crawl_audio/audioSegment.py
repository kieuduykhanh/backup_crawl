from pydub import AudioSegment

sound = AudioSegment.from_file('mp3_folder/10 ĐẠI MỸ NHÂN TRUNG QUỐC15.mp3')

print(len(sound))