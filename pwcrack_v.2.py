import subprocess
import logging

from numpy import sqrt

logging.basicConfig(filename="passwordCracker.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def checkLuhn(imei):
    sum = 0
    alternate = False
    i = len(imei) - 1
    while i >= 0:
        nx = imei
        n = int(nx[i])
        if alternate:    
            n *= 2
            if n > 9:
                n = (n % 10) + 1
        sum += n
        alternate = not alternate
        i -= 1

    return sum % 10

def incrementChecksum(oemCode, checksum, imei):       
    oemCode += int(checksum + sqrt(int(imei)) * 1024)
    return oemCode
 
imei = "IMEI_Code"
checksum = int(checkLuhn(imei))
oemCode = 1
lastOem = oemCode


while(True):
    try:
        oemCode = incrementChecksum(oemCode, checksum, imei)
        command = subprocess.run(["fastboot", "oem", "unlock", "\"" + str(oemCode) + "\""], capture_output=True, timeout= 5)
        if lastOem != oemCode:
            logging.warning("Password Tryed: [" + str(oemCode) + "]")
        lastOem = oemCode
    except:
        logging.raiseExceptions
        subprocess.run(["adb", "reboot", "bootloader"])
