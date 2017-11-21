
# IMPORTANT!
# Didn't want to duplicate comments,
# written_texts_analysis.py contains additional information about these imports,
# what you need to do before using nltk etc
import re
import time
import docx2txt
import nltk
# conf.py contains configuration etc. files used both by written_text_analysis.py and spoken_text_analysis.py
from conf import *

SOURCE_FILE_NAME = "interview02txt.txt"
PARSED_FILE_NAME = "parsed_spoken_texts.txt"