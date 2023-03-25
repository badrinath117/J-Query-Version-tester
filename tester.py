from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def get_jquery_version(url):
    try:
        options = Options()
        options.binary_location = '/usr/bin/brave'  # Set the path to the Brave executable on your system
        options.add_argument('--headless')  # Set headless mode to true to prevent the browser window from opening

        # Set the path to the chromedriver executable on your system
        # Replace "/path/to/chromedriver" with the path to the downloaded chromedriver executable
        driver = webdriver.Chrome(options=options, executable_path="Path-to-chromedriver")

        # Open the URL in the browser
        driver.get(url)

        # Open the browser console
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + 'J')

        # Wait for the console to open
        driver.implicitly_wait(5)

        # Execute the jQuery command in the console
        jquery_version = driver.execute_script("return jQuery.fn.jquery")

        # Close the browser
        driver.quit()

        # Return the jQuery version
        return jquery_version

    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")
        return None

# Read the list of URLs from a file
with open('url.txt', 'r') as file:
    urls = file.readlines()

# Remove any newlines from the URLs
urls = [url.strip() for url in urls]

# Get the jQuery version for each URL and print the results
for url in urls:
    jquery_version = get_jquery_version(url)
    print(f"{url}: jQuery version {jquery_version}")
