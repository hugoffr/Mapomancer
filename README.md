# Mapomancer
RPG Map Helper Tool

## The Project
This tool is being built as a helper for RPG Games or for general world building.
It is map-driven so that you can build your map first and then build the world as you go.

It is still a very embrionary project right now.


## Run this project

(Instructions for windows, but other systems might be similar)

### Install an Environment Manager

Install any python environment manager. I prefer to use mamba, so the instructions will center around it. You can find it here https://conda-forge.org/download/.

```
mamba create -n mapomancer
mamba activate mapomancer
pip install pyside6
```

### Run the App

In the root of this project run:
```
mamba activate mapomancer
python main.py
```

### To run the designer app

In the root of this project run:

add `C:\Users\<User>\.local\share\mamba\envs\mapomancer\Scripts` to Windows PATH in the environment variables.

```
mamba activate mapomancer
pyside6-designer.exe
```

You only need to activate the environment once.