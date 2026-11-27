# CSV 점수 관리 프로그램


## ① 무엇을 하나요 (What)

CSV 파일에 저장된 학생의 이름과 점수를 읽고, 정상적인 데이터만 저장하는 프로그램이다. 이름이나 점수가 비어 있거나 잘못 입력된 경우에는 따로 구분하여 처리한다.



## ② 왜 만들었나요 (Why)          ★ AI는 이 칸을 못 씁니다

CSV 파일을 읽는 과정에서 점수가 비어 있거나 숫자가 아닌 값이 입력되면 오류가 발생할 수 있다. 또한 점수가 0~100점 범위를 벗어나는 경우도 있다.
이러한 문제로 프로그램이 중간에 종료되는 것을 방지하고, 잘못된 데이터와 정상적인 데이터를 구분하여 안정적으로 점수를 관리하기 위해 만들었다.



## ③ 어떻게 쓰나요 (How)


```bash
# 설치
pip install pytest pytest-cov
# 실행
test_ai_A: cd C:\Users\kimmi\OneDrive\Desktop\ai-programing\week11_files
pytest test_ai_A.py

test_ai_B: cd C:\Users\kimmi\OneDrive\Desktop\ai-programing\week11_files
pytest test_ai_B.py
```

## ④ 어떻게 테스트하나요


```bash
pytest를 사용하여 여러 가지 입력 상황에서 프로그램이 정상적으로 작동하는지 확인한다.
```

```

```

## ⑤ 파일 구성


| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | CSV 파일을 읽고 정상적인 점수와 잘못된 데이터를 구분한다. |
| test_ai_A.py | 여러 입력 상황에서 프로그램이 제대로 작동하는지 테스트한다. |
| README.md | 프로그램의 기능과 사용 방법을 설명한다. |

## ⑥ 만든 사람 · AI를 어디에 썼는지


- 만든 사람 : 김민성 · 2026100694
- AI를 쓴 곳 : 코드 작성 및 테스트 코드 작성에 도움을 받았다.
- 내가 직접 판단한 것 : 점수의 범위를 0~100점으로 정하고 잘못된 데이터를 구분하는 기준을 정하였다.

## 라이선스


MIT License (LICENSE 파일 참고)
>>>>>>> 81580060eb04a6c48854c86cce8bae3c7bcbbe24
