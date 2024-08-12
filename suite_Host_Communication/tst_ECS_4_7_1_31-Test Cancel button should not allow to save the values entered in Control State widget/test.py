# -*- coding: utf-8 -*-
#Test Cancel button shouldn't allow to save the values entered in Control State widget-UIECS-649
import names
from json_utils import read_json_file


def main():
    file_path=names.json_file_path
    jsondata=read_json_file(file_path)
    T3_timeout_value=jsondata["T3_timeout_value"]
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.ecs_Window), 37, 522, MouseButton.PrimaryButton) #T3 timeout
    snooze(2)
    type(waitForObject(names.eCSUI_Window),"<Ctrl+A>")
    type(waitForObject(names.eCSUI_Window),"<Backspace>")
    snooze(2)
    type(waitForObject(names.eCSUI_Window),T3_timeout_value)
    type(waitForObject(names.eCSUI_Window),"<Return>")
    snooze(2)
    clickButton(waitForObject(names.cancel_Button))
    snooze(2)
    test.ocrTextNotPresent(str(T3_timeout_value))#1234 should be not present 
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))
    
    
    
   