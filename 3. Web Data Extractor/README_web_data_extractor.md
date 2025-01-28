### 3. **Web Data Extractor**
**File name**: `web_data_extractor.py`

```python
import requests
from bs4 import BeautifulSoup

def extract_titles(url):
    """
    Extracts all <h1> titles from a given webpage.
    
    Parameters:
        url (str): The URL of the webpage to scrape.
        
    Returns:
        list: A list of extracted titles.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            titles = [h1.text.strip() for h1 in soup.find_all('h1')]
            return titles
        else:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    example_url = "https://example.com"
    print("Extracted Titles:", extract_titles(example_url))
