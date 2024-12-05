from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time  # 이 줄을 추가

def capture_weather():
    url = "https://weather.naver.com/"

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    time.sleep(3)  # 페이지 로드 대기
    screenshot_path = 'frontend/public/weather.png'
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return screenshot_path