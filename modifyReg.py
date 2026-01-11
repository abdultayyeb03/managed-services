import winreg
import sys

REG_PATH = r"SOFTWARE\CollegeProjectDemo"
VALUE_NAME = "Enabled"
VALUE_DATA = 0  # Change value to 0

try:
    # Create (or open) the registry key
    key = winreg.CreateKeyEx(
        winreg.HKEY_LOCAL_MACHINE,
        REG_PATH,
        0,
        winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY
    )

    # Set DWORD value
    winreg.SetValueEx(
        key,
        VALUE_NAME,
        0,
        winreg.REG_DWORD,
        VALUE_DATA
    )

    winreg.CloseKey(key)
    print("Registry value successfully set to 0")

except PermissionError:
    print("ERROR: Please run this script as Administrator")
    sys.exit(1)

except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)