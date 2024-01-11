## Huawei Bootloader Unlocker

It's a simple script made for the purpose of unlocking the Bootloader of your Huawei device.

Simply open it in vscode, or an other IDE, and replace the IMEI variable with your IMEI code, now you'll have to plug in your phone to your computer enable USB debbuging and allow OEM unlocking. Now reboot in to the bootloader (adb reboot bootloader).

And thats it. Now you'll sadly have to wait about 5 real days and your bootloader should be unlockt if it's not and the FRP (OEM) Lock is back on, don't panic the programm creates a log file in which the last tryed code will be saved and that one should be the code too unlock it.

Have fun :)   
I really hope it works!   
BTW its based on the c# programm made by rainxh11 so go check him out!! 
https://github.com/rainxh11/HuaweiBootloader_Bruteforce/blob/master/Program.cs
