from pydub import AudioSegment
import math
import os

def split_wav(input_file, output_folder, duration):
    audio = AudioSegment.from_wav(input_file)
    total_duration = len(audio)
    segment_duration = duration * 1000  # Преобразуем длительность в миллисекунды

    num_segments = math.ceil(total_duration / segment_duration)

    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = min((i + 1) * segment_duration, total_duration)

        segment = audio[start_time:end_time]
        output_file = os.path.join(output_folder, f"segment_{i}.wav")
        segment.export(output_file, format="wav")
        print(f"Создан сегмент {output_file}")

# Пример использования
input_file = "D:\\Projects\\dataset\\Audio_Projects-main\\Audio_Projects-main\\input_file.wav"  # Укажите путь к вашему большому WAV-файлу
output_folder = "D:\\Projects\\dataset\\Audio_Projects-main\\Audio_Projects-main\\output_directory"  # Укажите путь к папке, где будут сохранены маленькие WAV-файлы
duration = 10  # Длительность каждого сегмента в секундах

split_wav(input_file, output_folder, duration)
