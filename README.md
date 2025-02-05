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


#### 가상환경 생성 명령

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

#### 가상환경 제거 하기

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
    - 02_List_예제.ipynb



## DAY 04