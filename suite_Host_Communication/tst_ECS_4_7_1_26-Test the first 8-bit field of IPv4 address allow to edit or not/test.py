# -*- coding: utf-8 -*-
#Test the first 8-bit field of IPv4 address allow to edit or not
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    IP_Address_value=jsondata["IPv4_address"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.eCSUI_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.eCSUI_Window), 25, 440, MouseButton.PrimaryButton)  #IP Address click
    snooze(2)
    type(waitForObject(names.eCSUI_Window),"<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window),"<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window),IP_Address_value)
    snooze(2)
    mouseClick(waitForObject(names.eCSUI_Window), 25, 440, MouseButton.PrimaryButton)#again input field click
    snooze(2)
    for _ in range(7):
        type(waitForObject(names.eCSUI_Window), "<Left>")# going middle to delete
    snooze(2)
    for _ in range(7):
        type(waitForObject(names.eCSUI_Window), "<Backspace>")
    snooze(2)
    type(waitForObject(names.ecs_Window), "213.14")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Return>")
    snooze(2)
    clickButton(waitForObject(names.apply_Button))
    snooze(2)
    test.ocrTextPresent("213.14.90.168", { "tesseract": { "psm": 12 } });
    clickButton(waitForObject(names.x_Button_2))