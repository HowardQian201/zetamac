import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def playZetaMac():
    service = Service('/Users/howardqian/Desktop/zetamac/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://arithmetic.zetamac.com/")

    driver.find_element(By.XPATH, "/html/body/div/form/input").click()

    while(True):
        question = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/span").text
        questionList = question.split()

        operator = questionList[1]
        print(operator)

        operator = ''.join(r'\u{:04X}'.format(ord(chr)) for chr in operator)[2:]
        print(operator)

        if operator == '002B':
            questionList[1] = '+'
        elif operator == '00D7':
            questionList[1] = '*'
        elif operator == '00F7':
            questionList[1] = '/'
        elif operator == '2013':
            questionList[1] = '-'

        question = questionList[0]+' '+questionList[1]+' '+questionList[2]
        answer = int(eval(question))
        print(question, answer)

        driver.find_element(By.XPATH, "/html/body/div/div/div[1]/input").send_keys(answer)

        #time.sleep(1.35)



if __name__ == '__main__':
    playZetaMac()

