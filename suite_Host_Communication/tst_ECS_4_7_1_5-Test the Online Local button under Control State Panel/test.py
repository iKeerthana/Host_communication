# -*- coding: utf-8 -*-

# Test the Online Local button under Control State Panel

import names


def main():
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    clickButton(waitForObject(names.equipment_Offline_Button))
    snooze(3)
    clickButton(waitForObject(names.online_Local_Button))
    snooze(6)
    test.vp("VP1")
    clickButton(waitForObject(names.x_Button_2))