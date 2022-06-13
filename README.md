# dynmap_scanner
A tool to log everything that happens on a minecraft dynmap

Simply clone to repository and modify the config file to add in the dynmap's url and the dimension's name (more than likely it will just be "world")
The tool will ping the dynmap every 30seconds and will log:
Chat messages, player leave and join, current player count, weather status and for every player will log their coordinates, their health, their armor.
All logs will also come with a timestamp so you can know when it happened
timestamp is in the unix-millisecond format.

