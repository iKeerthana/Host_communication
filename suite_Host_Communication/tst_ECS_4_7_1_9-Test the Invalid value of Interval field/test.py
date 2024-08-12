# -*- coding: utf-8 -*-
#Test the Link Test Interval field option with invalid value under Control State Panel
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    Link_test_interval_invalid_value=jsondata["Link_test_interval_invalid_value"]

    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.ecs_Window), 39, 416, MouseButton.PrimaryButton)
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window), "<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), Link_test_interval_invalid_value)
    snooze(2)
    test.compare(waitForObjectExists(names.o_Edit_5).text,"")
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))