from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from config import user, password, link
import re

#to remove unwanted shit from html
def clean_text(text):
    clean_html = re.sub('<.*?>', '', text)
    clean_spaces = re.sub(r'\s+', ' ', clean_html).strip()
    return clean_spaces

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=500)
    page = browser.new_page()
    page.goto(link)
    page.fill('input#mui-1', user)
    page.fill('input#mui-3', password)
    page.click('button[type=submit]')
    page.locator('"Messages"').click()
    page.is_visible('div.MuiBox-root css-0')
    page.wait_for_timeout(8000)
    html = page.inner_html('#root')
    soup = BeautifulSoup(html, 'html.parser')
    conf = soup.find_all('p', {'class': 'MuiTypography-root MuiTypography-body1 jss26 css-2irivz'})

    modified_list = [clean_text(item.text) for item in conf]
    modified_list.reverse()
    print(modified_list)
    

    with open("confession.txt", "w", encoding="utf-8") as f: #confessions.txt contains all the scrapped data
        for i in modified_list:
            f.write(i + "\n")
#I was 4 pegs in while making this
#dont ask me how this shit works😭