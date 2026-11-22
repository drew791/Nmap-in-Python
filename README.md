# Nmap-in-Python

A simple port scanner and banner grabber in Python.

## ？ What is this? 
This tool can be used to scan a host (yes, including yourself) to find open ports and their info (service, banner, eventual headers...). 
It's a similar concept of the tool "Nmap", regarded as "an open source tool designed to scan large networks or single hosts". But, although these scripts do something almost identical, everything's brought down to its very basic concepts (I used the "socket" library, which has limitations) to further understand how nmap and similar tools work.

## ⚠️ WARNING
Before proceeding, there are a few things I must warn you about. 

- First and most important, if you're ever gonna use this tool, it's for **EXPLICITLY AUTHORIZED TARGETS ONLY**.

- If you're going to use this tool and want to test it in a safe environment, I highly recommend you to get a virtual machine, especially one like Metasploitable which has flaws designed on purpose for you to exploit. You'll obviously need to install a virtualization software to run the VM. The best ones are Oracle VirtualBox, VMware (Workstation for Windows and Linux, Fusion for macOS), UTM (specifically optimized for macOS) and GNOME (for Linux). Personally, the only one that worked for me to run Metasploitable 2 was UTM, so here's a quick tutorial for you macOS users (please note I have an Apple Silicon chip, so this guide might not work for Intel):

1. Install UTM on the App Store
2. Install [Metasploitable 2](https://www.rapid7.com/products/metasploit/metasploitable/) on this link (or use another one if you want)
3. Open UTM and select the "Create a New Virtual Machine" option
4. Choose "Emulate", then "Other" when selecting the OS
5. Toggle expert mode, then choose: "x86_64" as architecture, "Standard PC (Q35 + ICH9, 2009)(alias of pc-q35-10.0)(q35)" or similar as system, and keep the rest as it is
6. Turn off UEFI boot, and select "None" as a boot device option
7. 
