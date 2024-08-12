# -*- coding: utf-8 -*-
#Test the TCP port field option with valid value under Control State Panel
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    Tcp_value=jsondata["TCP_valid_value"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.eCSUI_Window), 25, 465, MouseButton.PrimaryButton)
    snooze(2)
    type(waitForObject(names.eCSUI_Window),"<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window),"<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window),Tcp_value)
    snooze(2)
    type(waitForObject(names.ecs_Window),"<Return>")
    snooze(2)
    clickButton(waitForObject(names.apply_Button))
    snooze(2)
    #test.ocrTextNotPresent(str(Tcp_value))
    test.ocrTextPresent(str(Tcp_value), { "tesseract": { "language": "English", "psm": 12 } });
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))