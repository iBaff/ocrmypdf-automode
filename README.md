# ocrmypdf-automode

Usage:

```bash
docker run -d -v <input_directory>:/ocr-in -v <output_directory>:/ocr-out ocrmypdf-automode
```

e.g.:

```bash
docker run -d -v \"$(pwd)\"/test-input:/ocr-in -v \"$(pwd)\"/test-output:/ocr-out ocrmypdf-automode
```

Search for "ToDO:" !


ToDo:

* https://docs.python.org/3/tutorial/datastructures.html
* https://docs.python.org/3/library/subprocess.html
* http://queirozf.com/entries/python-3-subprocess-examples#popen-example-run-command-and-get-return-code
* https://stackoverflow.com/questions/25079140/subprocess-popen-checking-for-success-and-errors
