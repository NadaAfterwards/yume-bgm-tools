# Info
A set of CLI tools aimed at aiding with the process of contributing BGMs files to [Yume Wiki](https://yume.wiki/Main_Page), a MediaWiki dedicated to documenting Yume Nikki fangames.
These tools are designed with the intention of automating all aspects involved when making this sort of contribution. 

From obtaining the information necessary which usually requires either playing the game or importing it in RPG Maker 2000/2003, to modifying the game files to meet the Wiki's [styleguide](https://yume.wiki/YumeWiki:Style_Guide#Audio) and finally uploading these game files and editing the corresponding articles. With these tools the entire process should be streamlined to make it less tedious and less time consuming.

# The Tools
Each tool tackles one aspect of the entire process, this segmentation eases the maintenace of the tools as well as giving the flexibility to the user on picking what aspect they wish to work on.

_As of right now, only BGM File Adapter is publicly available._

**BGM Data Extractor:** A tool designed to obtain all the necessary information by reading through the `RPG_RT.ldb` file contained in each RPG Maker game, powered by [EasyRPG's](https://easyrpg.org/tools/) Tool "LCF2XML".

BGM Data Extractor runs LCF2XML for you and then parses its output to extract the necessary information into a CSV file, this information being: The name of the game, the name of the audio file, the tempo (or speed) in which it plays, the map ID where it plays in-game.

**BGM File Adapter:** This tool handles the modification of the audio files while keeping them in-line to the Yume Wiki styleguide, powered by the [ffmpeg](https://ffmpeg.org/) library used by the [pydub](https://github.com/jiaaro/pydub) package.

Users can select between two methods of file handling, a "one-by-one" mode intended for processing a couple of files or a "batch" mode intended to process several hundred files using the outputted CSV from the previous tool. This tool eliminates the need to manually manipulate each file in programs such as Audacity.

**BGM Wiki Bot (name pending):** With this tool you can take the outputted audio files from the previous tool and alongside the CSV from the first one, upload these files to Yume Wiki and apply them to their respectice location pages. This tool is powered by the [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page) and as such is heavily dependent in authentication and rights to use bots pertaining to Yume Wiki.

All tools are made using Python 3.11 or above, retroactive support is expected to go as far back as Python 3.6 (when f-strings were added) but there are no guarantees. The tools are also expected to be compatible with Windows and Linux systems.

# Usage
This section will only describe BGM File Adapter usage at this time.
### BGM File Adapter
This tool prompts the user with two methods:
> 1.Single File Mode: Input details manually one file at a time -- Slow but user friendly.

> 2.CSV Feed Mode: Provide a CSV formated file to process in batch -- Fast but technical.

***Method one*** is intended for users to familiarize with the program, for each audio file proccessed it will ask the following:
- The name of the game: Users are expected to provide the name with proper casing and following Yume Wiki's namespace conventions. E.g. instead of ".flow" you should input "Dotflow".
- The name of the file: The name of the audio file which can be the three types supported by RPG Maker (.wav, .mp3 and .mid). A relative or absolute path is necessary whenever the file is not within the tool's folder.
- The speed of the song: The speed in which the song plays in-game, represented as a percentage value minus the percentage symbol. I.e. instead of "80%" you should input "80". Speed is capped at a range of 50% to 150%.

Some checks are put in place in case of bad inputs so generally you shouldn't run into issues. Once all the info is accounted for, the program will begin processing the files. After it is done it will ask you if you wish to process another file, restarting method's one process if you respond "yes". Responding "no" will exit the program. An "Output" folder in the program's directory will be generated with all the modified audio files.

***Method two*** is essentially the same thing but rather than prompting you for every single file, you tell the program to get this information from a CSV file instead. When method two is active two things will be asked from you:
- The CSV file: Similar to method one's name of file, if the CSV file is not present within the program's folder a absolute or relative path is necessary.
- Path to BGMs: The path to where all the audio files listed in the CSV are to be fetched from. If you place all the audio files in the same folder, you can leave this one empty.

Once again some checks are in place when prompting the user however you should make sure to know what you are doing as this process can be more delicate. If the CSV file is not one generated by BGM Data Extractor _make sure to follow the pre-requisites as mentioned by the tool_ otherwise the program might traceback.

Once the tool gathered the necessary information it will proceed as method one without any interruptions, this means if there are any issues such as missing audio files or bad speed values these iterations will be skipped entirely. Whenever this happens a "log.txt" file will be generated in the same directory as the tool for you to review the issue(s).

If the tool were to traceback or be interrupted, a failsafe system is in place where it will register to a "progress.txt" file (currently in same directory, future versions will move this to a temp folder) all the necesasry information to resume work from the _last successfully processed file_. Meaning if the tool skipped the last few iterations it will resume before the skipping took place, this gives you a chance to also review any bad data before resuming.

In order to resume you will have to select method two again, future versions of the tool might make it so the user is prompted immediately instead.

# Installation
You can either install Python itself to run the source code or download the provided binary file if you're on Windows. Installing PIP is highly recommended if you opt to run the source code, if you prefer the binary please refer to "False Positives".
### Dependencies
BGM Data Extractor is dependent in the EasyRPG tool [LCF2XML](https://easyrpg.org/tools/). A binary version exists for Windows users.

BGM File Adapter is dependent in both [pydub](https://github.com/jiaaro/pydub) and [ffmpeg](https://ffmpeg.org/).
- Windows users running the source code can simply install pydub via pip `pip install pydub` and the ffmpeg dpendency should be accounted for. Linux users will additionally need to get ffmpeg from their corresponding package manager e.g. `sudo apt install ffmpeg`
- When opting to run the binary for Windows ffmpeg must be downloaded from [here](https://www.ffmpeg.org/download.html) and additionally, its folder must be added to "Path" in Environment Variables. Refer to "Path Env. Variable" for an explanation.
    
BGM Wiki Bot has no known dependencies as of yet.

# False Positives
Binaries are made using [Pyinstaller](https://github.com/pyinstaller/pyinstaller/tree/c7ee9de026c2ed2bf34fc5857347b903baf284c2) which sadly triggers a `Win32/Wacapew.C!ml` detection in Windows Defender and some Anti-Viruses (namely BitDefender). There is not much I can do about this as my only options are to pay for a certificate to sign my code or constantly upload all three programs for review to vendors like [Microsoft](https://www.microsoft.com/en-us/wdsi/filesubmission), each time a tool is updated...

Alas, the tools provided here will unfortunately be flagged as malicious. If this is a concern to you or an annoyance, you can always run the source code directly. You can read about the type of detection [here](https://gridinsoft.com/blogs/win32-wacapew-cml-detection-analysis/).

My idea is that once the tools are unlikely to receive constant updates, I will submit them for analysis to Microsoft to hopefully remove the false positive on Defender.

# Path Env. Variable
Some binaries might require setting up variables in the System Environment Variables, this is generally handled automatically in Linux by your package manager bur Windows users have to do this manually. This essentially means the ability to run a tool like ffmpeg as a command in Command Prompt or PowerShell. For the example mentioned that is how ffmpeg normally works, my tool simply runs the command discretly via pydub's AudioSegment object. Following is a step-by-step guide for Windows users.

Head on to Start and type "env", the following result should come up:
![Look for the "Edit the system environment variables" option](https://i.ibb.co/Ch3PDyC/SEV1.png)

Once opened it will display this window, click on the "Environment Variables..." button at the bottom:
![A window titled "System Properties" will open up, with the tab "Advanced" pre-selected](https://i.ibb.co/zHFWWy5/SEV2.png)

You will now be prompted with a new window. You have the option to set up the Environment Variable for your user (top half) or for the entire system (top bottom), choice is up to you. If a variable "Path" exists select it and click "Edit..." otherwise create it with "New..."
![Another window "Environment Variables" opens up](https://i.ibb.co/Fzt6D2h/SEV3.png)

When clicking "Edit..." you will be prompted with this new window, this displays all the values the variable has:
![Yet another window, the buttoms are on the right side bar](https://i.ibb.co/H7WxWX2/SEV4.png)

Click on the "New" button and then "Browse..." to locate the directory to the program (e.g. ffmpeg):
![Christ almighty Microsoft, more windows. This is that really awful "Browse For Folder" window you might be familiar with](https://i.ibb.co/f0P621J/SEV5.png)

If done correctly you should now be set up. Note that my list of Environment Variables (both user level and system level) are cluttered, your ammount of variables depenends on the current or previous programs you have installed. Same goes for the values of each variable.

Also note that in my case I do not have a value for ffmpeg, this is because my system level Path variable contains the value. I've only shown you my user level Path variable.

To test that everything works you can open Command Prompt or Powershell, in ffmpeg's case you can do `ffmpeg -version` to test if it works:
![Running the command in Power Shell and it spews a bunch of nonsense but nothing about the command not being found](https://i.ibb.co/bbPDZ0r/SEV6.png)

You're now good to go.

If you had to create Path instead of editing then process will be a lot more straightforward, give it the name "Path" and for the value "Browse files..."

# Licensing
For the time being, no licenses are being chosen since I've never coded a tool to be publicly available. But as far as I'm concerned, BGM Tools fall under the [WTFPL](https://en.wikipedia.org/wiki/WTFPL) license. As long as you're not messing with the original repo, it's all game.
