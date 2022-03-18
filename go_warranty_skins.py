import cv2, requests, base64, sys, os
from PIL import Image
from io import BytesIO
from glob import glob
from time import time
import re


ssid = []
files = []
img = Image.open(sys.argv[1])
img.load()
with BytesIO() as output:
	img.save(output, 'BMP')
	data = output.getvalue()
img64byte = base64.b64encode(data)
ssid = 'test'

receive = requests.post(url='http://0.0.0.0:9768/warranty',json={'PolicyKey':ssid,'File':img64byte.decode('utf8')},timeout=600)
rec = receive.json()
print(rec)
