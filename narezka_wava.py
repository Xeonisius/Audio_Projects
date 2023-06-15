import os
import wave
import math

def cut_audio_file(file_path, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the input audio file
    with wave.open(file_path, 'rb') as audio_file:
        # Get the audio file parameters
        sample_width = audio_file.getsampwidth()
        sample_rate = audio_file.getframerate()
        num_channels = audio_file.getnchannels()
        total_frames = audio_file.getnframes()

        # Calculate the segment duration in frames
        segment_duration = 10  # Segment duration in seconds
        segment_frames = int(segment_duration * sample_rate)

        # Calculate the total number of segments
        total_segments = math.ceil(total_frames / segment_frames)

        # Split the audio file into segments
        for segment_index in range(total_segments):
            # Calculate the start and end frames of the segment
            start_frame = segment_index * segment_frames
            end_frame = min((segment_index + 1) * segment_frames, total_frames)

            # Set the position of the audio file to the start frame
            audio_file.setpos(start_frame)

            # Read the audio data of the segment
            segment_data = audio_file.readframes(end_frame - start_frame)

            # Create the output segment file path
            output_file_path = os.path.join(output_directory, f"segment_{segment_index}.wav")

            # Open the output segment file for writing
            with wave.open(output_file_path, 'wb') as segment_file:
                # Set the audio file parameters for the segment file
                segment_file.setsampwidth(sample_width)
                segment_file.setframerate(sample_rate)
                segment_file.setnchannels(num_channels)

                # Write the audio data to the segment file
                segment_file.writeframes(segment_data)

    print("Audio file has been cut into segments.")

# Usage example
audio_file_path = "path/to/audio_file.wav"
output_directory = "path/to/output_directory"

cut_audio_file(audio_file_path, output_directory)


cut_audio_file(audio_file_path, output_directory)
