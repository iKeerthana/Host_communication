# -*- coding: utf-8 -*-
#Test description and Tooltip messages should not over lap each other
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    data=jsondata["T3_timeout_invalid_value"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    mouseClick(waitForObject(names.ecs_Window), 37, 522, MouseButton.PrimaryButton)
    test.vp("VP1")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window), "<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), data)
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Return>")
    test.vp("VP2")
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))
