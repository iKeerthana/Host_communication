# -*- coding: utf-8 -*-
#Test Connection mode shouldn't have blank value in dropdown under Control State widget
import names


def main():
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.ecs_Window), 42, 389, MouseButton.PrimaryButton)  #Connection mode
    snooze(2)
    test.vp("VP1")
    clickButton(waitForObject(names.x_Button_2))
