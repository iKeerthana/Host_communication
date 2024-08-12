# -*- coding: utf-8 -*-
#Test Clear Search icon (X) shouldn't be visible by default under Host Communication 
import names


def main():
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    test.vp("VP1")
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))    

