import os
import time
import signal
import subprocess
from pathlib import Path
# https://inotify-simple.readthedocs.io/en/latest/          https://pypi.org/project/inotify-simple/
from inotify_simple import INotify, flags

# Constants
ocr_in_path = Path('/ocr-in')
ocr_out_path = Path('/ocr-out')
# local testing
# ocr_in_path = Path(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'test-input')))
# ocr_out_path = Path(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'test-output')))
# print(ocr_in_path)
# print(ocr_out_path.absolute())

if (not ocr_in_path.exists()):
    ex_text = ocr_in_path.absolute().as_posix() + ' does not exist!'
    raise Exception(ex_text, 'Please bind to docker.')

if (not ocr_out_path.exists()):
    ex_text = ocr_out_path.absolute().as_posix() + ' does not exist!'
    raise Exception(ex_text, 'Please bind to docker.')

if (not ocr_in_path.is_dir()):
    ex_text = ocr_in_path.absolute().as_posix() + ' is not a directory!'
    raise Exception(ex_text, 'Please bind to docker.')

if (not ocr_out_path.is_dir()):
    ex_text = ocr_out_path.absolute().as_posix() + ' is not a directory!'
    raise Exception(ex_text, 'Please bind to docker.')

inotify = INotify()
watch_flags = flags.CREATE
wd = inotify.add_watch(ocr_in_path.absolute().as_posix(), watch_flags)

# https://stackoverflow.com/a/41753517/1781686
run = True


def signal_handler(signum, frame):
    global run
    run = False
    global inotify, wd
    inotify.rm_watch(wd)
    inotify.close()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

last_file_name = ''

try:
    while(run):
        time.sleep(1)
        for event in inotify.read():
            if(event.name != last_file_name):
                # Sometimes CREATE trigger twice or trice :)
                last_file_name = event.name
                file_in = ocr_in_path / last_file_name
                if (not file_in.as_posix().endswith('.pdf')):
                    # if file is not pdf continue with next file
                    print(last_file_name + ' had no .pdf suffix.')
                    continue
                print(file_in)
                file_out = ocr_out_path / last_file_name
                # Call ocrmypdf
                ocr = subprocess.Popen(['/usr/local/bin/ocrmypdf',
                    '--optimize', '1',
                    '-l', 'deu+eng',
                    '--clean',
                    '--deskew',
                    '--rotate-pages',
                    file_in.as_posix(),
                    file_out.as_posix()
                ])
                print('Return Code:' + str(ocr.returncode))
                print(ocr.returncode)
except ValueError as err:
    pass
finally:
    print('Bye!')
