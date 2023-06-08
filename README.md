# Protocol-Manual method - Rootqit (NOT FULLY FINISHED YET) 
First of all, this only works on windows 10. I think it could also work on windows 7 and 8, but I never tested it.
With this simple template, you can go to for example startaprogram://spotify in your everyday browser and it will start spotify.
You could technically also set shortcuts for this, so if you type @sp in your browser search bar it will automatically go to startaprogram://spotify. But we can do that at the end.
First, press the WIN button on your keyboard and search for cmd. Then press on start as administrator.
When you have the cmd running with admin privileges, type in "regedit". A bright explorer-like window will appear. 
If there are any folders open on the left of your screen, close them. But dont delete anything lmao.
After you closed all of them, there should only be 5 left: "HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS and HKEY_CURRENT_CONFIG.
Then, right click on HKEY_CLASSES_ROOT, and press on new -> key. Call it "vStart". Now, right click on the freshly created key and go on new -> String value. Just call that string value 'URL Protocol' but dont set any data.
Were already almost finished but you still have to click on the vStart key again, then press on new -> key again and name it 'shell' this time. Again, press on the new value and create another key named 'open', and then again, press on the open key and 
create a new one called 'command'. Then in that key, you will see one singular REG_SZ key. Right click it and change the value to "c:\proc\menu.bat" "%1". Were now done with the registry editor.
Were now done with the registry editor, now just download all the files from this repo into 'C:\proc\*' ( the files should go where the * is).
# TUTORIAL/README NOT FINISHED YET - COMING SOON
