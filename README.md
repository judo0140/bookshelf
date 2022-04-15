# 0. 환경 셋업

* src/dxl.py  +  src/test_dxl.py  모두 라즈베리파이의 ~/catkin_ws/src/bookshelf/src 폴더로


![image](https://user-images.githubusercontent.com/61779427/163523419-96849f07-1cf0-4877-bd59-82ac755cd6ea.png)

* 메인 PC 및 라즈베리파이의 ROS 네트워크 설정
* 동일 네트워크망 접속 여부
* ssh 원격 접속을 위한 각 디바이스 ip address 파악
* OpenCR 보드와 12V/5A 파워 연결 여부 및 보드 내 스위치 ON/OFF 여부


# 1. 소프트웨어 셋업

## 1.1 Ubuntu 18.04 ROS melodic 설치
http://wiki.ros.org/melodic/Installation/Ubuntu

## 1.2 라즈베리파이 ROS melodic 설치
http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi

## 1.3 OpenCR 보드 셋업
아두이노IDE 설치 : https://emanual.robotis.com/docs/en/parts/controller/opencr10/#install-on-linux
OpenCR 보드에 다이나믹셀 컨트롤을 위한 펌웨어 업로드 (OpenCR을 u2d2처럼 사용)
1) OpenCR 보드를 아두이노 IDE 실행시킬 메인 보드에 연결
2) 아두이노IDE 실행
3) Tool -> Port -> /dev/ttyACM0 (혹은 ttyUSB0.. 혹은 PC 환경마다 상이) 선택
4) File -> Examples -> OpenCR -> 10.Etc -> usb_to_dxl 클릭
5) 업로드

## 1.4 다이나믹셀 구동을 위한 Dynamixel SDK 패키지 설치
참고 : https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/#repository

Dynamixel SDK 패키지를 설치하고자 하는 디바이스의 터미널(Ctrl + Alt + T) 실행

```
cd ~/catkin_ws/src

git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git

cd ..

catkin_make
```


--------------

# 2. ROS 네트워크 설정

## 2.1 고정 IP 할당
동일 네트워크망 안에서 고정 IP 할당

(참고 : https://raycat.net/5314)

L8326 iptime 공유기 (ssid : bog)의 경우

* PC : 192.168.0.7
* 라즈베리파이1 : 192.168.0.13


## 2.2 ROS ~/.bashrc 파일 수정
1) PC

터미널(Ctrl + Alt + T) 실행 후
```
nano ~/.bashrc
```
네트워크 설정 변경

![Screenshot from 2022-04-08 15-49-08](https://user-images.githubusercontent.com/61779427/162380194-f8f43f7e-526e-4d51-b5f8-51d39432f2d2.png)

파일 저장 (Ctrl + X-> Y -> Enter) 후
```
source ~/.bashrc
``` 
2) 라즈베리파이 (ROS_HOSTNAME에 각 고정 IP)

PC에서 터미널(Ctrl + Alt + T) 실행 후 ssh 원격접속
```
ssh pi@192.168.0.x
```
이후 해당 터미널에서 ~/.bashrc 파일수정

```
nano ~/.bashrc
```
네트워크 설정 변경

![Screenshot from 2022-04-08 15-51-18](https://user-images.githubusercontent.com/61779427/162380446-398d917a-8f0c-43b9-94c3-0036861b85b7.png)

파일 저장(Ctrl+X -> Y -> Enter) 후
```
source ~/.bashrc
```

--------------
# 3. 실행
## 3.1 ROS 및 노드 실행

1) PC

터미널(Ctrl + Alt + T) 실행 후
```
roscore
```

2) 라즈베리파이1

터미널 창을 2개 실행시켜 노드 2개를 실행시켜야 한다

터미널(Ctrl + Alt + T) 실행 후
```
ssh pi@192.168.0.4
```
원격 접속 완료한 터미널에서 노드 실행
```
rosrun bookshelf test_dxl.py
```

## 3.2 조작

노드 실행 시의 다이나믹셀(CAM)의 현재 위치가 's' 입력 시의 위치가 됨

'w', 'x' 는 's' 위치를 기준으로 45degree 회전

----------------
# 4. 하드웨어
## 4.1 프로파일

구매 : 디바이스메이커 서비스 20x20 프로파일 및 볼트, 너트 https://www.devicemart.co.kr/goods/maker?custom=al_profile

## 4.2 다이나믹셀 & OpenCR

구매 : https://www.robotis.com/shop/

참고 : https://emanual.robotis.com/docs/kr/
