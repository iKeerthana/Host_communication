
#Test Tooltip shouldn't overlap on Apply button under Control State widget-DEVQA-12
import names


def main():
    startApplication(names.App_Name)
    snooze(names.sleep)
    mouseClick(waitForObject(names.ecs_Window), 972, 367, MouseButton.PrimaryButton)
    snooze(2)
    clickButton(waitForObject(names.host_Button))
    snooze(2)
    mouseClick(waitForObject(names.ecs_Window), 39, 631, MouseButton.PrimaryButton) #T8 timeout
    test.vp("VP1")
    snooze(2)
    test.ocrTextPresent("spm")
    clickButton(waitForObject(names.x_Button_2))
