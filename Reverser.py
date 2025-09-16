import tkinter as tk #dette importerer tkinker som gjør at jeg kan lage GUI (graphical user interface)

def reverse(): #dette er funksjonen som reverserer teksten
    entry_text = entry.get() #dette henter teksten fra entry boksen
    result.set(entry_text[::-1]) #dette reverserer teksten og setter den i resultat variabelen

root = tk.Tk() #starten på programmet
root.title("Reverser Text") #tittelen på programmet
root.geometry("350x180") #størrelsen på program viunduet
root.configure(bg="#222831")  #bakgrunnsfargen

entry = tk.Entry(root, width=30, font=("Segoe UI", 12), bg="#393e46", fg="#eeeeee", insertbackground="#eeeeee", relief="flat") #dette er fonten og størrelsen på teksten som skal reverseres
entry.pack(pady=(20, 10)) #avstanden mellom teksten og knappen

btn = tk.Button(root, text="Reverse", command=reverse, font=("Segoe UI", 11, "bold"), bg="#00adb5", fg="#222831", activebackground="#393e46", activeforeground="#00adb5", relief="flat", padx=10, pady=5) #dette er knappen som reverserer teksten
btn.pack(pady=5) #avstanden mellom knappen og resultatet

result = tk.StringVar() #dette er resultatet av den reverserte teksten
lbl = tk.Label(root, textvariable=result, font=("Segoe UI", 13, "bold"), bg="#222831", fg="#00adb5") #dette er fonten og størrelsen på den reverserte teksten
lbl.pack(pady=10) #avstande mellom resultatet og bunnen av programmet

root.mainloop() #dette er slutten på programmet
