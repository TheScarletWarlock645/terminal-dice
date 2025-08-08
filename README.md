# Terminal Dice

### TLDR:
> This is just a fun dice roller in terminal I made for DnD and to practice my python :)

## About:
This is a terminal based application for rolling dice. Its pretty simple. Users can choose between a d6, 8, 10, 12, 20, and a coin flip option. Users can also roll multiples of dice, for example: 4d8. If the program is ran again consecutivley, users can sum all of their results together. Have fun.

## Use:
To use the app, start by entering the dice that you've selected, and then the amount of times you would like to roll it (not neccacary with coin flip). After that you will be promted whether you would like to run the app again. If you have already run it, it will prompt you whether you want to sum all of the results you've gathered (though, this option is not available with the coin flip).

## To download:
If you are interested in downloading this project as an actual app, here are the downloads and download instructions.

| Version | Link |
| ----------- | ----------- |
| MacOS (Apple Silicon) | [Terminal Dice - macOS Apple Silicon](https://github.com/TheScarletWarlock645/terminal-dice/releases/download/v12-terminal-dice-macos-arm64/terminal-dice) |
| MacOS (Intel) | [Terminal Dice - macOS Intel](https://github.com/TheScarletWarlock645/terminal-dice/releases/download/v12-terminal-dice-macos-x64/terminal-dice) |
| Windows | [Terminal Dice - Windows x64](https://github.com/TheScarletWarlock645/terminal-dice/releases/download/v12-terminal-dice-windows-x64/terminal-dice.exe) |
| Linux | [ Terminal Dice - Linux x64](https://github.com/TheScarletWarlock645/terminal-dice/releases/download/v12-terminal-dice-linux-x64/terminal-dice) |

### Unix-like Install Instructions:
Download the latest release to your downloads folder, then run the following commands:

```bash
chmod +x ~/Downloads/terminal-dice
mkdir -p ~/.local/bin
cp ~/Downloads/terminal-dice ~/.local/bin
sudo rm ~/Downloads/terminal-dice
export PATH="$HOME/.local/bin:$PATH"
```
### Windows Install Instructions:
Download the latest release to your downloads folder, then run the following commands:

```cmd
cd %USERPROFILE%\Downloads
mkdir %USERPROFILE%\bin
copy terminal-dice.exe %USERPROFILE%\bin\
```
Then to put it in your path:\
\
**command line**
```cmd
setx PATH "%PATH%;%USERPROFILE%\bin"
```
**powershell**
```powershell
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$env:USERPROFILE\bin", [EnvironmentVariableTarget]::User)
```
## To uninstall/remove:
### Unix-like Uninstall Instructions:
Run the following commands to uninstall the app:
```bash
sudo rm ~/.local/bin/terminal-dice
```
Then go into your shell config file and remove lines such as:
```bash
export PATH="$HOME/.local/bin:$PATH"
```
Then reload your shell config.

### Windows Uninstall Instructions:
Run the following commands to uninstall the app:
```cmd
del "%USERPROFILE%\bin\terminal-dice.exe"
```
Then press **Win + R**, type **sysdm.cpl**, and press **Enter**. Click **Environment Variables...**. In **User variables** find **Path** and click **Edit...**. Find and remove your the entry that has your bin directory. Click OK for all dialogs.\
\
## Verify Uninstallation:
**Unix-like:**
```bash
which terminal-dice
```

```cmd
where terminal-dice
```
both commands should return a message similar to "not found".
