# DiarizeWhisper




## Major Caveats
- I havent tested for large audio but small snippets are confirmed working
- It is theoretically capable of detecting multiple speakers but hasnt undergone extensive testing
- Higher quality audio will lead to better results, if you have bad audio I cant help you

## HF TOKEN

Navigate to this tab and click a `+ Create new token`

<img width="1497" height="824" alt="Screenshot 2025-08-08 at 1 18 26" src="https://github.com/user-attachments/assets/fc89d837-af5a-4a81-b0f3-17c24eb032e6" />

---

Select the `Read` tab, Create a name and click `Create token`
Make sure to copy the token to a secure location as the pop-up will be the only place to access it

<img width="951" height="417" alt="Screenshot 2025-08-08 at 1 21 16" src="https://github.com/user-attachments/assets/1f62ae1a-df8f-44f6-979f-9095914de379" />


## VENV SETUP

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
