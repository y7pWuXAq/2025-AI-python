# 2025-AI-python
2025년 빅데이터 기반 AI 개발 전문가 과정 파이썬 기본 학습 리포지토리



### DAY 01

- 아나콘다 설치
-  Anaconda Prompt 실행
    -  아나콘다가 관리하는 root 경로
        - C:\Users\Administrator
    -  우리가 사용할 작업폴더로 이동 
        - cd C:\Users\Administrator\pk_202503

- (base) : 아나콘다가 관리하는 대표 가상환경(가상공간)
    -  이곳에는 라이브러리 설치를 하지 않음

- (base) 가상공간에 설치된 라이브러리 목록 확인
    - ```conda list```
 
- 파이썬 버전 확인
    - ```python --version```
 
- 아나콘다 명령어 : conda 라는 이름으로 명령을 시작
    - conda 버전 확인
    - ```conda --version```

- 아나콘다에 생성된 가상환경(가상공간) 목록 확인
    - ```conda env list```

- 주피터 노트북(jupyter notebook) 프로그램 에디터 열기
    - 내가 작업할 작업폴더 경로 확인 후 아래 실행
        - ```jupyter notebook```

- (base) 가상공간과 웹브라우저 주피터 노트북 에디터와 연결하기 위해서는 커널(kernel) 연결을 통해서 파일을 생성해야 가상공간의 라이브러리를 사용할 수 있음
    - (base 공간은 -> Python3 커널을 통해서 연결되어 있음)

- 주피터 노트북에서 사용하는 파이썬 파일 확장자 : *.ipynb
    - 순수한 파이썬 파일 확장자 *.py로 변환하려면 별도로 변환하여 저장

- 새로운 가상환경(가상공간) 생성하여 진행
    - 우리가 별도로 생성할 가상환경(가상공간)은 (base) 가상공간에서 수행


- 가상환경 생성 명령
    - 새로운 가상환경 생성하기 (폴더 위치 무관)
        - Anaconda Prompt의 (base) 가상환경에서 실행해야 함
        - 설치를 위한 라이브러리 업그레이드 (가끔 한번씩 수행)
            ** 라이브러리 설치 명령어 : conda 또는 pip

        - conda 라이브러리 업그레이드
            ```conda update -n base conda```

        - pip 라이브러리 업그레이드
            ```python -m pip install --upgrade pip```

        - 가상환경 생성 : 가상환경 이름은 pk_base_202503
            - conda create -n (가상환경이름) python=(python 버전)
            ```conda create -n pk_base_202503 python=3.9```
            - 가상환경 잘 만들어졌는지 확인하기 : 가상환경 목록 리스트 확인
            - 생성된 위치 : C:\Users\Administrator\anaconda3\envs\pk_base_202503
            ```conda env list```
        
        - 터미널 확인
            ```
            # To activate this environment, use 
            - 특정 가상환경으로 들어갈 때 사용, 들어간다는 의미는 활성화

            #$ conda activate pk_base_202503

            #To deactivate an active environment, use
            - 현재 가상환경에서 빠져 나갈 때, 비활성화라고 칭합니다. base 가상환경으로 돌아감

            #$ conda deactivate
            ```

- 가상환경 제거 하기
    - conda remove -n pk_base_202503 --all

    - 새로운 가상환경에 라이브러리 설치하기 (base에서 하시면 안됩니다. 디렉토리 위치 무관)
    - 최초에 한번 pip 업그레이드
        ```python -m pip install --upgrade pip```

    - 커널(Kernel) 생성하기 : pk_base_202503_kernel
        - 각 가상환경이 만들어 질 때마다, 커널(Kernel)을 만들어야 함
        - 커널을 생성하기 위해서는 jupyter 및 notebook 라이브러리가 필요함
        - jupyter 및 notebook 라이브러리 설치
            ```pip install jupyter notebook```

    - 커널(Kernel) 생성 : 가상환경 1개당 커널 1개 생성
        - 가상환경 1개에 커널 2개이상인 경우 모두 삭제해야함
        - (생성위치 : C:\Users\Administrator\AppData\Roaming\jupyter\kernels\pk_base_202503)
            ```python -m ipykernel install --user --name pk_base_202503 --display-name pk_base_202503_kernel```
        - 생성된 커널 확인하기 : 커널 목록 확인(가상환경 이름으로 확인)
            ```jupyter kernelspec list```

    - 커널 삭제하기 : 가상환경을 삭제할 경우에는 커널도 함께 삭제해야 함
        - 가상환경 삭제 순서 : 커널 삭제 > 가상환경 삭제 커널 목록에 나와 있는 이름 그대로 사용
            ```jupyter kernelspec uninstall pk_base_2025```

    - 주피터 노트북 open -> 커널 확인
        ```jupyter notebook```



## DAY 02

- 변수 타입 확인하기 : 
- 변수의 타입을 확인하는 함수 : type(값)
    ```type(a), type(b)```

- 타입 변환 (형변환)
    ```c = int(b)```

- 변수명 규칙
    * 변수명은 변수명은 영문, 특수문자, 숫자 등의 조합으로 생성
    * 가급적 영문으로 생성
    * 필요 시 특수문자를 이용해 영문명과 연결하여 사용 (abc_a)
    * 숫자는 변수명의 뒤에 사용 (abc_1)
        - 변수명은 숫자로 시작 할 수 없음
    * !! 중요 : 변수명은 값이 아님(임의로 변수명을 값처럼 만들어 낼 수 없음)

- 산술연산자
    - 보통 숫자를 이용한 연산을 수행
        - 간혹, 문자열간의 더하기(+) 또는 곱하기(*) 연산을 수행하는 경우도 있음

    - 연산자 기호 : +, -, *, /, %, //, **, ++, --
        - 주로 사용하는 연산 기호는 +, -, *, /, %, ++

    - % : 나눈 나머지의 값 (홀, 짝 체크 할 때 주로 사용)
    - // : 나눈 몫의 값
    - ** : 거듭제곱(^)

- while 문
    - for 문으로 가능한 것들은 모두 while 문으로 가능함 (반대도 가능)
    - while 문은 주로 무한 반복 시 사용
        - 무한 반복을 하는 경우에는 while 문 내에 반복을 종료하는 조건을 반드시 추가해야 함
    - 종료 방법 : 조건 (if) 처리
    - 종료 옵션 : break 사용 > break가 있는 시점부터 반복 중지

- while 문 문법
    ```
    while 반복 할 조건 :
        처리할 코드 작성
    ```

- List 리스트
    - 여러개의 변수값들을 묶어서 가지고 다니는 타입

- 리스트(List), 딕셔너리(Dict), 튜플(tuple), 등등..

- 리스트(List) 변수 :  여러개의 변수들의 값들을 하나로 관리하는변수
    - 사용되는 기호 : []
    - 리스트 메모리 공간 내에 여러개의 작은 메모리(변수)들이 존재함
    - 여러개의 작은 메모리의 주소값을 인덱스(index) 주소, 또는 번호라고 칭함
    - 리스트 내에 있는 값들을 처리 할 때는 주로 for 문과 함께 사용
    - 리스트 내에 값들이 타입은 다양함 (어떤 타입도 가능)
    - 리스트 내에 값을 추출하는 방법
        - 작은 메모리 주소, 즉 인덱스(index) 번호를 이용해서 추출함



## DAY 03

- 슬라이스 사용
    - 슬라이스는 범위를 의미함.
    - 범위를 지정하는 기호는 콜론( : )
    - 범위를 지정하여 리스트 내 값을 추출 할 때 사용

- 문자열 데이터
    - 리스트 메모리 구조와 동일하게 저장되고 처리 됨
        ```py
            str1 = "안녕하세요, 파이썬 재미있어요!"
            str1, type(str1)
        ```

- 리스트에 값 추가하기
    - .append()

- 리스트 연산
    - 리스트 더하기 연산 : 여러개의 리스트가 하나의 리스트로 더해짐
    - 리스트 곱하기 연산 : 하나의 리스트 내에 동일한 값을 어러개 추가하고자 할 때 사용

- 리스트에 값 삭제하기
    - del 사용 : 리스트의 인덱스 번호를 사용해서 삭제할 때 사용
    - remove() : 값을 이용해서 삭제할 때 사용
        - 같은 값이 존재할 경우, 가장 첫번째 나오는 값을 삭제함

- 리스트에 값 수정하기
    - 리스트 내 특정 인덱스 위치의 값 수정하기

- 예제 학습
    - [02_List_예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day03/02_List_예제.ipynb)



## DAY 04

- 딕셔너리(dictionary)

- 리스트와 동일하게 여러개의 값을 가지고 다니는 타입 중 한가지
- 리스트와 차이점
    - 리스트 메모리는 인덱스 순서가 순서적으로 만들어지지만 딕셔너리는 순서가 없음

- 딕셔너리는 key 와 value의 한쌍으로 한개의 데이터가 만들어짐
- key는 고유한 값만 사용가능하며 key를 이용해 value의 값을 추출 할 수 있음
- 리스트는 [ ] 사용, 딕셔너리는 { }를 사용하여 데이터를 정의함
- 딕셔너리에서 데이터(value 의 값)을 추출하고자 할 때는 "딕셔너리 변수명 [key]" 형태로 작성

- 딕셔너리 값(value) 수정 
    - 딕셔너리 변수명[존재하는 key] = 수정할 값
- 딕셔너리 값(value) 추가
    - 딕셔너리 변수명[존재하는 key] = 추가할 값

- 딕셔너리 학습
    - [01_딕셔너리_dic](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day04/01_딕셔너리_dic.ipynb)

- 딕셔너리 응용 예제
    - [02_딕셔너리_예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day04/02_딕셔너리_예제.ipynb)

- 튜플 (tuple)

- 튜플은 소괄호 ( ) 기호를 사용합니다.
- 출력 결과값이 소괄호( )로 묶여 있는 경우에는 대부분 튜플 타입
- ** 튜플은 리스트와 구조 및 사용법이 모두 동일함. 기호만 다름.
- ** 리스트와의 차이점
    - 한 번 정의 된 값들은 수정이 불가함.
    - 수정 및 삭제 하려면 완전 제거 후 재정의 필요.

- 보통 직접 튜플을 생성하여 사용하는 경우는 많지 않음.
- 주로 특정 함수의 결과 또는 처리 결과를 튜플 타입으로 제공을 함.
- 튜플을 생성할 때 한개의 값만 정의해서 생성할 경우에는 한개의 값 뒤에 콤마(,)를 사용



## DAY 05

- 클래스
    - 클래스 이름은 대문자로 시작
    - 변수를  멤버 변수, 함수를 멤버 함수라고 칭함
    - 함수를 정의할 때, 매개변수에는 무조건 self라는 단어를 처음에 제시해야 함
    - self는 클래스 내에서 전역변수로 사용하겠다는 의미를 가짐
    - self로 정의된 변수들은 모두 외부에서 접근이 가능
- 클래스 예제
    - [02_클래스_class](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day05/02_클래스_class.ipynb)

- 한줄코딩



## DAY 06

- 판다스(pandas)
    - 행렬 데이터를 처리하기 위한 다양한 함수를 제공해 주는 라이브러리 이름
    - 데이터 분석에서 데이터 처리(전처리) 시에 가장 많이 사용되는 라이브러리
    - 파일 읽어들이기, 저장하기, 행렬 데이터 처리 등을 수행
    - 데이터에 대한  시각화도 일부 지원
    - 라이브러리 사용 방법 : import pandas as pd
    - 라이브러리 설치 필요(가상환경에서 설치 > 가상환경 확인) : pip install pandas
    - 시각화 및 파일 처리 라이브러리 등 기본 라이브러리 설치 : 1day 설치 파일 참조

- 데이터 분석 과정
    - 일반 도서에서 정의하는 과정
        - 계획수립 > 데이터 수집 > 데이터 전처리 > 데이터 후처리 > 데이터 분석 > 데이터 시각화

    - 현장에서 사용하는 과정
        - 탐색적 데이터 분석
            - 사전계획(파이럿 프로젝트) > 데이터 수집 > 데이터 전처리 > 데이터 가공(후처리) > 데이터 시각화 > 인사이트 도출

    - 데이터 분석 모델링
        - 데이터 분석(머신러닝 or 딥러닝 모델 생성) >

    - 분석 서비스 및 결과
        - 웹서비스 or 분석보고서

- EDA(탐색적 데이터 분석)
    - 주로 데이터에서 발생되는 패턴들을 시각적으로 탐색하여 인사이트를 도출함
    - 방법론이라고도 합니다. (탐색 방법론)

- 데이터의 형태 분류
    - 정형 데이터   : 행렬 형태로 정리된 데이터(보통 엑셀 데이터)
    - 반정형 데이터 : 행렬 형태는 아니지만, 항목에 대한 정의 형태 처럼 구분이 가능한 데이터들
    - 비정형 데이터 : 행렬 또는 항목에 대한 정의 형태가 아닌, 뉴스와 같은 구분할 수 없는 내용들 (뉴스, 음성, 영상 등)

- 데이터 처리 기초
    - [01_데이터처리_기초](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day06/01_데이터처리_기초.ipynb)



## DAY 07

- day06에 학습한 내용을 바탕으로 예제
    - [01_데이터처리_예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day07/01_데이터처리_예제.ipynb)

- 데이터 시각화
    - [02_입국객데이터_시각화](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day07/02_입국객데이터_시각화.ipynb)
    - 선 그래프 활용
        - 중국 국적에 대한 기준년월별 관광객 변화 추이
        ![1개국선그래프](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d07_중국입국객데이터시각화.png)
        - 국적 및 기준 년월별 관광객 변화 추이
        ![5개국선그래프](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d07_국가별관광객데이터시각화.png)




## DAY 08

- 포항시 교통버스카드 데이터 현황 시각화 분석
    - 데이터 수집처 : 국가 교통데이터 오픈마켓
    - 수집 URL : bigdata-transportation.kr
    - 검색어 : 포항시 BIS 교통카드 사용내역

- 포항시 교통버스 데이터 현황을 수집하고 데이터 분석 실행
    - [포항시_교통버스카드데이터_수집_및_통합](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day08/01_포항시_교통버스카드데이터_수집_및_통합.ipynb)

- 분석한 데이터를 시각화
    - [데이터_현황분석_시각화](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day08/02_데이터_현황분석_시각화.ipynb)
    ![포항시버스교통카드시각화](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d08_포항시교통버스카드데이터시각화.png)



## DAY 09

- 시리즈
    - 한 컬럼의 열 데이터를 담당하는 타입
    - 리스트의 구조와 유사함(인덱스 번호 또는 값으로 유지됨)
    - 리스트와 사용방법이 유사함
- ex)
    ```py
    data = ["강아지", "고양이", "호랑이", "사자", "원숭이"]
    idx  = ["0", "1", "2", "3", "4"]
    idx  = ["a", "b", "c", "d", "e"]

    # - 시리즈 타입으로 정의하기
    pd.Series(data=data, index=idx)
    ```

- 딕셔너리 데이터 -> 시리즈
    ```py
        dict_data = {"a" : 1, "b" : 2, "c" : 3}
        # 딕셔너리의 key는 index값으로 사용
        # value는  시리즈의 값으로 사용됨
        pd.Series(dict_data)
    ```

- 리스트 데이터 -> 시리즈
    ```py
        list_data = ["강아지", "고양이", "호랑이", "사자", "원숭이"]
        # 리스트의 index 번호를 -> 시리즈의 인덱스 값으로
        # 데이터 값을 -> 시리즈의 값으로
        pd.Series(list_data)
    ```

- 튜플 -> 시리즈
    ```py
        tuple_data = ("강아지", "고양이", "호랑이", "사자", "원숭이")
        # 튜플의 index 번호를 -> 시리즈의 인덱스 값으로
        # 데이터 값을 -> 시리즈의 값으로
        pd.Series(tuple_data)
    ```

- 시리즈의 인덱스 값을 수정 할 수 있음
    ```py
        pd.Series(tuple_data, index=["a", "b", "c", "d", "e"])
    ```
- [데이터 구조 예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day09/01_데이터_구조.ipynb)

- 데이터프레임 이름 뒤에 대괄호 안에 사용한 행번호는 눈에 보이는 인덱스 값이 아님
    - (메모리 내에서 관리하는 인덱스 번호가 아님)
- 인덱스 값을 이용하는 경우에는  실제 눈에 보이는 값(번호)만 사용 가능

- 데이터프레임 내에 행/렬, 또는 특정 행렬 값에 접근하여 수정 등을 수행할 경우
    - 넘파이(Numpy)에서 제공하는 loc과 iloc를 이용해야 함
    - loc와 iloc는 실제 메모리에 접근해서 사용하는 방식
    - 특정 컬럼의 값을 수정하고자 할때 주로 loc 또는 iloc로 접근하여 사용
    - 이외 일반적으로 데이터 조회 시에도 사용
  
- loc[] : 인덱스 값을 이용하여 접근하는 방식(눈에 보이는 값)
- iloc[] : 실제 메모리에서 관리하는 인덱스 번호로 접근하는 방식(메모리 번호)
- Numpy 라이브러리 : 숫치 데이터 처리(연산 등 처리)를 위한 특화된 라이브러리

- [데이터 조작 예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day09/02_데이터_조작.ipynb)



## DAY 10
- 수집 데이터 전처리
    - 1. 결측 데이터처리(결측치)
        - 특정 컬럼의 데이터들 중에 비어 있는 데이터를 찾아서 처리
        - 읽어들인 데이터를 info() 함수를 통해서 최초 확인 가능
            - 확인이 불가능한 경우도 있음
    - 2. 중복 데이터처리(중복치)
        - 행단위로 중복된 데이터가 있는지 찾아서 처리
    - 3. 이상 데이터처리(이상치)
        - 컬럼의 성격에 맞지 않는 데이터를 찾아서 처리
        - describe() 함수의 min, max 데이터를 이용하여 상식선에서 숫자 컬럼의 이상치 확인가능
        - 연속된 데이터의 경우 특정 범위를 벗어나는 데이터 찾아서 처리하는 것이 일반적임
            - 계산 공식에 의해서 확인 후 처리 진행됨

- 결측데이터 처리
    - 결측치라고 칭함
    - 결측데이터
        - 특정 컬럼의 값이 비어있는 경우 null 또는 Nan 이라고 표기
        - 스페이스 한칸은? -> 문자로 인식
    - encoding= : 문자 해석기라고 생각하시면 편합니다.
        - 한국어 관련 문자 해석기 : euc-kr
        - 국제 표준화 해서 사용하는 문자 해석기 : utf-8
    - isnull() : 행렬 데이터에서 결측치가 있는 특정 값들 찾는 함수
        - 결측치가 있으면 : True 
        - 결측치가 없으면 : False
    - notnull() : 행렬 데이터에서 결측치가 없는 값들 찾는 함수
        - 결측치가 있으면 : True 
        - 결측치가 없으면 : False

    - 결측치 처리 방법
        - 1. 결측치가 있는 부분의 데이터를 사용할지 or 말지 결정
            - 데이터 제공 기관에 사전 문의
        - 2. 사용하지 않는경우
            - 컬럼과 행 중에 어느 부분을 제거(삭제)할지 결정(삭제하지 않고 그냥 사용, 가급적 지양)
            - 제거 방법 : 해당 결측치가 있는 -> 행 또는 열 자체를 삭제
                - 결측치가 있는 [행] 삭제하기
                - axis=0 : 행삭제, 1은 열삭제
                - 사용함수 : dropna(axis=0)
                    - 일반적으로 행을 삭제함(다만, 시간단위 추이 분석의 경우 행 삭제는 조심)
                    - 삭제할 경우 데이터에 대한 손실이 발생할 수 있기에 잘 결정해야 함
        - 3. 사용하는 경우
            - 어떻게 사용할지 결정 (정답은 없음)
            - 숫자 컬럼의 경우 : 평균값 또는 0으로 대체
            - 결측치가 속해 있는 컬럼의 전체 값에 대한 평균 사용
                ```py
                df["컬럼명"].fillna(0) # 0으로 대체하기
                avg_all = df["컬럼명"].mean() # 평균으로 대체하기
                ```
            - 결측치가 있는 데이터의 전/후 데이터의 평균 사용
            - 범주형 컬럼의 경우
                - 비율 대비 대체 또는 해당 범주의 주변 데이터 탐색 후 유사값으로 대체
    - !! 결측치 처리 결정 후 필수 확인 사항 : 분석을 의뢰한 고객에게 확인 후 처리 진행
    - [결측 데이터 처리 예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day10/01_전처리_결측데이터처리.ipynb)

- 중복데이터 처리 방법
    - 1. 중복값 확인
        - 중복을 허용하는 데이터인지 (제공자에게)확인 필요
    - 2. 중복값을 삭제할지, 그냥 사용할지 결정
        * 삭제할 경우 -> 중복된 행을 삭제
        * 그냥 사용할 경우  -> 실제로 중복이 가능한 데이터의 성격인 경우가 해당
    - [중복 데이터 처리 예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day10/02_전처리_중복데이터처리.ipynb)

- 이상치 처리순서
    - 1. 결측치 처리 완료
    - 2. 중복치 처리 완료
    - 3. describe()를 통해 1차적으로 이상한 데이터가 있는지 확인
        - 숫자값을 가지는 컬럼들에 대해서만 확인이 가능(문자값은 직접 확인해야함)
        - 컬럼의 성격을 상식선에 알고 있는 경우 min과 max값을 확인
    - 4. 이상치 확인 방식
        - 그래프 이용하여 확인 : boxplot() 그래프로 확인
        - 이상치 계산 공식으로 확인 후 -> 이상치가 없는 데이터로 사용
    - 5. 확인 후 이상치가 있는 행 또는 컬럼을 삭제할지, 대체할지 결정
        -> 대체 처리 방법은 결측치 처리와 동일

    - 이상치 계산 공식
        - <계산공식>
            * min 이상치 = Q1 - (1.5 x IQR)
            * max 이상치 = Q3 + (1.5 x IQR)
            * IQR = Q3 - Q1
            * Q1 = 25% 시점의 분위수 값
            * Q3 = 75% 시점의 분위수 값
    - [이상 데이터 처리 예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day10/03_전처리_이상데이터처리.ipynb)



## DAY 11

- 날짜 format(형태) : 문자열 타입이 아래 날짜 형태인 경우 날짜 타입으로 형변환 가능
    ```py
    data = ["2020-01-01", "2020-03-01", "2020-09-01"]
    # 결과값 ['2020-01-01', '2020-03-01', '2020-09-01']
    
    ts_dates = pd.to_datetime(data)
    ts_dates, type(ts_dates)
    # 결과값 DatetimeIndex(['2020-01-01', '2020-03-01', '2020-09-01'],
    # dtype='datetime64[ns]', freq=None
    ```

- 날짜 데이터에서 년, 월, 일 추출하기
    - 년 월 일 데이터 추출
        - to_period() 함수 사용 : 날짜 데이터 추출 함수
        - freq 속성(파라미터) 사용 : 년, 월, 일 지정 속성(파라미터)
            - freq="D" : 년월일 모두 표시(일자까지 표시)
            - freq="M" : 년월 까지 표시(월까지 표시)
            - freq="Y" : 년도 표시(년도만 표시)

- 시계열 데이터 프레임 형태로 만들기
    - 시계열 데이터
        - 날짜 타입을 인덱스로 사용하는 형태
        - 데이터 프레임의 인덱스를 날짜타입의 값으로 사용하게 됨
        - 실제 날짜 타입의 컬럼이 있거나, 인덱스를 날짜 타입으로 만들어 주어야 함
    ![시계열데이터시각화](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_시계열데이터선그래프시각화.png)

- 원-핫 인코딩(One-Hot Encoding)
    - 범주형 데이터의 문자 특성을 컬럼으로 만들고 0부터 시작되는 값으로 변환하는 방법을 통칭함
    - 특정 컬럼의 범주의 갯수만큼 컬럼이 만들어지며 범주의 갯수만큼 0부터 n까지의 정수값이 정의됨
    - 0~n까의 값을 가변수(dummy variable)라고 칭함
    - 이진분류, 다중분류에서 사용됨
    - 이진분류에서는 0과 1을 사용(0은 아니다, 1은 맞다의 의미로 사용)
    - 다중분류에서도 0과 1을 사용
    - 데이터들의 패턴 분석을 할 경우 범주형 데이터들을 숫자로 변환하는 경우가 있음
    - 이때 범주형 데이터들을 원-핫 인코딩 개념을 통해 구조를 변환
    - 원-핫 인코딩 변환 함수 : get_dummies(), 판다스에서 제공하는 함수
            - 함수 활용
            ![데이터재구조화](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_데이터재구조화.png)
            - 원-핫 인코딩 처리된 결과값을 숫자로 변환해서 표현
            ![원-핫인코딩](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_원-핫인코딩.png)
            - 전치(Transposition) : 행과 열을 교환한다는 개념 구조 변경됨
            ![원-핫인코딩전치](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_원-핫인코딩전치.png)

- 엔스콤 dataset 다양한 시각화 방식
![엔스콤 dataset 다양한 시각화](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_엔스콤dataset그룹별시각화.png)


- 다양한 그래프 그리기
- [그래프 그리기 예제](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day11/03_데이터_시각화.ipynb)
    - 데이터 프레임에서 제공해주는 시각화
    ```py
    ### 데이터프레임에서 제공하는 선그래프 원형
    # - 기본값(디폴트)은 line이기에 생략가능
    tips.plot(kind="line")
    ```
    ![데이터 프레임 제공 시각화](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_데이터프레임제공시각화.png)

    ```py
    ### 박스플롯 그리기
    tips.plot(kind="box")
    ```
    ![박스플롯](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_데이터프레임제공박스플롯.png)

    - matplotlib 라이브러리에서 제공하는 시각화
        - 선 그래프, 막대 그래프, 산점도 그래프 등등
        ![산점도 그래프](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_matplotlib산점도그래프.png) 
    - seaborn 라이브리에서 제공해주는 그래프
    ![seaborn라이브러리](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_seaborn라이브러리제공시각화.png)

- 그래프 여러개를 동시에 그릴수도 있음
```py
### 그래프 여러개 동시에 그리기
# jointplot() 함수 사용
#  - 함수 내부에서 속성으로 그래프 형태 정의
#  - 메인 그래프는 산점도로, 상단 및 우측에는 히스토그램 막대그래프가 나타남

sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
plt.show()
```
![그래프동시에그리기](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d11_그래프여러개동시에그리기.png)

- 이외에 여러 방식의 그래프가 있음



## DAY 12

- 지도 시각화를 위한 라이브러리 설치
    - 지도 시각화는 별도의 라이브러리 설치가 필요함
        ```
        pip install folium
        ```
    - 설치 후 라이브러리 정의
        ```py
        import folium
        ```

- 지도 시각화 순서
    - 정해진 순서보다는 절차에 따르는게 편할 수 있음(향후 본인의 편의로 수정)
- 1. 최초에 보여질 기준 지역의 위/경도를 중심으로 배경 지도를 그림
- 2. 배경 지도에 데이터의 위/경도를 이용해서 마커(maker) 표시를 함
    - 마커, 말풍선, 사진, 링크, 등등 응용 가능

- 지도 시각화 스타벅스 매장 분석
    - [01_지도시각화_스타벅스1](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day12/01_지도시각화_스타벅스1.ipynb)
    ![지도시각화](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d12_지도시각화_스타벅스1.png)
    - [02_지도시각화_스타벅스2](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day12/02_지도시각화_스타벅스2.ipynb)
    - [03_지도시각화_스타벅스3](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day12/03_지도시각화_스타벅스3.ipynb)
        - 경계면 표시하기
        ![지도시각화경계면](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d12_지도시각화_스타벅스2.png)
        - 경계와 범례, 마커 표시
        ![지도시각화경계면범례](https://raw.githubusercontent.com/y7pWuXAq/2025-AI-python/refs/heads/main/images/d12_지도시각화_스타벅스2-1.png)



## DAY 13

- 데이터 조별 실습



## DAY 14

- 데이터 수집
    - 분석을 위해 필요한 데이터를 내부 또는 외부로 부터 수집
    - 수집 방법 : 파일 다운로드, Open-API, 웹크롤링

    - 파일 기반 데이터 수집
        - 파일 데이터 수집 방법 : 일반적으로 다운로드 방식을 통해 수집함
        - 데이터 제공 기관 : 공공기관, 국책기관, 기업 등 (기업의 경우 유료가 많음)
        - 파일 포멧에 따라 읽어들이기는 함수가 다름 : 사용 라이브러리는 판다스(pandas), 이외 등등
        - csv, txt : read_csv(), to_csv() 함수 사용(저장은 어떤 포맷이든 가능)
        - xlsx : read_excel(), to_excel() 함수 사용(저장은 어떤 포맷이든 가능)
        - json : read_json(), to_json() 함수 사용(저장은 어떤 포맷이든 가능)
        - geojson : json 라이브러리의 load() 함수 사용하여 읽어들임
    - [01_데이터수집_파일](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day14/01_데이터수집_파일.ipynb)

    -  Open-API 방식
        - 특정 기관에서 데이터를 제공하는 방식
        - 웹 URL을 이용해서 제공하는 방식(정확하게는 웹프로토콜을 이용해서 제공)
            - 프로토콜 : 규약, 규칙이라는 의미
        - 데이터를 요청하는 사람(수집)과 데이터를 제공하는 기관이 있음
        - 수집자는 제공자가 제공하는 URL을 사용해야 함
            - 제공자가 정의한 key : value 값들을 받아와서 사용해야 함
        - 제공자는 아무에게나 데이터를 제공하지 않으며 승인된 수집자에게만 데이터를 제공
            - 승인여부 : 제공자가 발급한 API-Key를 수집자가 전달받아서 요청 시 사용
        - 중요 용어
            - 수집자 : 요청자(클라이언트, client) == request
            - 제공자 : 응답자(서버, server) == response
    - [02_데이터수집_Open-API](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day14/02_데이터수집_Open-API)



## DAY 15

- 웹페이지 데이터 수집
    - 웹브라우저에 보이는 데이터(텍스트, url, 이미지 등등..)를 수집
    - 수집 방법 : 정적웹페이지 수집, 동적 웹페이지 수집
    - 정적 웹페이지 수집 : BeautifulSoup 라이브러리 사용 (Open-API 방식과 유사)
        - 정적 : 브라우저의 페이지 이동 없이, 현재 보이는 페이지에서만 데이터 수집하는 경우
    - 동적 웹페이지 수집 : Selenium 라이브러리 사용
        - 동적 : 브라우저의 페이지에서 클릭(click)을 통해 페이지가 바뀌는 처리를 포함해서 수집하는 경우

- 웹 데이터 수집 순서
    - 1. 크롬 브라우저를 제어하기 위한 브라우저 드라이버 연결
    - 2. 브라우저에 수집 URL(페이지) 요청하기 -> 동시에 페이지 정보(html) 받아오기 (수집)
    - 3. 받아온 html은 문자열 타입 -> html 타입으로 의미 부여하기
    - 4. 의미가 부여된 html 코드 내에서 태그 이름과 속성을 이용해 데이터 조회하기
        - 데이터 조회는 태그와 태그 사이의 text 값을 추출함
        - 태그 내에 속성(key)의 값(value)을 추출할 수도 있음
    - 5. 조회한 데이터프레임 또는 파일로 저장
    - 6. 저장된 데이터를 이용해서 분석

- HTML 태그에서 사용되는 용어
    - 태그 : 기호(<이름>)을 사용, 태그 내에 있는 첫번째 문자를 태그 이름이라고 함
    - 데이터 : 태그와 태그 사이의 문자, 또는 속성에 정의된 값
    - 속성 : 태그 내에 정의된 변수(key=value 형태로 되어 있음)
    - id 속성 : 고유한 이름값(value)을 가지는 한개 태그
        - 고유한 이름값을 가지는 특정 태그를 찾을 때 사용됨
    - class 속성 : 같은 이름값(value)을 가지는 여러개 태그들
        - 동일한 class 이름값을 가지는 여러 태그를 찾을 때 사용됨

- 사용 라이브러리
    - 웹 브라우저 컨트롤 라이브러리 : selenium (설치필요, pip install selenium)
    - 수집된 html 문자열 데이터에 html 타입으로 의미를 부여하는 라이브러리
        - 정적 페이지 처리 라이브러리
            - BeautifulSoup (정적 페이지 처리시에만 사용, 태그 정보 조회 함수들 포함)
        - 동적 페이지 처리 라이브러리
            - selenium (html 타입으로 의미를 부여하지 않아도 됨, 바로 조회 사용, 정적 페이지 처리도 가능)

- [03_데이터수집_웹크롤링_정적페이지](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day15/03_데이터수집_웹크롤링_정적페이지.ipynb)



## DAY 16

- 데이터 수집
    - 정적 페이지
        - [01_데이터수집_멜론차트순위_정적페이지](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day16/01_데이터수집_멜론차트순위_정적페이지.ipynb)
    - 동적 페이지
        - [02_데이터수집_영화데이터수집_동적페이지처리](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day16/02_데이터수집_영화데이터수집_동적페이지처리.ipynb)



## DAY 17

- 데이터 수집 실습
    - [01_데이터수집_웹크롤링_메가박스_10건](https://github.com/y7pWuXAq/2025-AI-python/blob/main/day17/01_데이터수집_웹크롤링_메가박스_10건.ipynb)