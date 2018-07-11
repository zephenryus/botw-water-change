# Breath of the Wild Water Changer

Changes all water to one type in The Legend of Zelda: Breath of the Wild

# Usage

To run the program, locate the `MainField.tscb` file of the field you want to change the water for. This is located in `/content/Terrain/A/`.

**Note:** This script does not overwrite your existing files, but a warning is shown to remind you to backup your files.

The new files are generated to an `output/` directory located in the same directory as the `change_water.py` script. The generated files are further sorted by the type of water material, such as `MainField - Clear Water` or `MainField - Normal Water`. That way you only have to build the files once per water type.

### Drag and Drop

Drag and drop the tscb file onto `change_water.py` (or `change_water.bat` on Windows).

![Drag and Drop Example](https://raw.githubusercontent.com/zephenryus/botw-water-change/master/.github/drag-and-drop.gif "Drag and Drop Example")

![Processing the files](https://raw.githubusercontent.com/zephenryus/botw-water-change/master/.github/console-process.gif "Processing the files")

### From the Commandline

```sh
> python change_water.py path/to/tscb/MainField.tscb
```

### Adding the Files to BotW

1. Navigate to `content/Terrain/A/` in your game files
1. Copy (or move) the generated `MainField - [water type]/` directory from the `output/` directory to  `content/Terrain/A/` in your game files
1. Rename `MainField - [water type]/` to `MainField/`
1. Play the game

![Move the files](https://raw.githubusercontent.com/zephenryus/botw-water-change/master/.github/move-and-rename.gif "Move the files")

# Installation

#### Requirements

* [Python 3+](https://www.python.org/downloads/)
* [SarcLib 0.2](https://pypi.org/project/SarcLib/)
* [libyaz0 0.5](https://pypi.org/project/libyaz0/)

#### Recommended

* pip

`change_water.py` can be extracted anywhere an your system you have permission to make directories and files.

If python and pip are installed, from the commandline run the following commands

1. `pip install SarcLib`
1. `pip install libyaz0`

Without pip you will have to install the modules manually. See [Installing Python Modules (Legacy version)](https://docs.python.org/2.7/install/index.html) for help.