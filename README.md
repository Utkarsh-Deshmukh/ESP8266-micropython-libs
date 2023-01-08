# ESP8266-micropython-libs
Various functions that can be run on ESP8266 using micropython

Target OS - Windows

# usage:
## Firmware flashing:
in order to run these various projects, we first need to flash the ESP8266 module with a micropython kernel.  
Step 0) `Prerequisite`: we need esptool installed in order to flash the ESP board. this can easily be done using the command: `pip install esptool`  
Step 1) `Download the latest micropython firmware for ESP8266`: the latest micropython kernel can be downloaded from here: https://micropython.org/download/esp8266/  
Step 2) `Erase the flash on the ESP8266 board`: we first erase the current flash on the board. this is done by using the following command:  
        `python -m esptool --chip esp8266 --port <COM-PORT-NAME> erase_flash`  
Step 3) Once the bin file of the kernel is downloaded, flash the ESP8266 board using this command:  
        `python -m esptool --chip esp8266 --port <COM-PORT-NAME> --baud 115200 write_flash --flash_size=detect 0 "<firmware-bin-file-path>"`  
  
Congratulations the ESP8266 board now has micropython kernel!  
  
## Transferring files from the computer to the ESP8266 board:  
in order to run the various projects, we need to transfer files from local computer to the ESP8622 board.  
Step 0) `Prerequisite`: To be able to transfer files from computer to the ESP8266 board, we need to install the adafruit-ampy library.  
        This can be done using the command: `pip install adafruit-ampy`.  
        `NOTE:` running the above pip install command installs ampy as an application. This application would be located in the `Scripts` folder of the python environment.  
  
Step 1) the default micropython kernel is configured in such a way that it first runs the `boot.py` file on the ESP board, and after that automatically runs the `main.py` file.  
Hence, any application that we develop will be called from this `main.py` file.  
Step 2) once the files are ready, we copy them over to the ESP board using the following command:  
`./ampy --port COM3 put <path-of-file-to-be-copied-to-the-ESP-board>`  
Step 3) Make sure that the intended application is called in main.py and that all the needed files are copied over to the board in order to run the application.  
