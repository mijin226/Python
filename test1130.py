import csv  ## CSV 파일 처리를 위한 모듈
import matplotlib.pyplot as plt   ## 데이터 시각화를 위한 matplotlib 모듈

## 월별 기온 데이터 파일
temps_file_path = "ta_20241130204917.csv"        

## 월별 지하철 승하차 인원 파일
subway_files = [
    "서울교통공사_월별 승하차인원_20191231.csv",
    "서울교통공사_월별 승하차인원_20201231.csv",
    "서울교통공사_월별 승하차인원_20211231.csv",
    "서울교통공사_월별 승하차인원_20221231.csv",
    "서울교통공사_월별 승하차인원_20231231.csv"
]


avg_temps = []                      ##평균 기온(왼쪽 y축 꺾은선 그래프)
ride_gettingoff_subway = []         ##월별 지하철 승하차 인원(오른쪽 y축 막대그래프)
years = []                          ##2019~2023년도(x축)


## CSV 파일을 읽기 위한 open 함수
with open(temps_file_path, mode='r') as file:
    reader = csv.reader(file)       ## CSV 파일의 내용을 읽어오는 reader 객체 생성

    #8행까지 헤더로 처리(추출 비대상 데이터)
    header = next(reader)
    header = next(reader)        
    header = next(reader)       
    header = next(reader)       
    header = next(reader)       
    header = next(reader)       
    header = next(reader)       
    header = next(reader)       

    ## 파일의 각 행을 순회하며 데이터 처리
    for row in reader:
        #월별 기온 데이터 추출하기
        avg_temp = float(row[2])    ## 3열에서의 실수형태 데이터 변수 선언
        avg_temps.append(avg_temp)  ## 3열데이터 추출

## 데이터 출력
for temp in avg_temps:
    print(temp)                     
