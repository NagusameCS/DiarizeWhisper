# DiarizeWhisper

## VEM SETUP

### How to set up and activate a venv

```
python3 -m venv tx800env
```

This creates a folder called `tx800env` containing the isolated Python environment.
Here we're using `tx800env` but it doesnt specifically matter


### Activate the venv

On macOS/Linux (bash, zsh):

```
source tx800env/bin/activate
```

On Windows (PowerShell):

```
.\tx800env\Scripts\Activate.ps1
```

When activated, your terminal prompt should usually prefix with (`tx800env`) indicating the venv is active

Additionally you can run the above listed commands to reactivate the venv

### Install dependencies inside the venv

With the venv activated, install your required packages:

```
pip install torch
pip install pyannote.audio
pip install whisper
pip install pydub
```


### Run your script inside the venv

```
python /Users/a/transcript.py
```


### To exit the venv

```
deactivate
```

### Usefull Info (?)

If you open a new terminal, you must activate the venv again before running your script.
You can freeze your exact package versions with:

```
pip freeze > requirements.txt
```

and later install with

```
pip install -r requirements.txt
```
