# final-project
開放平台期末作業  
1.介紹:  
這個project主要是在做天氣預報，及水情查看
但是輸入有限制，台北市不能輸入臺北市,臺南市要輸入臺南市  

  
2.背景構想:  
一開始想做這個其實是因為看到台灣中南部的缺水問題，我們不斷的限水跟缺水，  
導致他們生活不便，我的構想是可以連結中央氣象局的api跟各個水庫的情況，  
輸入了地方就可以幫大家算出使否會缺水及限水，因為新聞總在最後撐不住才報出來，  
我覺得可以提早知道有助於大家提前準備，防範於未然。

3.code講解:  
一開始先用我們的tocken去獲得api並抓取資料，水利署的api必須設置tocken，成功抓取再做進一步動作  
抓到資料判斷使用者的輸入，天氣部分我們讀取縣市，把該縣市天氣資訊print出來  
如果氣溫過高或降雨機率大會發出提醒。  
水庫因為我們抓了2個api，一個是那個水庫的基本資料，一個是隨時更新的水庫狀況，  
使用者必須輸入水庫名稱來查詢，利用api的內容判斷是否可能缺水，最後給出提醒。

![image](https://github.com/loli-000/final-project/blob/main/%E6%93%B7%E5%8F%96.PNG)  
4.
https://opendata.cwb.gov.tw/index  
https://fhy.wra.gov.tw/WraApi#!/ReservoirApi/ReservoirApi_Station  
https://fhy.wra.gov.tw/WraApi/v1/Reservoir/Station?$select=StationNo%20%2CBasinName%2CStationName%20  
https://fhy.wra.gov.tw/WraApi/v1/Reservoir/RealTimeInfo?$select=Time%2CWaterHeight%20%2CPercentageOfStorage%20%2CStationNo%20  
