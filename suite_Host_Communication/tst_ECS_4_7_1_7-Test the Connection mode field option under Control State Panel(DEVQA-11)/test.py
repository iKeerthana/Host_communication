# -*- coding: utf-8 -*-
#Test the Connection mode field option under Control State Panel-(DEVQA-11)

import names


def main():
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    clickButton(waitForObject(names.o_ComboBox))
    snooze(2)
    type(waitForObject(names.o_ComboBox), "Active")
    snooze(2)
    type(waitForObject(names.o_ComboBox), "<Return>")
    snooze(2)
    clickButton(waitForObject(names.apply_Button))
    snooze(2)
    test.ocrTextPresent("Active")
    snooze(5)
    clickButton(waitForObject(names.o_ComboBox))
    snooze(2)
    type(waitForObject(names.o_ComboBox), "Passive")
    snooze(2)
    type(waitForObject(names.o_ComboBox), "<Return>")
    snooze(2)
    clickButton(waitForObject(names.apply_Button))
    snooze(2)
    test.ocrTextPresent("Passive")
    snooze(2)
    clickButton(waitForObject(names.x_Button_2))




