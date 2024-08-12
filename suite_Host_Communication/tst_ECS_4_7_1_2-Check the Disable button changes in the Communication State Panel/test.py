# -*- coding: utf-8 -*-
#Check the "Disable" button changes in the Communication State Panel
import names

def main():
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    clickButton(waitForObject(names.disable_Button))
    snooze(5)
    test.vp("VP1")
    clickButton(waitForObject(names.x_Button_2))
