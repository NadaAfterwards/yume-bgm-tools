# BUILD: 2024-07-13 16:45 UTC-03
# Version: 1.0
import csv
import os
import time
import subprocess
from Classes import audio_processor as AudioProcessor
from Classes import input_parser as InputParser
from Classes import text
from datetime import datetime

def method_two(last_completed_index, csv_file, bgm_path):
    with open(csv_file, 'r') as file:
        bgm_list = csv.reader(file)
        # skip rows if resuming a job
        for index, row in enumerate(bgm_list):
            if index < last_completed_index:
                continue
            game_name, input_file, tempo = row
            input_path = os.path.join(bgm_path, input_file)
            print(f"Reading:{game_name},{input_file},{tempo}...")
            time.sleep(1)
            input_file = InputParser.find_audio_file(input_path, 2)
            # skip iteration and log if it errors
            if not input_file:
                print(text.err_audio + "\n")
                with open('log.txt', 'a', encoding='utf-8') as file:
                    file.write(f"{datetime.now()} — INDEX: {index + 1} — ERROR: {text.err_audio} — DATA: {row}\n")
                continue
            tempo = InputParser.parse_tempo(tempo, 2)
            # skip iteration and log if it errors
            if not tempo:
                print(text.err_tempo + "\n")
                with open('log.txt', 'a', encoding='utf-8') as file:
                    file.write(f"{datetime.now()} — INDEX: {index + 1} — ERROR: {text.err_tempo} — DATA: {row}\n")
                continue
            output_file = InputParser.compose_output_name(game_name, input_file, tempo)
            AudioProcessor.process_audio(input_file, output_file, tempo)
            # record progress
            with open('progress.txt', 'r+') as file:
                lines = file.readlines()
                lines[0] = str(index + 1) + "\n"
                file.seek(0)
                file.writelines(lines)
    # reset progress, triggers a new job
    # NOTE: I no longer remember why I'm reseting the count
    # It's probably more logical to just clear the file
    with open('progress.txt', 'r+') as file:
        lines = file.readlines()
        lines[0] = "0\n"
        file.seek(0)
        file.writelines(lines)

print(text.txt_head)
# check for ffmpeg dependency
try:
    subprocess.run(['ffmpeg', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except FileNotFoundError:
    print(text.warn_info)
    input("\nWhen you're ready, press Enter to exit.")
    print("Exiting program...")
    time.sleep(2)
    exit()
print(text.txt_method)
method_chosen = input("**Select a method (1 or 2): ")
while method_chosen not in ['1', '2']:
    print("\nPlease choose either 1 or 2 and try again")
    method_chosen = input("**Select a method (1 or 2): ")

if int(method_chosen) == 1:
    again = True
    while again:
        print(text.txt_game)
        game_name = input("**Name of game: ")
        print(text.txt_file)
        input_file = input("**Name of file: ")
        input_file = InputParser.find_audio_file(input_file, 1)
        print(text.txt_tempo)
        tempo = input("**Speed of the song: ")
        tempo = InputParser.parse_tempo(tempo, 1)
        output_file = InputParser.compose_output_name(game_name, input_file, tempo)
        AudioProcessor.process_audio(input_file, output_file, tempo)
        print("Task completed! You can perform another single file if you want.")
        while True:
            repeat = input("**Would you like to adapt another BGM? (yes/no or y/n): ").strip().lower()
            if repeat in ['yes', 'y']:
                again = True
                break
            elif repeat in ['no', 'n']:
                again = False
                print("Exiting program...")
                time.sleep(2)
                break
            else:
                print("\nI didn't understand your answer, respond only with yes/no or y/n.")

# NOTE: This is fine so long as the user doesn't switch to method 1 after failure
# When they do, the data in progress.txt becomes outdated over time
# Ideally method 1 should clear the txt file or instead, the warning can trigger at BOF
# The later option was the intended idea but was proving difficult to implement...
elif int(method_chosen) == 2:
    # attempt to retrieve previous job info
    try:
        with open('progress.txt', 'r') as file:
            lines = file.readlines()
            x = int(lines[0].strip())
            y = lines[1].strip()
            z = lines[2].strip()
     # if exceptions rise then assume a new job
    except (FileNotFoundError, ValueError, IndexError):
        x = 0
    # an unfinished job is detected
    if x != 0:
        print("\nIt appears the last task ended abruptly, you can resume it with the last recorded inputs.")
        while True:
            resume = input("**Would you like to resume? (yes/no or y/n): ").strip().lower()
            if resume in ['yes', 'y']:
                method_two(x,y,z)
                input("Task completed! Press Enter to exit.")
                print("Exiting program...")
                time.sleep(2)
                exit()
            elif resume in ['no', 'n']:
                # clean progress.txt
                with open('progress.txt', 'w'):
                    pass
                break
            else:
                print("\nI didn't understand your answer, respond only with yes/no or y/n.")
    # start a new job when no prev. job exists or if user didn't want to resume
    print(text.txt_csv)
    print(text.txt_guide)
    csv_file = input("**Name of your CSV file: ")
    csv_file = InputParser.parse_csv(csv_file)
    print(text.txt_path)
    bgm_path = input("**Path to the BGM folder: ")
    bgm_path = InputParser.parse_bgm_path(bgm_path)
    print(f"\nProcessing {csv_file}... if any rows cause errors they will be skipped.")
    print("If the tool exits prematurely, it will resume from the last processed file when re-run.\n")
    time.sleep(5)
    with open('progress.txt', 'w') as file:
        file.write("0\n")
        file.write(csv_file + "\n")
        file.write(bgm_path + "\n")
    method_two(0, csv_file, bgm_path)
    input("Task completed! Press Enter to exit.")
    print("Exiting program...")
    time.sleep(2)
