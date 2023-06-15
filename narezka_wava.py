import os
import wave
import math

def cut_audio_file(file_path, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    with wave.open(file_path, 'rb') as audio_file:
        sample_width = audio_file.getsampwidth()
        sample_rate = audio_file.getframerate()
        num_channels = audio_file.getnchannels()
        total_frames = audio_file.getnframes()
        segment_duration = 10
        segment_frames = int(segment_duration * sample_rate)
        total_segments = math.ceil(total_frames / segment_frames)
        for segment_index in range(total_segments):
            start_frame = segment_index * segment_frames
            end_frame = min((segment_index + 1) * segment_frames, total_frames)
            audio_file.setpos(start_frame)
            segment_data = audio_file.readframes(end_frame - start_frame)
            output_file_path = os.path.join(output_directory, f"segment_{segment_index}.wav")
            with wave.open(output_file_path, 'wb') as segment_file:
                segment_file.setsampwidth(sample_width)
                segment_file.setframerate(sample_rate)
                segment_file.setnchannels(num_channels)
                segment_file.writeframes(segment_data)

    print("Audio file has been cut into segments.")

# Usage example
audio_file_path = "path_to_file_to_cut"
output_directory = "path_to_folder_where_to_store"

cut_audio_file(audio_file_path, output_directory)
