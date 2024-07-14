# warning supression provided by chasemcdo, issue #795 on repo
from warnings import catch_warnings
with catch_warnings(action="ignore", category=RuntimeWarning):
    from pydub import AudioSegment
import os
import time

def change_tempo(input_file, sound, tempo):
    """
    Changes the tempo of the given audio segment.
    tempo < 100 slows down the tempo
    tempo > 100 speeds up the tempo
    """
    print(f"\nAdjusting speed of {os.path.basename(input_file)} to {tempo}%...")
    tempo = float(tempo)/100
    sound_with_changed_tempo = sound._spawn(sound.raw_data, overrides={
         'frame_rate': int(sound.frame_rate * tempo)
      })
    return sound_with_changed_tempo.set_frame_rate(sound.frame_rate)

def extend_to_one_minute(input_file, sound):
    """
    Extends the audio segment to at least one minute by duplicating the track.
    """
    print(f"Looping {os.path.basename(input_file)} to reach 1 minute...")
    original_sound = sound
    while len(sound) < 60000:  # 60000 ms = 1 minute
        sound += original_sound
    return sound

def process_audio(input_file, output_file, tempo):
    """
    Creates the output file with .ogg extension
    """
    output_dir = 'Output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, output_file)
    sound = AudioSegment.from_file(input_file)
    sound = change_tempo(input_file, sound, tempo)
    time.sleep(0.5)
    sound = extend_to_one_minute(input_file, sound)
    time.sleep(0.5)
    sound.export(output_path, format='ogg')
    print(f"Processed audio saved to {output_path}\n")
