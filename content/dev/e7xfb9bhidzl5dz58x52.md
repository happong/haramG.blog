---
title: 젠킨스 URL주소가 기억이 안날 경우
dashboard_id: e7xfb9bhidzl5dz58x52
category: dev
status: draft
stage: draft
visited: 2026-10-22
planned: 
published: 
tistory_done: false
tistory_published: 
season: false
season_end: 
priority: 3
photos: 0
place_shots: 0
no_place: true
---

## 경험 메모

내가 생성한 젠킨스 접속 URL주소가 기억이 아나는 경우 찾을 수 있는 방법에 대한 가이드입니다. 
- 기본적으로 http://localhost:8080으로 접속을 하거나 https://IP:8080으로 접속을 할 수 있으나, 포트를 다르게 설정을 했다면 jenkins파일을 확인하여 포트 번호를 확인할 수 있습니다. 
jenkins.xml파일에서 확인할 수 있고, 경로를 변경하지 않았다면 아래 경로에서 확인이 가능합니다. 
경로 : 내pc:\c:\program files\jenkins\jenkins.xml
해당 파일을 우클릭 후 메모장으로 엽니다. 
컨트롤 + 에프 클릭하여 Port를 검색합니다.  
그럼 아래처럼 포트를 확인할 수 있습니다.

## 네이버 초안

[확인 필요 — 확인 후 이 블록은 지우고 올려주세요]
- 제목 제안: 젠킨스(Jenkins) 접속 URL 주소가 기억이 안 날 때 포트 번호 찾는 방법
- 메모에는 "https://IP:8080"으로 되어 있었는데, 젠킨스 공식 설치 문서와 설치 파일 설정 기준으로 기본 설치는 http로 열려요. 그래서 "http://IP:8080"으로 고쳤어요. https를 따로 설정해서 쓰고 계신 거라면 알려주세요.
- 메모 마지막 "아래처럼 포트를 확인할 수 있습니다" 부분에 들어갈 캡처가 없어요. [사진] 자리에 jenkins.xml에서 포트를 찾은 화면을 넣어주세요.
- 이 방법은 Windows에 젠킨스 설치 프로그램(MSI)으로 설치한 경우 기준이에요.

안녕하세요! 하해입니다.

오늘은 내가 만든 젠킨스 접속 URL 주소가 기억이 안 날 때, 주소를 찾는 방법을 정리해보려고 해요.
젠킨스를 한 번 설치해두고 한동안 안 들어가다 보면, 주소가 뭐였는지 헷갈릴 때가 있잖아요?
그럴 때 이 방법으로 포트 번호를 찾으면 바로 다시 접속할 수 있어요!

✅ 기본 접속 주소

기본적으로는 아래 주소로 접속할 수 있어요.

- 젠킨스를 설치한 PC에서 접속할 때: http://localhost:8080
- 다른 PC에서 접속할 때: http://젠킨스를설치한PC의IP:8080

여기서 8080이 바로 포트 번호예요.
젠킨스는 설치할 때 따로 바꾸지 않으면 8080 포트를 써요.

그런데 설치할 때 포트를 다르게 설정했다면, 8080으로는 접속이 안 돼요.
이럴 때는 jenkins.xml 파일에서 포트 번호를 확인하면 돼요!

📁 jenkins.xml 파일 위치

설치 경로를 바꾸지 않았다면 아래 경로에 있어요.

C:\Program Files\Jenkins\jenkins.xml

내 PC → C드라이브 → Program Files → Jenkins 폴더로 들어가면 찾을 수 있어요.

🔍 포트 번호 확인하는 방법

1. jenkins.xml 파일을 우클릭해서 메모장으로 열어요.
2. Ctrl + F를 눌러서 Port를 검색해요.
3. 그럼 아래처럼 --httpPort=숫자 부분이 보여요. 이 숫자가 바로 포트 번호예요!

[사진 - jenkins.xml에서 httpPort를 찾은 화면]

예를 들어 --httpPort=9090 이라고 되어 있다면, 접속 주소는 http://localhost:9090 이 돼요.

💡 중요한 점 하나!

주소 앞부분은 https가 아니라 http예요.
젠킨스를 기본 설정으로 설치하면 http로 열리기 때문에, https로 접속하면 열리지 않아요.
https는 따로 설정했을 때만 쓸 수 있으니 이 부분 꼭 기억해주세요!

📌 한 줄 정리

젠킨스 주소가 기억이 안 나면 → C:\Program Files\Jenkins\jenkins.xml을 메모장으로 열고 → Ctrl + F로 Port 검색 → http://localhost:포트번호 로 접속!

참고: 젠킨스 공식 Windows 설치 문서 (https://www.jenkins.io/doc/book/installing/windows/)

#젠킨스 #Jenkins #젠킨스설치 #젠킨스포트 #젠킨스포트변경 #젠킨스포트확인 #젠킨스URL #젠킨스접속 #젠킨스주소 #jenkinsxml #httpPort #localhost8080 #8080포트 #포트번호확인 #윈도우젠킨스 #JenkinsWindows #CICD #빌드자동화 #DevOps #개발자공부 #개발공부 #IT공부 #비전공자코딩 #직장인코딩 #게임PM #PM #실무팁 #업무팁 #개발팁 #커리어전환

젠킨스 쓰시면서 막혔던 부분 있으면 댓글로 남겨주세요. 같이 찾아봐요!

## 티스토리 초안

# 젠킨스(Jenkins) 접속 주소와 포트 번호 확인하는 방법 (Windows, jenkins.xml · 레지스트리)

안녕하세요, 하해입니다! ☺️

Windows에 젠킨스를 설치해두고 오랜만에 들어가려는데 **접속 주소(포트 번호)가 기억나지 않을 때** 확인하는 방법을 정리했어요.
이 글은 **Windows에 젠킨스 설치 프로그램(MSI)으로 설치한 경우** 기준이에요. 내용은 젠킨스 공식 설치 문서와 젠킨스 설치 프로그램 소스에서 확인했어요. (출처는 글 아래에 있어요)

## 1. 접속 주소 구조

```
http://[주소]:[포트 번호]
```

| 접속 위치 | 주소 예시 |
|---|---|
| 젠킨스를 설치한 PC | `http://localhost:8080` |
| 같은 네트워크의 다른 PC | `http://192.168.0.10:8080` (설치한 PC의 IP) |

- 설치할 때 포트를 따로 정하지 않으면 기본 포트는 **8080**이에요.
- 기본 설치는 **http**로 열려요. https는 별도로 설정해야 해요.

## 2. 방법 ① jenkins.xml에서 확인

설치 폴더를 바꾸지 않았다면 파일 위치는 아래와 같아요.

```
C:\Program Files\Jenkins\jenkins.xml
```

1. `jenkins.xml`을 우클릭 → **메모장**으로 열기
2. `Ctrl + F` → `httpPort` 검색
3. `<arguments>` 안의 `--httpPort=숫자`에서 숫자가 포트 번호

```
--httpPort=8080
```

설치 경로를 바꿨다면 바꾼 설치 폴더 안에서 같은 이름의 파일을 찾으면 돼요.

## 3. 방법 ② 레지스트리에서 확인

젠킨스 설치 프로그램은 설치할 때 포트 번호를 레지스트리에도 저장해요.

1. `Win + R` → `regedit` 실행
2. 아래 경로로 이동

```
HKEY_LOCAL_MACHINE\SOFTWARE\Jenkins\InstalledProducts\Jenkins
```

3. 오른쪽 목록의 `Port` 값이 포트 번호

레지스트리는 **보기만** 하고 수정하지 않는 걸 권해요.

## 4. 그래도 안 열린다면

| 증상 | 확인할 것 |
|---|---|
| `https://`로 접속했더니 안 열림 | 기본 설치는 `http://` 로 접속 |
| 포트를 맞게 넣었는데 안 열림 | 젠킨스 서비스가 실행 중인지 확인 (`Win + R` → `services.msc` 에서 젠킨스 서비스 상태) |
| 다른 PC에서만 안 열림 | 설치한 PC의 IP가 맞는지, 방화벽에서 막혀 있지 않은지 확인 |

## 요약

| 하고 싶은 것 | 방법 |
|---|---|
| 기본 주소로 접속 | `http://localhost:8080` |
| 포트 번호 찾기 | `C:\Program Files\Jenkins\jenkins.xml` 에서 `--httpPort` 검색 |
| 다른 방법으로 찾기 | 레지스트리 `HKLM\SOFTWARE\Jenkins\InstalledProducts\Jenkins` 의 `Port` |
| 접속 주소 만들기 | `http://localhost:포트번호` |

## 참고 자료

- 젠킨스 공식 문서, Windows 설치: https://www.jenkins.io/doc/book/installing/windows/
- 젠킨스 Windows 설치 프로그램 소스 (jenkins.xml 설정, 레지스트리 Port 값): https://github.com/jenkinsci/packaging/blob/master/msi/build/jenkins.wxs

다른 방식(설치 파일 없이 war 실행, Docker 등)으로 설치했다면 확인 방법이 달라요. 어떤 방식인지 댓글로 알려주시면 같이 찾아볼게요!

태그: 젠킨스, Jenkins, 젠킨스포트, 젠킨스URL, jenkins.xml, httpPort, 젠킨스설치, Windows젠킨스, CICD, 빌드자동화
