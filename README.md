# translator
Graphical interface running on top of python and the Google Translate API.
## How to use
In the translate from and translate to fields, input the language code of your choice. You must input a language code: https://cloud.google.com/translate/docs/languages
You can use the little lightbulb button to toggle light and dark modes. The folder icon opens the github page, and the question mark button opens the list of language codes online.

Some of the binaries will be flagged by antivirus software (usually Smartscreen on Windows) because these files aren't reputable. I'll try to find a way to sign the files. 
## Using the source code
You'll need Python to run the source code. Download it for your OS here: https://www.python.org/
It should work with any version of Python 3.x, but it's only been tested on Python 3.9.

You will also need to install the following packages:
```
pip install calendar
pip install time
pip install datetime
pip install sys
pip install googletrans==3.1.0a0
```
Run the above commands in the command prompt. Make sure Python is added to PATH.
Note: many of these packages may come preinstalled. It's also important to install this exact version of googletrans as later versions don't support the same API for some reason.

I'm also aware my coding skills are less than mediocre. If you've got ideas for how to optimize the code, you can drop it under the Issues tab (I think?).

## If you don't want the source code...
Head to releases and download.


