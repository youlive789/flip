# flip
Language study application using OCR, NMT

### 1. 소개
flip은 OCR과 NMT를 이용하여 화면상의 텍스트를 번역해주는 앱입니다. 데스크탑 환경에서 워드 프로세서, 브라우저, 게임 등의 텍스트를 인식하여 번역을 제공합니다. flip을 통해서 쉽게 언어공부를 할 수 있도록 사람들을 돕는 것이 flip의 목표입니다.

 - 사용법 
    - 학습된 자연어모델 다운로드
      - https://drive.google.com/drive/folders/1-4QYoBB8-JCQOUTENfiV3HiEpq_4nODi?usp=sharing
      - third-party/huggingface 폴더에 config.json, pytorch_model.bin을 다운로드합니다.
    - pip install -r requirements.txt
    - python flip.py
  
### 2. 진행상황 및 문제들
 - UI 화면
    - flip 기본 UI
        ![flip 기본 UI](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbtNISQ%2FbtqIVIhqs39%2F3k0NL7QQKKqfxRrN66bCf1%2Fimg.png)
    - flip 번역결과
        ![flip 번역결과](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbVkthJ%2FbtqIVHQlYr8%2FfgwFMMa9RJemFzKY03DTz1%2Fimg.png)
 - 번역모델
    - 고품질의 parallel corpus 데이터를 찾아야함.
    - huggingface의 경우 모델크기가 너무 큰 단점이 있음. 또한 학습시킨 모델이 onnx 모델로 전환되지 않는 버그를 수정해야함.
    - opennmt의 경우에는 자체 추론 라이브러리 ctranslate2를 제공해주고 있지만 windows 버전을 제공해주지 않음.
    - 직접 학습시키는 모델의 경우 아직까지 만족할만한 번역성능을 내고있지 못함.

### 3. 기술스택
 - Python kivy
 - tesseract
 - AutoHotkey
 - (pilot) huggingface, opennmt

### 4. 레퍼런스 및 기타링크
 - UI
    - [kivy MVVM example](https://github.com/rafalo1333/KivyExampleMVVMPhotosApp)
    - [kivy SystemTray example](https://github.com/twister077/KivySystemTrayApp)
 - OCR
    - [로봇매냐님의 OCR 포스팅](https://blog.naver.com/PostView.nhn?blogId=monkey5255&logNo=221598376164&from=search&redirect=Log&widgetTypeCall=true&directAccess=false)
 - NMT
    - [번역 데이터](https://github.com/jungyeul/korean-parallel-corpora)
    - [flip-huggingface 학습노트](https://colab.research.google.com/drive/18yLBjDQ6uZYKzz1aeZTIUvw0wFDWOn6X?usp=sharing)
    - [flip-opennmt 학습노트](https://colab.research.google.com/drive/1atmKcbQIvTy9drMnAxFhLWWneDO1TL_R?usp=sharing)
    - [flip-translation](https://github.com/youlive789/flip-translation)
    - [HeungBae Lee 님의 Seq2Seq 구현예제](https://heung-bae-lee.github.io/2020/01/22/deep_learning_11/)