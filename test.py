"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""
import six
import csv
import os
import io
from html import unescape

directory = 'cnn/stories/'
from google.cloud import translate_v2 as translate
t = 0
directory = 'cnn/stories/'
dirs = os.listdir(directory)
text = ""
for file in dirs[0:]:
    try:
        file_name = directory + '/' + file
        with open(file_name, 'r', encoding='utf-8') as filename:
            text = filename.read()  
        translate_client = translate.Client()
        if isinstance(text, six.binary_type):
            text = text.decode('utf-16')
        result = translate_client.translate(
            text, target_language="ar")
     #   print(format(result['translatedText']))
        unescaped = unescape(result['translatedText'])
        with io.open("/home/badawi/GP/Translated/result"+ str(t) +".txt", "w", encoding='utf-16') as f:
            f.write(unescaped)
        t = t + 1
        pass
    except Exception as exception:
        with open('/home/badawi/GP/Errors/rerror' + str(t) + '.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([t, exception])
        t = t + 1
        pass