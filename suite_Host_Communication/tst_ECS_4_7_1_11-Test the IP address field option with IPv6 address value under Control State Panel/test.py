# -*- coding: utf-8 -*-
#Test the IP address field option with IPv6 address value under Control State Panel
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    IPv6=jsondata["IPv6_address"]

    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.eCSUI_Window), 25, 439, MouseButton.PrimaryButton)
    snooze(2)
    type(waitForObject(names.eCSUI_Window), "<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window), "<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window), IPv6)
    snooze(2)
    test.ocrTextNotPresent(IPv6)
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))