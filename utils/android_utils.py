import subprocess


def get_UDID_dynamically():
    active_devices = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    if active_devices:
        return active_devices.stdout.split()[4]
    raise Exception('Device not found')


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '13',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_UDID_dynamically(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
    }
