# Ser

A simple Finnish speech recognition example in python.

Use Python3. You might need to install portaudio lib + headers. OS Language should be set to Finnish for proper output, but also note that some OS's might not support Finnish text-to-speech - in that case you can just change
a couple of parameters in run.py to switch to English (naturally you might need to swap the activation keyword and commands).

```
$ pip install -r requirements.txt
$ python run.py
```

Talk!

Keyword to use is "tietokone", so you can say:

"Tietokone aika."

And the system will respond by speaking the time.
