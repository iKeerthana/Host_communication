# -*- coding: utf-8 -*-
#Test Cancel button should be enabled only when values are modified under Control State widget 
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    value=jsondata["TCP_valid_value"]   
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.ecs_Window), 37, 522, MouseButton.PrimaryButton)
    #mouseClick(waitForObject(names.eCSUI_Window), 45, 537, MouseButton.PrimaryButton) #T3 timeout
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window), "<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), value)
    snooze(2)
    test.compare(waitForObjectExists(names.cancel_Button).enabled, True)
    snooze(2)
    clickButton(waitForObject(names.apply_Button))
    snooze(3)
    test.compare(waitForObjectExists(names.cancel_Button).enabled, False)
    clickButton(names.x_Button_2)