import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from selenium_ui.jira.pages.pages import Issue

def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    print(f"custom data:{datasets['custom_issues']}")
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']
        print(f"custom_issue_key:{issue_key}")
        issue_page = Issue(webdriver, issue_key)
        @print_timing("selenium_app_custom_action:view_issue")
        def measure():
            issue_page.go_to()
            issue_page.wait_for_page_loaded()
        measure()

