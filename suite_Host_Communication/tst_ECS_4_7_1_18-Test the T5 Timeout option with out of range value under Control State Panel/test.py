# -*- coding: utf-8 -*-
#Test the T5 Timeout option with out of range value under Control State Panel
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    T5_Timeout_valid_value=jsondata["T5_Timeout_valid_value"]
    T5_Timeout_invalid_value=jsondata["T5_Timeout_invalid_value"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.ecs_Window), 38, 549, MouseButton.PrimaryButton)
    snooze(2)
    type(waitForObject(names.eCSUI_Window),"<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window),"<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window),T5_Timeout_invalid_value)
    type(waitForObject(names.eCSUI_Window),"<Return>")
    test.ocrTextPresent("Invalid Input")
    snooze(2)
    clickButton(waitForObject(names.apply_Button))
    snooze(2)
    test.ocrTextPresent(str(T5_Timeout_valid_value))
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))