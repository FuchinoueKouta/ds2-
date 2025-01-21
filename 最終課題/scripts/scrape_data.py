import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_save_data():
    url = 'https://luggagelosers.com/'
    response = requests.get(url)
    response.raise_for_status()
    
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 適切なHTMLタグと属性を利用してデータを抽出
    rows = soup.find_all('tr')  # すべてのテーブル行を取得
    
    data = []
    for row in rows:
        airline_name = row.find('td', class_='airline-name')
        loss_probability = row.find('td', class_='loss-probability')
        
        if airline_name and loss_probability:
            data.append({
                'airline_name': airline_name.text.strip(),
                'loss_probability': float(loss_probability.text.strip('%')) / 100
            })
    
    # データフレームを作成し、CSVファイルとして保存
    df = pd.DataFrame(data)
    df.to_csv('../data/raw_data.csv', index=False)

if __name__ == "__main__":
    scrape_and_save_data()