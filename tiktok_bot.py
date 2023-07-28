def func(video_url, c1,c2,c3):
    from selenium import webdriver
    from selenium_stealth import stealth
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from time import sleep
    from selenium.webdriver.common.keys import Keys

    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    sleep(5)
    for i in range(1,3):
        options.add_argument(f"user-data-dir=C:\\Users\\acer\\desktop\\profiles\\profile{i}")
        path = r"C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(path,options=options)

        driver.get(video_url)

        def follow():

            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[3]/div/button')))
            driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[3]/div/button').click()

        def like_video():
            driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[5]/div[2]/div[1]').click()


        def comment_video():
            driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[5]/div[2]/div[2]/div').click()
            comments=WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div/main/div/div[2]/div[2]/div[4]/div/div[1]/div/div/div[1]/div[2]/div')))
            comments.send_keys('wow')
            sleep(1)
            comments.send_keys(Keys.RETURN)

        if c1==1 and c2==1 and c3==1:
            follow()
            like_video()
            comment_video()

        elif c1 ==1 and c2==0 and c3 ==0:
            like_video()

        elif c1 == 0 and c2 == 1 and c3 == 0:
            comment_video()

        elif c1 ==0 and c2==0 and c3 ==1:
            follow()

        driver.quit()
