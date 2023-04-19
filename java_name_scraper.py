from bs4 import BeautifulSoup
import requests
import random
import time
url = "https://mcnames.net/username/"


characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

endings = [c1 + c2 + c3 for c1 in characters for c2 in characters for c3 in characters]
random.shuffle(endings)

timetocomplete = len(endings) * 2.1 / 60 / 60
#VERY ROUGH ESTIMATE
print(f"Estimated time to complete {len(endings)} permutations: {timetocomplete} hours")

NOTAVAIL = 0
AVAIL = 0
percentage = 0

for ending in endings:
    percentage += 1
    ratio = percentage / len(endings) * 100 
    timetocomplete = len(endings) - endings.index(ending)
    finaltime = timetocomplete *2.1 / 60 / 60
    

    with open('log.txt', 'a') as f:
            response = requests.get(url + ending)

            soup = BeautifulSoup(response.text, 'html.parser')

            content = soup.find('div', class_='box_profile')

            startindex = 12 + len(ending)
            endofindex = startindex + 3
            avail = content.text[startindex:endofindex]
            if avail == "not":
                    NOTAVAIL += 1
                    time.sleep(random.uniform(0.4, 0.5))

            if avail == "ava":
                print(ending + " is Available")
                f.write(ending)
                f.write(", ")
                AVAIL += 1
                print("Total Available: " + str(AVAIL))
                time.sleep(random.uniform(0.4, 0.5))

            if avail == "it,":
                randtime = random.uniform(2, 7.5)
                print('api limit')
                time.sleep(randtime)
                finaltime += randtime / 3600 #divide by 3600 to convert to hours

            print(f'{round(finaltime, 2)} hours left, {round(ratio, 2)} % Complete | Name {ending}')

print ( f"out of {AVAIL + NOTAVAIL} unique usernames, {AVAIL} are available" )