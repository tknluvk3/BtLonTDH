import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_kenh14_data():
    # Cấu hình Selenium (ẩn trình duyệt)
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")

    # Khởi động trình duyệt
    driver = webdriver.Chrome(options=chrome_options)

    # Truy cập trang và cuộn để load thêm nội dung
    url = "https://kenh14.vn/xa-hoi/nong-tren-mang.chn"
    driver.get(url)
    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(10):  
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Sau khi cuộn xong, lấy HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Phân tích HTML
    articles = soup.find_all('div', class_='knswli-right')  # phần thông tin bài viết

    data = []
    for article in articles:
        title_tag = article.find('h3', class_='knswli-title')
        title = title_tag.get_text(strip=True) if title_tag else 'N/A'
        content_url = title_tag.find('a')['href'] if title_tag and title_tag.find('a') else 'N/A'

        description_tag = article.find('div', class_='knswli-sapo')
        description = description_tag.get_text(strip=True) if description_tag else 'N/A'

        # Ảnh nằm ở div bên trái
        image_container = article.find_previous_sibling('div', class_='knswli-left')
        image_url = image_container.find('img')['src'] if image_container and image_container.find('img') else 'N/A'

        data.append({
            'Title': title,
            'Description': description,
            'Image URL': image_url,
            'Content URL': content_url
        })

    # Lưu vào file CSV
    df = pd.DataFrame(data)
    df.to_csv('kenh14_data.csv', index=False, encoding='utf-8-sig')
    print(f"✅ Đã lưu {len(data)} bài viết vào articles_data.csv")

# Lên lịch chạy hằng ngày
schedule.every().day.at("06:00").do(get_kenh14_data)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)

