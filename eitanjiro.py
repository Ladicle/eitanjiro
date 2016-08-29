# -*- coding: utf-8 -*-

import codecs
import os
from selenium import webdriver
import sys
import time


driver = webdriver.Chrome()
_pass = None
_user = None


def setIDandPassword():
    global _user
    _user = os.environ.get('ALC_USERNAME')
    if _user is None:
        print "Please set 'ALC_USERNAME'"
        sys.exit(1)

    global _pass
    _pass = os.environ.get('ALC_PASSWORD')
    if _pass is None:
        print "Please set 'ALC_PASSWORD'"
        sys.exit(1)


def alclogin():
    driver.get("https://eowp.alc.co.jp/login")
    inputID = driver.find_element_by_name("username")
    inputID.clear()
    inputID.send_keys(_user)
    inputPass = driver.find_element_by_name("password")
    inputPass.clear()
    inputPass.send_keys(_pass)
    driver.find_element_by_id("submit_button").click()


def parsewordbook():
    driver.get("http://eowp.alc.co.jp/wordbook/ej")

    filename = "wordbook.csv"
    f = codecs.open(filename, "w", "utf-8")

    word_meaning_dic = {}
    wordnumber = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div/form/div[2]/div[2]/p/span[1]").text
    pagenumber = int(wordnumber) / 30 + 1

    for page in range(1, pagenumber + 1):
        # Select page
        driver.get('http://eowp.alc.co.jp/wordbook/ej?page=' + str(page) + '&col=2&sort=2')
        time.sleep(0.3)

        for num in range(1, 31):
            # Get word
            wordtext = driver.find_element_by_xpath(getWordXpath('div', num * 2)).text
            f.write(wordtext)
            f.write(",")

            # Show detail
            driver.find_element_by_xpath(getWordXpath('a', num * 2)).click()
            time.sleep(0.3)

            meaningtext = driver.find_element_by_xpath(getWordXpath('div', (num * 2) + 1)).text
            meaningtext2 = meaningtext.replace("\n", " ")
            meaningtext3 = meaningtext2.replace(",", " ")

            f.write(meaningtext3)
            f.write("\n")

            word_meaning_dic[wordtext] = meaningtext3

    f.close


def getWordXpath(elm, id):
    return "/html/body/div[1]/div[1]/div/form/div[2]/div[2]/div[6]/table/tbody/tr[%d]/td[2]/$s" % id, elm


# ========= main() ==========
setIDandPassword()
alclogin()
parsewordbook()
