# ROBLOX Item Downloader - Downloads Metadata, item model, and thumbnail of an accessory. 
* Mainly meant for [LegacyVerse](https://www.roblox.com/games/12147220287/LegacyVerse-NEW-UPDATE)
* Only tested on Windows

# Requirements
* Basic CMD knowledge
* [Python 3.x.x](https://www.python.org/downloads/)
* Request Module (in CMD, type `pip install requests`)

# How to run
* in Command Prompt: `python RobloxItemDownloader.py`

# NOTES
* Due to changes in ROBLOX APIs, a .ROBLOSECURITY cookie is **required** to use this tool. This is only stored on **your** computer, you can read through the script to prove this.

It is recommended you use a throwaway account anyway, in case you accidentally manage to give it out somehow. Getting the cookie is simple.

1. Press CTRL+SHIFT+I or right click anywhere on the page and click ***Inspect Element***
2. Find the application tab (Storage tab on firefox) and click on it
 * If you cannot find it, then press the + button or resize your browser window
3. Open up cookies, and then ROBLOX then click the listing with the name `.ROBLOSECURITY`
4. Copy and paste the value right next to it and you have your cookie.
5. Open the python script, then paste the cookie when asked.
