import requests, json, xmltodict

raw_data = requests.get(f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey=<API_KEY>&numOfRows=10&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&searchCondition=DAILY').content

xmlObject = xmltodict.parse(raw_data)
# jsonObject = json.loads(json.dumps(xmlObject))

print(type(raw_data))
print(xmlObject)

dataShown = xmlObject['response']['body']['items']['item']

for data in dataShown:
  print(data['dataTime']+'기준 '+ data['cityName']+'의 대기')
  print('아황산가스 농도: ' + data['so2Value'])
  print('일산화탄소 농도: ' + data['coValue'])
  print('오존 농도: ' + data['o3Value'])
  print('이산화질소 농도: ' + data['no2Value'])
  print('미세먼지(pm10) 농도: ' + data['pm10Value'])
  print('미세먼지(pm25) 농도: ' + data['pm25Value'])
  print('-----------------------------')


  #json.dumps: python object => string
  #json.load: file object
  #json.loads: python string parsing
  #class 'bytes': readable by machine
  #class 'sring': readable by human