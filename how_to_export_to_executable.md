# Executable export command
The `--add-data` options are crucial. Without using it and adjusting the code whole project seems to export correctly, but then it's not possible to run it - a window pops up and disappears.

```bash
pyinstaller --onefile \
            --windowed \
            --add-data="assets/sounds/anime_wow.mp3:." \
            --add-data="assets/sounds/roblox_oof.mp3:." \
            --add-data="assets/sounds/you_lost.mp3:." \
            --name "Pablo-Tetris" \
            main.py
```
