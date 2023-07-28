	
def func(selected_new_profile_folder):
	from selenium import webdriver
	from selenium_stealth import stealth
	from selenium.webdriver.support.select import Select
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.action_chains import ActionChains
	from selenium.webdriver.common.keys import Keys



	options = webdriver.ChromeOptions()
	options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
	options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option('useAutomationExtension', False)
	options.add_argument('--disable-blink-features=AutomationControlled')
	options.add_argument(f"user-data-dir={selected_new_profile_folder}")

	path = r"C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(path, options=options)
	stealth(driver,
		languages=["en-US", "en"],
		vendor="Google Inc.",
		platform="Win32",
		webgl_vendor="Intel Inc.",
		renderer="Intel Iris OpenGL Engine",
		fix_hairline=True,
		)

	driver.get("https://www.tiktok.com/login/")