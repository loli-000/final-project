# 天氣水情中心
## Build process
* 介紹:  
  * 主題發想來源：
  一開始想做這個其實是因為看到台灣中南部的缺水問題，我們不斷的限水跟缺水，  
  導致他們生活不便，我的構想是可以連結中央氣象局的api跟各個水庫的情況，  
  輸入了地方就可以幫大家算出使否會缺水及限水，因為新聞總在最後撐不住才報出來，  
  我覺得可以提早知道有助於大家提前準備，防範於未然。
  * 目的：  
  讓使用者查詢天氣，了解水情。  

## Details  
* 過程:
  * 一開始先用我們的tocken去獲得api並抓取資料，水利署的api必須設置tocken，成功抓取再做進一步動作  
  抓到資料判斷使用者的輸入，天氣部分我們讀取縣市，把該縣市天氣資訊print出來  
  如果氣溫過高或降雨機率大會發出提醒。  
  水庫因為我們抓了2個api，一個是那個水庫的基本資料，一個是隨時更新的水庫狀況，  
  使用者必須輸入水庫名稱來查詢，利用api的內容判斷是否可能缺水，最後給出提醒。  
  
取得資料API
 ```python
   token = 'CWB-10872B0D-A923-47C9-9517-BC195576D0DB' #憑證
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=' + token + '&format=JSON&locationName=' + str(city)#取得api
    Data = requests.get(url)#對api發出請求
   ```
   
判斷溫度跟降雨機率並發出警訊  
```python
        if int(j["records"]["location"][0]["weatherElement"][1]["time"][i]["parameter"]["parameterName"])>=50:
           print("\n出門請攜帶雨具!")

        if int(j["records"]["location"][0]["weatherElement"][2]["time"][i]["parameter"]["parameterName"]) >=27:
            print("\n氣溫過高請待在家裡不要外出!")
   ```
   
水庫部分抓取兩個API在做資料過濾  
```python
        url = 'https://fhy.wra.gov.tw/WraApi/v1/Reservoir/Station?$select=StationNo%20%2CBasinName%2CStationName%20'
    url2='https://fhy.wra.gov.tw/WraApi/v1/Reservoir/RealTimeInfo?$select=Time%2CWaterHeight%20%2CPercentageOfStorage%20%2CStationNo%20'
    Data = requests.get(url)#對api發出請求
    Data2= requests.get(url2)
    #print(Data2.text)
    j = json.loads(Data.text)#對json資料進行操作
    j2 = json.loads(Data2.text)
   ```
![image](https://github.com/loli-000/final-project/blob/main/%E6%93%B7%E5%8F%96.PNG)  
## API網站:  
https://opendata.cwb.gov.tw/index  
https://fhy.wra.gov.tw/WraApi#!/ReservoirApi/ReservoirApi_Station  
https://fhy.wra.gov.tw/WraApi/v1/Reservoir/Station?$select=StationNo%20%2CBasinName%2CStationName%20  
https://fhy.wra.gov.tw/WraApi/v1/Reservoir/RealTimeInfo?$select=Time%2CWaterHeight%20%2CPercentageOfStorage%20%2CStationNo%20  
