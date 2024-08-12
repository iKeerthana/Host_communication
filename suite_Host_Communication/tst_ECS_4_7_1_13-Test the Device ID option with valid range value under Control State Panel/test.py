# -*- coding: utf-8 -*-
#Test the Device ID option with valid range value under Control State Panel
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    Device_ID_valid_value=jsondata["Device_ID_valid_value"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    clickButton(waitForObject(names.host_Button))
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    snooze(2)
    mouseClick(waitForObject(names.eCSUI_Window), 25, 495, MouseButton.PrimaryButton)
    snooze(2)
    type(waitForObject(names.eCSUI_Window),"<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window),"<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), str(Device_ID_valid_value))
    type(waitForObject(names.eCSUI_Window),"<Return>")
    snooze(2)
    clickButton(waitForObject(names.apply_Button))
    snooze(2)
    test.ocrTextPresent(str(Device_ID_valid_value), { "tesseract": { "psm": 12 } }, waitForObjectExists(names.eCSUI_Window));
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))
    
  