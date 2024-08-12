# -*- coding: utf-8 -*-
#Test Automatically adjust tooltip should be disappear after few seconds
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    T3_timeout_invalid_value=jsondata["T3_timeout_invalid_value"]
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
    type(waitForObject(names.eCSUI_Window),T3_timeout_invalid_value)
    type(waitForObject(names.eCSUI_Window),"<Return>")
    snooze(1)
    test.ocrTextPresent("Invalid Input", { "tesseract": { "psm": 12 } }, waitForObjectExists(names.eCSUI_Window));
    snooze(5)
    test.ocrTextNotPresent("Invalid Input", { "tesseract": { "psm": 12 } }, waitForObjectExists(names.eCSUI_Window));
    clickButton(waitForObject(names.x_Button_2))