"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""
import six
import csv
import os
import io
from html import unescape
from google.cloud import translate_v2 as translate

t = 5570
directory = 'cnn/stories/'
dirs = os.listdir(directory)
translate_client = translate.Client()
unescaped = ""
for file in dirs[5570:]:
    try:
        file_name = directory + '/' + file
		with open("file_name.txt") as fp: 
			Lines = fp.readlines() 
		for line in Lines
			text = line.strip()
        	if isinstance(text, six.binary_type):
            	text = text.decode('utf-16')
        	result = translate_client.translate(
            	text, target_language="ar")
        	print(format(result['translatedText']))
        	unescaped = unescaped + unescape(result['translatedText'])

        with io.open("/home/badawi/GP/test/result"+ str(t) +".txt", "w", encoding='utf-16') as f:
            f.write(unescaped)
        t = t + 1
        pass
    except:
        with open('/home/badawi/GP/Results/rerror' + str(t) + '.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([t, "Exception"])
        t = t + 1
        pass