# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
	"""
	Base page class
	"""
	capabilities = {"browserName": "chrome", "platform": "linux"}

	def __init__(self):
		# self.driver = webdriver.Remote(desired_capabilities=BasePage.capabilities)
		self.driver = webdriver.Chrome()
		self.wait = WebDriverWait(self.driver, 15)

	def go_to_site(self, url):
		self.driver.get(url)

	def click_on_element(self, by, element: str):
		element_on_click = self.wait.until(ec.visibility_of_element_located((by, element)))
		element_on_click.click()

	def close_site(self):
		self.driver.close()

	def enter_data(self, by, path: str, data: str):
		input = self.wait.until(ec.visibility_of_element_located((by, path)))
		input.send_keys(data)
		return input

	def press_enter(self, element):
		element.send_keys(Keys.ENTER)

	def get_page_source(self):
		return self.driver.page_source

	def get_title(self) -> str:
		return self.driver.title

	def get_list_elements(self, by: str, value: str) -> list:
		list_elements = self.wait.until(ec.presence_of_all_elements_located((by, value)))
		return list_elements

	def get_element(self, by: str, value: str):
		element = self.wait.until(ec.visibility_of_element_located((by, value)))
		return element
