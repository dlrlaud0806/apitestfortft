import requests
import json

headers = {
    "Accept-Language": "ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": "RGAPI-1bfd5c4c-7eae-4652-a016-9f8d7e4d1b90"
}

# Make a GET request to the API endpoint
url = "https://kr.api.riotgames.com/tft/league/v1/challenger"  # Replace with your API endpoint URL
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON data
    data = response.json()

    test =sorted(data['entries'], key= lambda x: -x["leaguePoints"])[:3]
    top3id = [t['summonerId'] for t in test]
    print(top3id)
    puuids=[]
    for id in top3id:
        url = "https://kr.api.riotgames.com/tft/summoner/v1/summoners/"+id
        response = requests.get(url, headers=headers)
        data1 = response.json()
        puuids.append(data1['puuid'])
    matches=[]
    for puuid in puuids:
        url = f'https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count=10'
        response = requests.get(url, headers=headers)
        matches.extend(response.json())

    finals=[]
    for match in set(matches):
        url = f'https://asia.api.riotgames.com/tft/match/v1/matches/{match}'
        response = requests.get(url, headers=headers)
        datas = response.json()
        infos = datas["info"]["participants"]
        for i in infos:
            if i["placement"]==1:
                finals.append(i)
                break

    # Save the data to a file
    filename = "data.json"  # Replace with your desired filename
    with open(filename, "w") as file:
        json.dump(finals, file)

    print("Data saved successfully.")
else:
    print(f"Request failed with status code: {response.status_code}")