# -*- coding: utf-8 -*-
#Test the T3 Timeout option with valid range value under Control State Panel
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    T3_Timeout_valid_value=jsondata["T3_Timeout_valid_value"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.ecs_Window), 37, 522, MouseButton.PrimaryButton)
    snooze(2)
    type(waitForObject(names.eCSUI_Window),"<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window),"<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window),T3_Timeout_valid_value)
    type(waitForObject(names.eCSUI_Window),"<Return>")
    snooze(2)
    clickButton(waitForObject(names.apply_Button))
    snooze(2)
    test.ocrTextPresent(str(T3_Timeout_valid_value), { "tesseract": { "psm": 12 } }, waitForObjectExists(names.eCSUI_Window))
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))