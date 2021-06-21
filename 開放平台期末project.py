
import json
import requests

def get(city):
    token = 'CWB-10872B0D-A923-47C9-9517-BC195576D0DB' #憑證
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=' + token + '&format=JSON&locationName=' + str(city)#取得api
    Data = requests.get(url)#對api發出請求
    #print(Data.text)
    j = json.loads(Data.text)#對json資料進行操作
    print(j["records"]["datasetDescription"])
    print(j["records"]["location"][0]["locationName"])
    for i in range(3):#印出需要的欄位
        print(j["records"]["location"][0]["weatherElement"][0]["time"][i]["startTime"])
        print(j["records"]["location"][0]["weatherElement"][0]["time"][i]["endTime"])
        print(j["records"]["location"][0]["weatherElement"][0]["time"][i]["parameter"]["parameterName"])
        print("降雨機率:", j["records"]["location"][0]["weatherElement"][1]["time"][i]["parameter"]["parameterName"])
        print("最低溫度:", j["records"]["location"][0]["weatherElement"][2]["time"][i]["parameter"]["parameterName"])
        print("最高溫度:", j["records"]["location"][0]["weatherElement"][4]["time"][i]["parameter"]["parameterName"])
        #print(j["records"]["location"][0]["weatherElement"][1]["time"][i]["parameter"]["parameterName"])

print("輸入查詢縣市: ")
location = input()
print("=====================")
get(location)
