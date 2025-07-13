from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

app = FastAPI()

@app.get("/run-scraper")
def run_scraper():
    try:
        chrome_options = Options()
        chrome_options.headless = False
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        driver.get("https://www4.pwcva.gov/Web/user/disclaimer")
        time.sleep(2)

        try:
            accept_btn = driver.find_element(By.ID, "btnAccept")
            accept_btn.click()
        except:
            pass

        time.sleep(5)
        driver.quit()
        return {"status": "✅ Browser opened, disclaimer accepted!"}

    except Exception as e:
        return {"error": str(e)}
