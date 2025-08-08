# DiarizeWhisper

## Major Caveats
- I havent tested for large audio but small snippets are confirmed working
- It is theoretically capable of detecting multiple speakers but hasnt undergone extensive testing
- Higher quality audio will lead to better results, if you have bad audio I cant help you

## VEM SETUP

### How to set up and activate a venv

```bash
python3 -m venv tx800env
```

This creates a folder called `tx800env` containing the isolated Python environment.
Here we're using `tx800env` but it doesnt specifically matter


### Activate the venv

On macOS/Linux (bash, zsh):

```bash
source tx800env/bin/activate
```

On Windows (PowerShell):

```bash
.\tx800env\Scripts\Activate.ps1
```

When activated, your terminal prompt should usually prefix with (`tx800env`) indicating the venv is active

Additionally you can run the above listed commands to reactivate the venv

### Install dependencies inside the venv

With the venv activated, install your required packages:

```bash
pip install torch
pip install pyannote.audio
pip install whisper
pip install pydub
```

Additionally via homebrew on MacOS

```bash
brew install ffmpeg
```

### Run your script inside the venv

```bash
python /Users/a/transcript.py
```


### To exit the venv

```bash
deactivate
```

### Usefull Info (?)

If you open a new terminal, you must activate the venv again before running your script.
You can freeze your exact package versions with:

```bash
pip freeze > requirements.txt
```

and later install with

```bash
pip install -r requirements.txt
```

## Dependancy Errors

If you encounter any errors these are the fixes to the only two issues Ive seen occuring (Although they are irregular)

```bash
pip install soundfile
pip install numpy
```
