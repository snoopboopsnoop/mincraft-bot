# mincraft-bot
Minecraft minigame in which you cannot say the letter "e" using a Discord bot and Mozilla's deepspeech library.

## Getting Started
In order for the program to function, you must first:
  1. Clone this repo (https://github.com/snoopboopsnoop/mincraft-bot.git) and run npm install
  2. Create a new Discord Application (https://discordapp.com/developers/applications/me) and obtain its Authorization Token
  3. Duplicate example.env and paste the token into its respective field
  4. In read-audio-python, create the following folders:
  ```
  audio
  bruhaudio
  rawaudio
  ```
  *note: rawaudio is used to hold the recorded discord audio in raw format; bruhaudio is used to hold audio in .wav format; audio is used to hold it in 16kHz bitrate. ALL 3 FOLDERS ARE REQUIRED.*
  
  5. Download the pbmm and scorer models of the deepspeech algorithm (https://github.com/mozilla/DeepSpeech/releases) and place them in read-audio-python
  6. Create a Minecraft server and make sure enable-rcon=true, rcon.port=25575, and rcon.password=the password used in test.py (default "password", you should probably change that) in `server.properties`
  7. Run `node main.js` in your terminal as well as `python test.py` in `/read-audio-python`
  8. Add your bot to a server, call `.join`, log into your server, and have fun (maybe, not likely)
