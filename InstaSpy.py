#instaspy.followers
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class instaspy:
    def __init__(self, username, password, target_username):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.browser = webdriver.Firefox()

    def login(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #opening instagram.com
        browser.get('https://www.instagram.com/')
        #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        browser.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        #findind login button and clicking it
        browser.find_element_by_xpath("//button[@type='submit']").click()
        #-------login process ends

    def target_profile(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #Clicking "Not Now" in pop up just after login
        sleep(4)
        not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
        sleep(1)
        not_now_button.click()


        #-------search for victim's username starts
        #click search bar
        browser.find_element_by_xpath("//span[text()='Search']").click()
        #enter victim's username and clicking Search
        browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys(self.target_username)
        sleep(3)
        #open victim's profile
        browser.find_element_by_xpath("//span[text()='"+self.target_username+"'][@class='Ap253']").click()
        sleep(2)
        #-------search for username stops


    def list_followers(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #clicking and opening followers tabs and getting maximum numbers of followers
        max = int(browser.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/span[1]").get_attribute('title').replace(',',''))
        browser.find_element_by_xpath("//a[@class='-nal3 '][@href='/"+self.target_username+"/followers/']").click()
        sleep(0.5)

        followersList = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
        temp = [numberOfFollowersInList, 0]
        followersList.click()
        actionChain = webdriver.ActionChains(browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(1)
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            sleep(1)
            if (numberOfFollowersInList == temp[1]):
                break
            else:
                temp[1] = temp[0]
                temp[0] = numberOfFollowersInList

        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            followers.append(userLink)
            if (len(followers) == max):
                break

        return followers

    def list_following(self):
        browser = self.browser
        browser.implicitly_wait(5)

        browser.get("https://www.instagram.com/"+self.target_username+"/")
        #clicking and opening following tabs and getting maximum numbers of following
        max = int(browser.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/span[1]").text.replace(',',''))
        browser.find_element_by_xpath("//a[@class='-nal3 '][@href='/"+self.target_username+"/following/']").click()
        sleep(0.5)

        followingList = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))
        temp = [numberOfFollowingInList, 0]
        followingList.click()
        actionChain = webdriver.ActionChains(browser)
        while (numberOfFollowingInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(1)
            numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))
            sleep(1)
            if (numberOfFollowingInList == temp[1]):
                break
            else:
                temp[1] = temp[0]
                temp[0] = numberOfFollowingInList

        following = []
        for user in followingList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            following.append(userLink)
            if (len(following) == max):
                break
        browser.close()
        return following


if __name__ == '__main__':
    InstaSpy_bot = instaspy('<Username>', '<Password>', '<target_username>')
    InstaSpy_bot.login()
    InstaSpy_bot.target_profile()
    followers_list = InstaSpy_bot.list_followers()
    following_list = InstaSpy_bot.list_following()
    with open('followers.csv', 'w') as f1:
        f1.write("Followers list:\n")
        for l1 in followers_list:
            f1.write(l1)
            f1.write('\n')
    with open('following.csv', 'w') as f2:
        f2.write("Following list:\n")
        for l2 in following_list:
            f2.write(l2)
            f2.write("\n")
