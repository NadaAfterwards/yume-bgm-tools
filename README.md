# Info
A set of tools aimed at aiding with the process of contributing BGMs files to [Yume Wiki](https://yume.wiki/Main_Page), a MediaWiki dedicated to documenting Yume Nikki fangames.
These tools are designed with the intention of automating all aspects involved when making this sort of contribution. From obtaining the information necessary which usually requires either playing the game or importing it in RPG Maker 2000/2003, to modifying the game files to meet the Wiki's [styleguide](https://yume.wiki/YumeWiki:Style_Guide#Audio) and finally uploading these game files and editing the corresponding articles. With these tools the entire process should be streamlined to make it less tedious and time consuming.
# The Tools
Each tool tackles one aspect of the entire process, this segmentation eases the creation of the tools as well as giving the flexibility to the user on picking what aspect they wish to work on.
As of right now, only BGM File Adapter is publicly available.

**BGM Data Extractor:** A tool designed to obtain all the necessary information by reading through the `RPG_RT.ldb` file contained in each RPG Maker game, powered by [EasyRPG's](https://easyrpg.org/tools/) Tool "LCF2XML". BGM Data Extractor runs LCF2XML for you and then parses its output to extract the necessary information into a CSV file, this information being: The name of the game, the name of the audio file, the tempo (or speed) in which it plays, the map ID where it plays in-game.

**BGM File Adapter:** This tool handles the modification of the audio files while keeping them in-line to the Yume Wiki styleguide, powered by the [ffmpeg](https://ffmpeg.org/) library. Users can select between two methods of file handling, a "one-by-one" mode intended for processing a couple of files or a "batch" mode intended to process several hundred files using the outputted CSV from the previous tool. This tool eliminates the need to manually manipulate each file in programs such as Audacity.

**BGM Wiki Bot (name pending):** With this tool you can take the outputted audio files from the previous tool and alongside the CSV from the first one, upload these files to Yume Wiki and apply them to their respectice location pages. This tool is powered by the [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page) and as such is heavily dependent in authentication and rights to use bots pertaining to Yume Wiki.
