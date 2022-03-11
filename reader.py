import os
import random

path = 'E:\\Pelis'

listaPelis = []


for folder in os.listdir(path):
    listaPelis.append(folder)

new_list0 = [s.replace(".", " ") for s in listaPelis]
new_list1 = [s.replace("1080p", "") for s in new_list0]
new_list2 = [s.replace("BluRay", "") for s in new_list1]
new_list3 = [s.replace("x265-RARBG", "") for s in new_list2]
new_list4 = [s.replace("H264", "") for s in new_list3]
new_list5 = [s.replace("AAC-VXT", "") for s in new_list4]
new_list6 = [s.replace("720p", "") for s in new_list5]
new_list7 = [s.replace("x264-XpoZ", "") for s in new_list6]
new_list8 = [s.replace("AAC-RARBG", "") for s in new_list7]
new_list9 = [s.replace("x264-CM", "") for s in new_list8]
new_list10 = [s.replace("x264-MANiC[rarbg]", "") for s in new_list9]
new_list10 = [s.replace("iNTERNAL BDRip x264-MANiC[rarbg]", "") for s in new_list9]
new_list11 = [s.replace("[", "") for s in new_list10]
new_list12 = [s.replace("]", "") for s in new_list11]
new_list13 = [s.replace("WEBRIP", "") for s in new_list12]
new_list14 = [s.replace("WEBH265-PETRiFiED", "") for s in new_list13]
new_list15 = [s.replace("SECONDSiGH", "") for s in new_list14]
new_list16 = [s.replace("x265-VXT", "") for s in new_list15]
new_list17 = [s.replace("WEB-NAISU", "") for s in new_list16]
new_list18 = [s.replace("PROPER", "") for s in new_list17]
new_list19 = [s.replace("AMZN", "") for s in new_list18]
new_list20 = [s.replace("FLAC", "") for s in new_list19]
new_list21 = [s.replace("x264-HiFi", "") for s in new_list20]
new_list22 = [s.replace("x264-RARBG", "") for s in new_list21]
new_list23 = [s.replace("WEBRip", "") for s in new_list22]
new_list24 = [s.replace("x264-HD4U", "") for s in new_list23]



new_list100 = [s.replace(" ", "") for s in new_list24]


print(len(new_list100))


def aleatorio():
    print(random.choice(new_list100))

aleatorio()