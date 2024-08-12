# -*- coding: utf-8 -*-
#Test field value should be highlighted(Orange border) after value has been automatically adjusted.
import names
from json_utils import read_json_file


def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    data=jsondata["T3_auto_adjust_value"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.ecs_Window), 37, 522, MouseButton.PrimaryButton)
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window), "<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), data)
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Return>")
    snooze(3)
    test.vp("VP1")
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))

