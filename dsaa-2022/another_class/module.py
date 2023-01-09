import soccer as sc
import pyautogui # 프롬프트 명령어 pip install pyautogui


# if __name__ == "__main__": # 이 py파일을 직접 실행하였다면.! 이라는 뜻! 직접 실행하지않았다면 다른 곳에서 이 파일을 import하여 실행하겠지

aq = sc.SoccerPlayer('son','FW', 7)
print(aq.name)
