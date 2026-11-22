# Nmap-in-Python

A simple port scanner and banner grabber in Python.

## ？ What is this? 
This tool can be used to scan a host (yes, including yourself) to find open ports and their info (service, banner, eventual headers...). 
It's a similar concept of the tool "Nmap", regarded as "an open source tool designed to scan large networks or single hosts". But, although these scripts do something almost identical, everything's brought down to its very basic concepts (I used the "socket" library, which has limitations) to further understand how nmap and similar tools work.

## ⚠️ WARNING
If you're ever gonna use this tool, it's for **EXPLICITLY AUTHORIZED TARGETS ONLY**. Any other use is (probably) considered illegal and is not my responsibility. You have been warned.

## 🖥️ VM Set-up UTM and Metasploitable 2 (for macOS users)
If you're going to use this tool and want to test it in a safe environment, I highly recommend you to get a virtual machine, especially one like Metasploitable which has flaws designed on purpose for you to exploit. You'll obviously need to install a virtualization software to run the VM. The best ones are Oracle VirtualBox, VMware (Workstation for Windows and Linux, Fusion for macOS), UTM (specifically optimized for macOS) and GNOME (for Linux). Personally, the only one that worked for me to run Metasploitable 2 was UTM, so here's a quick tutorial for you macOS users (please note I have an Apple Silicon chip, so this guide might not work for Intel).

### Installing and setting up Metasploitable in UTM

1. Install UTM on the App Store
2. Install [Metasploitable 2](https://www.rapid7.com/products/metasploit/metasploitable/) on this link (or use another one if you want)
3. Open UTM and select the "Create a New Virtual Machine" option
4. Choose "Emulate", then "Other" when selecting the OS
5. Toggle expert mode, then choose: "x86_64" as architecture, "Standard PC (i440FX + PIIX 1996)(default)(pc-i440fx-10.0)" or similar as system, and keep the rest as it is
6. Turn off UEFI boot, and select "None" as a boot device option, then name the VM and don't touch the other settings
7. Right click the VM you just created (it should appear in the menu on the left), then select "Edit"
8. Scroll down on the left menu until you reach the "Create Disk" option, then import the "Metasploitable.vmdk" file (you'll find it when extracting the zip you downloaded)
9. Once created, you're ready to go!

### Using Metasploitable

You'll need to log in once you boot the VM (both the username and the password are "msfadmin"). Then, you'll need to know the VM's IP address. Here's the command:
```bash

msfadmin@metasploitable:~$ ifconfig
```
You'll see two main blocks, but we'll only need the one called "eth0". In it, find  ```inet addr```: it's the IP address we're going to use.
