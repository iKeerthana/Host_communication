# -*- coding: utf-8 -*-
#Test entering the valid IP address in two digits under Control State widget
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    ip=jsondata["Valid_ip_two_digit"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.eCSUI_Window), 25, 440, MouseButton.PrimaryButton)
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window), "<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), ip)
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Return>")
    snooze(2)
    button = waitForObject("{type='Button' text='Apply'}")
    clickButton(button)
    snooze(2)
    test.compare(waitForObjectExists(names.o_Edit_9).text, ip)
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))
    