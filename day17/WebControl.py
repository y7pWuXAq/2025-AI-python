### 웹브라우저 오픈을 위한 라이브러리
# - 브라우저 제어
from selenium import webdriver

### 동적 웹페이지 처리 라이브러리
from selenium.webdriver.common.by import By

### 데이터 처리
import pandas as pd

### 시간 라이브러리
import time

# 크롬 드라이버 초기화
def getDriver(url) :
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

# 영화 정보를 담을 클래스 정의
class WebControl :
    def __init__(self) :
        self.driver = None
        self.movie_info = pd.DataFrame(columns=["영화제목", "실관람평점", "예매순위", "예매율", "누적관객수"])
        self.movie_user_info = pd.DataFrame(columns=["영화제목", "개별관람평점", "개별관람평내용", "긍정_부정"])

    # 영화 목록 추출 함수
    def get_movie_list(self, url) :
        self.driver = getDriver(url)
        try :
            # 영화 목록을 상위 10개만 추출
            movie_list_path = "div.movie-list-info"
            movie_elements = self.driver.find_elements(By.CSS_SELECTOR, movie_list_path)
            
            # 영화가 10개 이상 있을 경우, 상위 10개만 추출
            movie_elements = movie_elements[:10]
            
            movie_titles = []
            for movie in movie_elements:
                movie_titles.append(movie.text)
        except :
            movie_titles = []
            print("예외 발생!! : find_elements()의 결과값을 가져오지 못했습니다.")
        return movie_titles
    
    # 영화 세부 정보 추출 함수
    def get_movie_details(self, movie_elements):
        for movie_element in movie_elements:
            movie_element.click()
            time.sleep(1)
            self.setWindowPage(self.driver)

            ### 영화 기본정보
            # 영화 제목
            title_path = "#contents > div.movie-detail-page > div.movie-detail-cont > p.title"
            title_element = self.driver.find_element(By.CSS_SELECTOR, title_path)
            title = title_element.text
            
            # 실관람평
            score_path = "#mainMegaScore > p > em"
            score_element = self.driver.find_element(By.CSS_SELECTOR, score_path)
            score = score_element.text
            
            # 예매순위 및 예매율
            rate_level_path = "#contents > div.movie-detail-page > div.movie-detail-cont > div.info > div.rate > p.cont"
            rate_level_element = self.driver.find_element(By.CSS_SELECTOR, rate_level_path)
            rate_level = rate_level_element.text.split(" ")
            level = rate_level[0][:-1]
            rate = rate_level[1][1:][:-2]
            
            # 누적관객수
            audiance_path = "#contents > div.movie-detail-page > div.movie-detail-cont > div.info > div.audience > p > em"
            audiance_element = self.driver.find_element(By.CSS_SELECTOR, audiance_path)
            audiance = audiance_element.text.replace(",", "")
            
            # 영화제목, 실관람평점, 예매순위, 예매율, 누적관객수 정보를 movie_info에 저장
            movie_info = {
                "영화제목" : title,
                "실관람평점" : score,
                "예매순위" : level,
                "예매율" : rate,
                "누적관객수" : audiance
            }
            
            # pd.concat을 사용하여 새로운 데이터프레임을 movie_info에 추가
            self.movie_info = pd.concat([self.movie_info, pd.DataFrame([movie_info])], ignore_index=True)
            
            ### 영화 개별관람 정보
            # 개별 관람평 정보 추출
            movie_tab_path = "#contentData > div:nth-child(5) > div.tab-list.fixed > ul > li:nth-child(2) > a"
            movie_tab_element = self.driver.find_element(By.CSS_SELECTOR, movie_tab_path)
            movie_tab_element.click()
            time.sleep(1)
            self.setWindowPage(self.driver)
            
            # 개별 관람 평점
            use_score_path = "div.story-area > div.story-box > div > div.story-cont > div.story-point > span"
            use_score_elements = self.driver.find_elements(By.CSS_SELECTOR, use_score_path)
            
            # 개별 관람평 내용
            use_content_path = "div.story-area > div.story-box > div > div.story-cont > div.story-txt"
            use_content_elements = self.driver.find_elements(By.CSS_SELECTOR, use_content_path)
            
            for idx in range(len(use_score_elements)):
                use_score = use_score_elements[idx].text
                use_content = use_content_elements[idx].text
                
                # 개별 관람평점 및 평내용 추가
                positive_negative = "긍정" if int(use_score) >= 6 else "부정"
                user_info = {
                    "영화제목": title,
                    "개별관람평점": use_score,
                    "개별관람평내용": use_content,
                    "긍정_부정": positive_negative
                }
                # pd.concat을 사용하여 새로운 데이터프레임을 movie_user_info에 추가
                self.movie_user_info = pd.concat([self.movie_user_info, pd.DataFrame([user_info])], ignore_index=True)
            
            # 이전 페이지로 돌아가기
            self.driver.execute_script("window.history.go(-1)")
            time.sleep(1)

    # 페이지 변경 처리 함수
    def setWindowPage(self, driver):
        page_handle = driver.window_handles[-1]
        driver.switch_to.window(page_handle)
        time.sleep(1)