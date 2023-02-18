import tkinter as tk
import time
import threading
import sys
import os
import pygame

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def play_crash_sound():
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound("music.wav")
    sounda.play()

root = tk.Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root['bg'] = '#000000'
root.config(cursor="none")

empty = tk.PhotoImage(file=resource_path('empty.png'))
qr_code = tk.PhotoImage(file=resource_path('qr.png'))

def bsod():
    root['bg'] = '#003586'

    frame = tk.Frame(root, bg='#003586')
    frame.grid(row=0, column=0, padx=202, pady=105)

    face_label = tk.Label(frame, text='', font=('Segoe UI', 155), fg='white', bg='#003586', anchor='w', justify='left')
    face_label.grid(row=0, column=0, sticky='w')

    def renderText():
        time.sleep(0.1)
        face_label.config(text=':')
        time.sleep(0.1)
        face_label.config(text = ':(')
        time.sleep(0.25)
        text_label = tk.Label(frame, text='', font=('Segoe UI Semilight', 30), fg='white', bg='#003586', anchor='w', wraplength=700, justify='left')
        text_label.grid(row=1, column=0)
        text_label.config(text='Your de')
        time.sleep(0.05)
        text_label.config(text = 'Your device ran into a problem')
        time.sleep(0.05)
        text_label.config(text='Your device ran into a problem and needs to re')
        time.sleep(0.05)
        text_label.config(text='Your device ran into a problem and needs to restart.')
        time.sleep(0.05)
        text_label.config(text='Your device ran into a problem and needs to restart. We\'r')
        time.sleep(0.025)
        text_label.config(text='Your device ran into a problem and needs to restart. We\'re jus')
        time.sleep(0.025)
        text_label.config(text='Your device ran into a problem and needs to restart. We\'re just coll')
        time.sleep(0.025)
        text_label.config(text='Your device ran into a problem and needs to restart. We\'re just collecting some error info,')
        time.sleep(0.025)
        text_label.config(text='Your device ran into a problem and needs to restart. We\'re just collecting some error info, and t')
        time.sleep(0.025)
        text_label.config(text='Your device ran into a problem and needs to restart. We\'re just collecting some error info, and then we\'ll')
        time.sleep(0.025)
        text_label.config(text='Your device ran into a problem and needs to restart. We\'re just collecting some error info, and then we\'ll restart fo')
        time.sleep(0.025)
        text_label.config(text='Your device ran into a problem and needs to restart. We\'re just collecting some error info, and then we\'ll restart for you.')
        text_label2 = tk.Label(frame, text='', font=('Segoe UI Semilight', 30), fg='white', bg='#003586', anchor='w', wraplength=700, justify='left', height=2)
        text_label2.grid(row=2, column=0, sticky='w')
        frame2 = tk.Frame(frame, bg='#003586')
        frame2.grid(row=3, column=0, sticky='w')
        label = tk.Label(frame2, bg='#003586')
        image = empty
        label.config(image=image)
        label.pack(side='left', pady=10)
        label2 = tk.Label(frame2, bg='#003586')
        label2.config(text="", font=('Segoe UI Semilight', 15), fg='white', wraplength=400, anchor='n', justify='left', compound='left')
        label2.pack(padx=10)
        label3 = tk.Label(frame2, bg='#003586')
        label3.config(text="", font=('Segoe UI Semilight', 12), fg='white', wraplength=700, anchor='n', justify='left')
        label3.pack(side='left', padx=10)
        time.sleep(1.2)
        label2.config(text='For more information about this issue and possible fixes, visit')
        time.sleep(0.015)
        label2.config(text='For more information about this issue and possible fixes, visit https://w')
        time.sleep(0.015)
        label2.config(text='For more information about this issue and possible fixes, visit https://www.windows.com/stopcode')
        label3.config(text='If you call a support person, give')
        time.sleep(0.015)
        label3.config(text='If you call a support person, give them this info:' + "\n" + 'Stop code: PAGE_FAULT_IN_NONPAGED')
        time.sleep(0.015)
        label3.config(text='If you call a support person, give them this info:' + "\n" + 'Stop code: PAGE_FAULT_IN_NONPAGED_AREA')
        time.sleep(0.015)
        image2 = qr_code
        label.config(image=image2)
        time.sleep(0.015)
        def crashDump():
            for i in range(0, 6):
                try:
                    time.sleep(2)
                    text_label2.config(text=str(i * 20) + "% complete")
                except Exception as e:
                    break

        crash_dump_thread = threading.Thread(target=crashDump)
        crash_dump_thread.start()

    threading.Thread(target=renderText).start()

play_crash_sound()
root.after(1000, bsod)
root.mainloop()