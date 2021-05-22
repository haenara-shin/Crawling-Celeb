## git clone https://github.com/Joeclinton1/google-images-download.git
## cd google-images-download && sudo python setup.py install #

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"한지민,수지,박수진,고윤정,아이린,김태희,신세경,문채원,정은지,임윤아,손나은,이연희,장예원,한효주,박보영,한승연,손예진,최지우,강민경,한가인,고아라,박신혜,김태리,아이유,현빈,공유,원빈,장동건,강다니엘,박보검,이동욱,유재석,김종국,이승기,마동석,유아인,하정우,이정재,조승우,김수현,조정석,이준기,이민호, 경수진, 진기주, 박서준, 방성훈, 정경호, 유연석, 이병헌","limit":50,"print_urls":True, "format": 'jpg'}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images