import sys
import io
import urllib.request as test

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

bannerImgUrl = "https://ssl.pstatic.net/tveta/libs/1311/1311450/3bfde8c2b83ab9b4906c_20210106200349743.jpg"
bannerVideoUrl = "https://tvetamovie.pstatic.net/libs/1312/1312873/8922eb69f3ae154e566d_20210105100402999.mp4-pMAIN-v0-f123480-20210105100945077.mp4"

savePath1 = "c:/banner1.jpg"
savePath2 = "c:/banner2.mp4"

#urlopen으로 웹에서 리소스를 read로 읽어와서 f에 할당함.
f1 = test.urlopen(bannerImgUrl).read()
f2 = test.urlopen(bannerVideoUrl).read()

#어디에 저장할건지 파일경로 지정,생성. 옵션 wb 으로 저장을 해라
with open(savePath1,'wb') as saveFile1: #w : write, r : read, a : add / wr : binary로 write할것이다
    saveFile1.write(f1)

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print('다운로드 끝!')

# [Errno 13] Permission denied 오류 발생 : 에디터를 관리자 권한으로 실행 안해서 생긴 문제
