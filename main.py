from tkinter import Tk, Label, Button, filedialog, SE, SW, S, Text, END, DISABLED
import re
import os
from pandas import DataFrame
import time

File = ''
FileLoc = ''
apktool_loc = 'D:/apktool'  # change accordingly
df: DataFrame


def browseFiles():
    global apktool_loc
    global File
    global FileLoc
    File = ''
    FileLoc = ''
    button_extract_perms["state"] = DISABLED
    filename = filedialog.askopenfilename(title="Select a File",
                                          filetypes=[("APK File", "*.apk")])

    x = len(filename) - 1
    while filename[x] != '/':
        File += filename[x]
        x -= 1

    File = File[::-1]
    FileLoc = filename
    label_permission1.config(state="normal")
    label_permission2.config(state="normal")
    label_permission3.config(state="normal")
    if label_permission1.get("1.0", END) != "\n":
        label_permission1.delete("1.0", END)
    if label_permission2.get("1.0", END) != "\n":
        label_permission2.delete("1.0", END)
    if label_permission3.get("1.0", END) != "\n":
        label_permission3.delete("1.0", END)
    label_permission1.config(state=DISABLED)
    label_permission2.config(state=DISABLED)
    label_permission3.config(state=DISABLED)
    
    label_file_explorer.configure(text="APK under analysis: " + File)

    button_export["state"] = "disable"
    button_extract_perms["state"] = "normal"


def apktool():
    global df
    dangerous = ["android.permission.ACCEPT_HANDOVER",
                 "android.permission.ACCESS_BACKGROUND_LOCATION",
                 "android.permission.ACCESS_COARSE_LOCATION",
                 "android.permission.ACCESS_FINE_LOCATION",
                 "android.permission.ACCESS_MEDIA_LOCATION",
                 "android.permission.ACTIVITY_RECOGNITION",
                 "com.android.voicemail.permission.ADD_VOICEMAIL",
                 "android.permission.ANSWER_PHONE_CALLS",
                 "android.permission.BODY_SENSORS",
                 "android.permission.CALL_PHONE",
                 "android.permission.CAMERA",
                 "android.permission.DOWNLOAD_WITHOUT_NOTIFICATION",
                 "android.permission.GET_ACCOUNTS",
                 "android.permission.PROCESS_OUTGOING_CALLS",
                 "android.permission.READ_CALL_LOG",
                 "android.permission.READ_CALENDAR",
                 "android.permission.READ_CONTACTS",
                 "android.permission.READ_EXTERNAL_STORAGE",
                 "android.permission.READ_PHONE_NUMBERS",
                 "android.permission.READ_PHONE_STATE",
                 "com.android.launcher.permission.READ_SETTINGS",
                 "android.permission.READ_SMS",
                 "android.permission.RECEIVE_MMS",
                 "android.permission.RECEIVE_SMS",
                 "android.permission.RECEIVE_WAP_PUSH",
                 "android.permission.RECORD_AUDIO",
                 "android.permission.SEND_SMS",
                 "android.permission.USE_SIP",
                 "android.permission.WRITE_CALENDAR",
                 "android.permission.WRITE_CALL_LOG",
                 "android.permission.WRITE_CONTACTS",
                 "android.permission.WRITE_EXTERNAL_STORAGE"]
    signature = ["android.permission.MOUNT_UNMOUNT_FILESYSTEMS", "android.permission.BATTERY_STATS",
                 "android.permission.BIND_ACCESSIBILITY_SERVICE", "android.permission.BIND_AUTOFILL_SERVICE",
                 "android.permission.BIND_CALL_REDIRECTION_SERVICE",
                 "android.permission.BIND_CARRIER_MESSAGING_CLIENT_SERVICE", "android.permission.BIND_CARRIER_SERVICES",
                 "android.permission.BIND_CHOOSER_TARGET_SERVICE", "android.permission.BIND_CONDITION_PROVIDER_SERVICE",
                 "android.permission.BIND_DEVICE_ADMIN", "android.permission.BIND_DREAM_SERVICE",
                 "android.permission.BIND_INCALL_SERVICE", "android.permission.BIND_INPUT_METHOD",
                 "android.permission.BIND_MIDI_DEVICE_SERVICE", "android.permission.BIND_NFC_SERVICE",
                 "android.permission.BIND_NOTIFICATION_LISTENER_SERVICE", "android.permission.BIND_PRINT_SERVICE",
                 "android.permission.BIND_QUICK_ACCESS_WALLET_SERVICE", "android.permission.BIND_REMOTEVIEWS",
                 "android.permission.BIND_SCREENING_SERVICE", "android.permission.BIND_TELECOM_CONNECTION_SERVICE",
                 "android.permission.BIND_TEXT_SERVICE", "android.permission.BIND_TV_INPUT",
                 "android.permission.BIND_VISUAL_VOICEMAIL_SERVICE", "android.permission.BIND_VOICE_INTERACTION",
                 "android.permission.BIND_VPN_SERVICE", "android.permission.BIND_VR_LISTENER_SERVICE",
                 "android.permission.BIND_WALLPAPER", "android.permission.CHANGE_CONFIGURATION",
                 "android.permission.CLEAR_APP_CACHE", "android.permission.DELETE_CACHE_FILES",
                 "android.permission.GET_ACCOUNTS_PRIVILEGED", "android.permission.GLOBAL_SEARCH",
                 "android.permission.INSTANT_APP_FOREGROUND_SERVICE", "android.permission.LOADER_USAGE_STATS",
                 "android.permission.MANAGE_EXTERNAL_STORAGE", "android.permission.PACKAGE_USAGE_STATS",
                 "com.android.voicemail.permission.READ_VOICEMAIL", "android.permission.REQUEST_INSTALL_PACKAGES",
                 "android.permission.SMS_FINANCIAL_TRANSACTIONS", "android.permission.START_VIEW_PERMISSION_USAGE",
                 "android.permission.SYSTEM_ALERT_WINDOW", "android.permission.WRITE_SETTINGS",
                 "com.android.voicemail.permission.WRITE_VOICEMAIL"]

    global File
    global apktool_loc
    global FileLoc
    if not os.path.isdir(apktool_loc + "/" + File.replace('.apk', '')):
        os.system(f"powershell.exe cd '{apktool_loc}'; apktool.jar d '{FileLoc}'")
        time.sleep(5)
    File = File.replace('.apk', '')
    f = open(f"{apktool_loc}/{File}/AndroidManifest.xml", "r")

    label_permissions.configure(text="Permissions: Dangerous")
    label_permissions_legend.configure(text="Signature")
    label_permissions_legend2.configure(text="Normal")

    label_permission1.config(state="normal")
    label_permission2.config(state="normal")
    label_permission3.config(state="normal")
    if label_permission1.get("1.0", END) != "\n":
        label_permission1.delete("1.0", END)
    if label_permission2.get("1.0", END) != "\n":
        label_permission2.delete("1.0", END)
    if label_permission3.get("1.0", END) != "\n":
        label_permission3.delete("1.0", END)

    perms = {'name': list(), 'protection': list()}
    for x in f:
        # print(x)
        if "<uses-permission" in x:
            if "android.permission" in x or "com.android" in x:
                s = re.search(r'android:name=".+"', x)[0].replace('"', '').replace('android:name=', '')
                perms['name'].append(s)
                if s in dangerous:
                    label_permission1.insert(END, s + '\n')
                    perms['protection'].append('dangerous')
                elif s in signature:
                    label_permission2.insert(END, s + '\n')
                    perms['protection'].append('signature')
                else:
                    label_permission3.insert(END, s + '\n')
                    perms['protection'].append('normal')

    label_permission1.config(state=DISABLED)
    label_permission2.config(state=DISABLED)
    label_permission3.config(state=DISABLED)

    df = DataFrame(perms, columns=['name', 'protection'])
    f.close()
    button_extract_perms["state"] = "normal"
    button_export["state"] = "normal"


def exportCSV():
    global df

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv',
                                                    filetypes=[("Comma Separated Value File", '*.csv')])
    df.to_csv(export_file_path, index=False, header=True)


window = Tk()
window.title('APK Permissions Analysis')

label_file_explorer = Label(window,
                            text="Select an APK File",
                            height=2,
                            fg="black")
label_file_explorer.grid(row=0,
                         column=0,
                         columnspan=3)

label_permissions = Label(window,
                          text="",
                          height=2,
                          fg="blue")
label_permissions.grid(row=2,
                       column=0)

label_permissions_legend = Label(window,
                                 text="",
                                 height=2,
                                 fg="blue")
label_permissions_legend.grid(row=2,
                              column=1)

label_permissions_legend2 = Label(window,
                                  text="",
                                  height=2,
                                  fg="blue")
label_permissions_legend2.grid(row=2,
                               column=2)

button_explore = Button(window,
                        text="Browse APK",
                        command=browseFiles)
button_explore.grid(row=1,
                    column=0,
                    sticky=SW,
                    padx=5)

button_exit = Button(window,
                     text="Exit",
                     command=exit)
button_exit.grid(row=1,
                 column=2,
                 sticky=SE,
                 padx=5)

button_extract_perms = Button(window,
                              text="Extract permissions",
                              command=apktool)
button_extract_perms.grid(row=1,
                          column=1,
                          sticky=S)
button_extract_perms["state"] = "disable"

button_export = Button(window,
                       text="Export as CSV",
                       command=exportCSV)
button_export.grid(row=4,
                   column=1,
                   sticky=S,
                   pady=5)
button_export["state"] = "disable"

label_permission1 = Text(window,
                         fg="red")
label_permission1.grid(row=3,
                       column=0)

label_permission2 = Text(window,
                         fg="orange")
label_permission2.grid(row=3,
                       column=1)

label_permission3 = Text(window,
                         fg="green")
label_permission3.grid(row=3,
                       column=2)

label_permission1.config(state=DISABLED)
label_permission2.config(state=DISABLED)
label_permission3.config(state=DISABLED)

window.grid_columnconfigure(0, weight=3)
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=2)
window.geometry(f"{int(window.winfo_screenwidth() / 1.3)}x{int(window.winfo_screenheight() / 1.6)}")
window.maxsize(int(window.winfo_screenwidth()), int(window.winfo_screenheight()))
# window.maxsize(int(window.winfo_screenwidth()/1.2),int(window.winfo_screenheight()/1.2))
window.mainloop()
