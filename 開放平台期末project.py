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
    print("------------------------------------------------------")
    for i in range(3):#印出需要的欄位        
        print(j["records"]["location"][0]["weatherElement"][0]["time"][i]["startTime"])
        print(j["records"]["location"][0]["weatherElement"][0]["time"][i]["endTime"])
        print(j["records"]["location"][0]["weatherElement"][0]["time"][i]["parameter"]["parameterName"])
        print("降雨機率:", j["records"]["location"][0]["weatherElement"][1]["time"][i]["parameter"]["parameterName"])      
        print("最低溫度:", j["records"]["location"][0]["weatherElement"][2]["time"][i]["parameter"]["parameterName"])
        print("最高溫度:", j["records"]["location"][0]["weatherElement"][4]["time"][i]["parameter"]["parameterName"])

        if int(j["records"]["location"][0]["weatherElement"][1]["time"][i]["parameter"]["parameterName"])>=50:
           print("\n出門請攜帶雨具!")

        if int(j["records"]["location"][0]["weatherElement"][2]["time"][i]["parameter"]["parameterName"]) >=27:
            print("\n氣溫過高請待在家裡不要外出!")
        print("------------------------------------------------------")
        #print(j["records"]["location"][0]["weatherElement"][1]["time"][i]["parameter"]["parameterName"])

def get2(waterbar):    
    token = 'CWB-10872B0D-A923-47C9-9517-BC195576D0DB' #憑證
    url = 'https://fhy.wra.gov.tw/WraApi/v1/Reservoir/Station?$select=StationNo%20%2CBasinName%2CStationName%20'
    url2='https://fhy.wra.gov.tw/WraApi/v1/Reservoir/RealTimeInfo?$select=Time%2CWaterHeight%20%2CPercentageOfStorage%20%2CStationNo%20'
    Data = requests.get(url)#對api發出請求
    Data2= requests.get(url2)
    #print(Data2.text)
    j = json.loads(Data.text)#對json資料進行操作
    j2 = json.loads(Data2.text)
    index=0
    index2=0
    for i in j:
        if waterbar==j[index]["StationName"]:
            print(j[index]["StationNo"])
            print(j[index]["StationName"])
            print(j[index]["BasinName"])
            break
        index+=1
    for i in j2:
        if j[index]["StationNo"]==j2[index2]["StationNo"]:            
            print("水情時間: ",j2[index2]["Time"])
            print("水位高度: ",j2[index2]["WaterHeight"])
            print("蓄水百分比: ",j2[index2]["PercentageOfStorage"])
            if int(j2[index2]["PercentageOfStorage"])<=25:
                print("-------------")
                print("你家沒水囉~")
                print("-------------")
            break
        index2+=1
    
print("輸入查詢縣市: ")
location = input()
print("=====================")
get(location)
print("=====================")
print("輸入水庫名稱:　")
waterbar = input()
print("------------------------------------------------------")
get2(waterbar)
