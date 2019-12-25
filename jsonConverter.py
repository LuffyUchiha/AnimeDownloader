# import json
#
# with open('anime.json') as json_file:
#     data = json.load(json_file)
#     for p in data:
#         print('Name: ' + p['name'])
#         print('')
from downloader import downloader

url = "http://103.91.144.230/ftpdata/Movies/Hollywood/1900_1999/Billy%20Madison%20%281995%29/Billy.Madison.1995.BluRay.720p.x264.YIFY.mkv"
output = "F:\\Billy Madison.mp4"
prin = "Hell"

downloader(url, output)
