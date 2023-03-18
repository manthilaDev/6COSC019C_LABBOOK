import pypandoc
import os
import datetime
from pathlib import Path

docSource = Path('.')
buildSource = Path('../build/_pandoc')

try:
    os.mkdir(buildSource)
except FileExistsError:
    pass
currentDateTime = datetime.datetime.now()
currentDateTimeStr = f'{currentDateTime.year}.{currentDateTime.month}.{currentDateTime.day}-{currentDateTime.hour}:{currentDateTime.minute}:{currentDateTime.second}'
pypandoc.convert_file(docSource.glob('*.md'), 'docx', outputfile=buildSource.joinpath(f'{currentDateTimeStr}-Lab_Log_Book_W1761889.docx'))


