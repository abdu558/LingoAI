import pyaudio
import wave
import os

# Function to record audio
def record_audio(filename, record_seconds=5):
    # Set parameters for recording
    chunk = 1024  # Record in chunks of 1024 samples
    format = pyaudio.paInt16  # 16 bits per sample
    channels = 2  # Stereo
    rate = 44100  # Sample rate

    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print(f"Recording for {record_seconds} seconds...")

    frames = []

    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to replace the recorded audio with another audio file
def replace_audio(original_file, replacement_file):
    if os.path.exists(replacement_file):
        os.remove(original_file)
        os.rename(replacement_file, original_file)
        print(f"{original_file} has been replaced with {replacement_file}")
    else:
        print(f"{replacement_file} does not exist")

# Record a new audio file
record_audio('new_recording.wav')

# Replace the recorded audio with another audio file
replace_audio('new_recording.wav', 'saved_audio.wav')