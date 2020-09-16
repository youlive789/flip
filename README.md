# flip
Screen language translation using OCR, NMT

### 1. 소개
flip은 OCR과 NMT를 이용하여 화면상의 텍스트를 번역해주는 앱입니다. 데스크탑 환경에서 워드 프로세서, 브라우저, 게임 등의 텍스트를 인식하여 번역을 제공해주는 것을 목표로 하고 있습니다.

### 2. 진행상황 및 문제들
 - UI 화면
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