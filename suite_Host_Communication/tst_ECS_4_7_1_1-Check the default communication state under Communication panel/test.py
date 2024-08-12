# -*- coding: utf-8 -*-
#Check the default communication state under Communication panel
import names

def main():
    startApplication(names.App_Name)
    snooze(names.sleep)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    test.vp("VP3")
    clickButton(waitForObject(names.x_Button_2))
    
