import pytube
import os
import subprocess

url = input("다운 받을 youtube 영상 주소를 입력하세요 : ")
#url = 'https://www.youtube.com/watch?v=i7fnlJ60RO8&ab_channel=ionix95'
yt = pytube.YouTube(url)
videos = yt.streams.all()

for i in range(len(videos)): #다운받을 수 있는 포맷들 출력
    print(i,',',videos[i])

down_dir = input("다운 받을 경로를 입력하세요 : ")

num = int(input("다운 받을 포맷/화질을 입력하세요 :"))
videos[num].download(down_dir)

fName_new = input("저장할 mp3 파일 이름을 입력하세요 (xxx.mp3) :")
fName_ori = videos[num].default_filename

subprocess.call(['ffmpeg', '-i', os.path.join(down_dir,fName_ori), os.path.join(down_dir,fName_new)])

print("동영상 다운로드 및 mp3 변환 완료되었습니다!")
