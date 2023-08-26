import pytest
from selenium import webdriver
from time import sleep

from pages.autorization_page import Autorization_Page
from pages.main_page import MainPage

def test_search_field(driver):
    autorization = MainPage(driver)
    autorization.select_autorization()
    sleep(10)