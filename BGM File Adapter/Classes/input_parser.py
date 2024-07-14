import os

def find_audio_file(file_name, method):
    """
    Checks if the file provided exists in the directory or not.
    If no extension was provided it will try to look for a match.
    """
    # find file the simple way
    if os.path.isfile(file_name):
        return file_name
    # if failed try again making ext. explicit
    for ext in ['.wav', '.mp3', '.mid']:
        if os.path.isfile(file_name + ext):
            return file_name + ext
    if method == 2:
        return None
    print("\nCouldn't find file. Make sure it's one of these types: .wav, .mp3, .mid")
    return find_audio_file(input("**Name of file: "), 1)

def parse_tempo(tempo, method):
    """
    Parse the input speed to ensure it's an integer from 50 to 150. Defaults to 100 if empty.
    """
    # default value first so inputs like "BGM" don't trigger the condition
    if not tempo:
        return 100
    # strip non-numeric
    tempo_numeric = ''.join(filter(lambda x: x.isdigit(), tempo))
    try:
        tempo_numeric = int(tempo_numeric)
    except ValueError:
        if method == 2:
            return None
        print("\nPlease ensure the input is numeric.")
        return parse_tempo(input("**Speed of the song: "), 1)
    if 50 <= tempo_numeric <= 150:
        return tempo_numeric
    else:
        if method == 2:
            return None
        print("\nPlease ensure the value is between 50 and 150.")
        print("For BPMs slower than 50, you can use Audacity.\n")
        return parse_tempo(input("**Speed of the song: "), 1)

def compose_output_name(game, file, tempo):
    """
    Takes all user input to format the output file's name to the following:
    [game]_[file]_[tempo]
    """
    game = game.replace(" ", "_")
    file = os.path.basename(file)
    file = file[:-4]
    output_name = f"{game}_{file}_{tempo}.ogg"
    return output_name

# Only method where late return is the expected outcome
def parse_csv(csv):
    """
    Ensures the csv file exists and meets the required conditions:
    Ext. type is either csv or txt AND uses commas as delimeter.
    """
    if not os.path.isfile(csv):
        print("\nCouldn't find the CSV file. Try copy pasting the absolute path if you haven't already.")
        return parse_csv(input("**Name of your CSV file: "))
    _, ext = os.path.splitext(csv)
    if ext not in ['.csv', '.txt']:
        print("\nThe CSV file doesn't use the allowed extensions (.csv and .txt). Please modify the file.")
        return parse_csv(input("**Name of your CSV file: "))
    with open(csv, 'r') as file:
        line = file.readline().strip()
        if ',' not in line:
            print("\nThe CSV file doesn't use commas as delimeters. Please modify the file.")
            return parse_csv(input("**Name of your CSV file: "))
    return csv

def parse_bgm_path(bgm_path):
    """
    Ensures the path to the BGM folder exists.
    Empty string represents CWD which is stored as './' for clarity.
    """
    if not bgm_path:
        return "./"
    if os.path.exists(bgm_path):
        return bgm_path
    print("\nCouldn't find the BGM folder. Try copy pasting the absolute path if you haven't already.")
    return parse_bgm_path(input("**Path to the BGM folder: "))
