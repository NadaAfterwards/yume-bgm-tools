# start
txt_head = """--------------------------BGM adapter by Nada Afterwards---------------------------
                         To exit at any time press Ctrl+C\n
"""
txt_method = """You can process files in two methods:
1.Single File Mode: Input details manually one file at a time -- Slow but user friendly.
2.CSV Feed Mode: Provide a CSV formated file to process in batch -- Fast but technical.

If you're running this tool after using BGM Data Extractor you should choose method #2.
If you previously ran method #2 and encountered an error select it again to resume.
"""
# method 1
txt_game = """\nPlease specify the name of the game as written in Yume Wiki e.g. Dotflow, NostAlgic.
"""
txt_file = """\nPlease provide the exact name of the BGM, you can copy and paste to make it easier.
If you don't provide the file extension the first match for the name will be used.
If it's not stored in the same folder as this tool, including a path is necessary.
You can place a copy of the BGM in the tool's folder to avoid specifying the path.
"""
txt_tempo = """\nNow please specify the speed used by the song in game which ranges from 50% to 150%.
Note that 100% is treated as the default value if you wish to leave this prompt empty.
"""
# method 2
txt_csv = """\nPlease specify the name of the CSV, if made by you check pre-requisites below first.
If it's not stored in the same folder as this tool, including a path is necessary.
You can place a copy of the CSV in the tool's folder to avoid specifying the path.
"""
txt_guide = """----CSV pre-requisites----
- Ensure it's either a .csv or .txt file and only use commas as delimeters.
- Values can be double-quoted or not however single-quotes are not allowed.
- If there's a header row, remove it. The tool does not check for headers.
- Provide these three values in the listed order: Game name, audio file, speed.
- Do not specify the path to the audio files this is done in the next step.
- The speed should be specified as a percentage WITHOUT the % symbol.
"""
txt_path = """\nNow please provide the path for where the tool needs to find the BGMs listed.
In case they're all in the tool's folder, press enter to leave the prompt empty.
"""
# warning messages
warn_info = """WARNING: ffmpeg not detected! Please read below before you proceed:

This tool relies on the ffmpeg library which you can get at: https://www.ffmpeg.org/download.html
The library is crucial to modify audio files, without it the tool simply will not work.
Ensure to download ffmpeg, you can get the 'essentials' version instead of the 'full' version.
Windows users will also need to add its folder to 'Path' in the environment variables.
For a tutorial you can either check my git repository or follow this link:
https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho
"""
# error messages
err_audio = "Could not find the BGM file, skipping..."
err_tempo = "Speed specified is out of range, skipping..."
