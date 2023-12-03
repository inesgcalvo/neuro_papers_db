from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pubmed_journals = []

def extract_article(url):
    """
    Extracts information from a series of articles on PubMed.

    Args: 
        url (str): The URL of the webpage containing the articles.

    Returns:
        list: A list containing information extracted from each article.
    """
    errors = []
    
    PATH = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options = PATH)
    wait = WebDriverWait(driver, timeout = 15)

    driver.get(url)

    # open the first article      
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.docsum-title'))).click()
    
    i = 0
    while i < 10:
        try:
            # Display Options
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.display-options:nth-child(3) > button:nth-child(1)'))).click()

            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#article-display-format'))).click()

            # Select PubMed format
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#article-display-format > option:nth-child(2)'))).click()

            # Save information
            pubmed_journals.append(driver.find_element(By.CSS_SELECTOR, '#article-details').text)

            # WebDriver Navigational Commands backward
            driver.back()

            # Go to the next article:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'next.side-link.visible'))).click()
            i += 1
            
        except:
            break

    driver.quit()
        
    return pubmed_journals, errors