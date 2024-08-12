# -*- coding: utf-8 -*-
#Test Communication chat message should display the text while typing multiple lines and scroll should be enabled under Host-Communication screen
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    data=jsondata["Host_message_field_data"]
    scrolldata=jsondata["Host-message_field_extra_data"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.eCSUI_Window), 870, 617, MouseButton.PrimaryButton)
    snooze(2)
    val = 3
    for _ in range(val):
        type(waitForObject(names.eCSUI_Window), "<Return>")
        snooze(1)
    type(waitForObject(names.eCSUI_Window), data)
    mouseWheel(2)
    snooze(2)
    mouseWheel(-2)
    snooze(2)
    test.ocrTextPresent(str(data))
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))