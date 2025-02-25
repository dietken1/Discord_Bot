# FOSS 2024-2 final project
Author: 소프트웨어학과 202126892 정원준
본 프로젝튼는 아주대학교 2024년 2학기에 이환용 교수님의 오픈소스SW 입문 수업을 들으면서 진행한 오픈소스 기말 프로젝트입니다.

# Python과 OpenAI API를 이용하여 개발한 디스코드 AI 봇
- Discord 공식 홈페이지 -> https://discord.com
- OpenAI  공식 홈페이지 -> https://platform.openai.com

## 아이템 선정 동기
예전부터 게임을 좋아했던 저는 디스코드를 오랜 기간 사용해 왔습니다. 그리고 다른 사람들이 제작해놓은 다양한 봇도 많이 사용했습니다.
그래서 저도 이번 기회에 유용한 봇을 만들어보고 싶다는 생각을 가지게 되었습니다.
최근 들어 AI가 많이 발전했고, OpenAI에서 AI를 사용할 수 있도록 API 서비스를 제공하고 있다는 사실을 알게 되었습니다.
그래서 디스코드 내에서 AI 봇을 사용하면 정말 유용할 것 같다는 생각을 하게 되었고, 이를 주제로 선정했습니다.

## 개발 환경 및 도구
- **개발 환경**: Windows
- **개발 도구**: Visual Studio Code
- **언어**: Python

## 강의 구성

1. **설정**

- Discord 란
- OpenAI API 란
- Discord developer portal을 이용한 봇 세팅
- Discord 서버 세팅
- OpenAI API 세팅


2. **실습**

- .env 파일 작성
- ai.py 파일 작성
- bot.py 파일 작성
- 코드 실행 및 결과 확인

## 개발하면서 생긴 문제점 및 해결 방법

### 1. **봇 메시지 처리 문제**
서버에 메시지가 올라가면 봇이 응답을 해주는 구조인데, 봇이 본인이 보낸 메시지를 제가 보낸 메시지로 인식해서 무한대로 메시지를 보내는 문제가 발생했습니다. 저는 이를 해결하기 위해서 메시지가 올라오면 작동하는 비동기 함수 내에 메시지의 주인이 봇 자신이면 무시하도록 조건문을 추가해 주었고, 이 문제를 해결할 수 있었습니다.

### 2. **OpenAI의 API 유료화 문제**
프로그램을 실행시켰을 때, 봇은 정상적으로 서버에 접속을 하는데, 메시지를 보내도 답장이 오지 않는 문제가 발생했습니다.
저는 코드 자체에 문제가 있다고 생각하고 원인을 찾아보았지만, 큰 문제가 없었기에 매우 혼란스러웠습니다.
그리고 원인을 찾기 위해서 긴 시간을 투자해서 관련 정보를 찾아보았습니다. 그리고 그 과정에서 원인을 발견할 수 있었습니다.
저는 이 프로젝트를 시작하기 전에는 OpenAI에서 API를 무료로 제공하고 있다고 알고 있었습니다. 하지만 API 기능은 전용 크레딧이 있어야 작동했습니다. 알고 보니, 첫 가입자에게만 일정량의 무료 크레딧이 제공되어서 잠시 무료로 사용이 가능한 것이었고,
그 이후에는 추가 결제를 해서 사용할 필요가 있었습니다. 그래서 크레딧을 구매했고, 그 결과 정상적으로 작동하였습니다.

## 소감
봇의 응답속도를 개선하지 못한 부분이 아쉬웠습니다. 응답속도를 개선하기 위해서 다양한 방안을 찾아보았지만, 정확한 원인을 파악하지 못했습니다.
하지만 이번 프로젝트를 통해 API를 이용하는 경험을 할 수 있었고, 오픈소스 API를 사용하여 새로운 것을 만드는데 흥미를 느끼게 되었습니다.
앞으로 더 많은 API를 사용해서 다양한 것들을 개발하고 싶습니다.

## 참고 자료
- https://discordpy.readthedocs.io/en/stable/
- https://www.magicaiprompts.com/docs/gpt-chatbot/openai-api-usage-guide
