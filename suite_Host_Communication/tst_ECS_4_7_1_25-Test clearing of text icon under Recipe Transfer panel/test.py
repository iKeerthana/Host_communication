# -*- coding: utf-8 -*-
#Test clearing of text icon under Recipe Transfer panel (UIECS-886)
import names
from json_utils import read_json_file

def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    Search_value=jsondata["Search_value"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    type(waitForObject(names.o_Edit_10), Search_value)
    snooze(2)
    mouseClick(waitForObject(names.o_Edit_10), 427, 11, MouseButton.PrimaryButton)
    snooze(2)
    test.ocrTextNotPresent(str(Search_value))
    test.compare(waitForObjectExists(names.o_Edit_10).text,"")
    clickButton(waitForObject(names.x_Button_2))