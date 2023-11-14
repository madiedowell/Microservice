#Author: Madison Dowell  Date: 11/10/23
# Microservice for Partner

import requests
import random
from time import sleep


while True:
    sleep(1)

    with open("DigiMetInput.txt", "r+", encoding = "utf-8") as f:
        is_get = f.readline()
        if is_get == "get":
            f.truncate(0)
            f.close()

            response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")

            if response.status_code == 200:
                data = response.json()

                if 'total' in data:
                    totalIDs = data['total']

                    if 'objectIDs' in data:
                        objectIDs = data['objectIDs']

                        if objectIDs:
                    
                            index = range(0, totalIDs - 1)
                            random_choice = random.choice(index)
                            output = str(objectIDs[random_choice])
                            with open("DigiMetOutput.txt", "r+", encoding = "utf-8") as f:
                                f.write(output)
                                f.close() 

                        else:
                            print("No object IDs in the response")

                    else:
                        print("No objectIDs key in the response")

                else:
                    print("No total key in the response")

            else:
                print(f"response failed with status code: {response.status_code}")




