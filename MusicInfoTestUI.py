import tkinter as tk

def showSongResults():
    """Get the necessary song info using the API and show it on the Results label."""
    #use the API
    lbl_result["text"] = "yes"

def showArtistResults():
    """Get the necessary artist info using the API and show it on the Results label."""
    #use the API
    lbl_result["text"] = "no"

window = tk.Tk()
window.title("Music Info")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_song = tk.Entry(master=frm_entry, width=10)
lbl_song = tk.Label(master=frm_entry, text="Song Title")

ent_song.grid(row=0, column=0, sticky="w")
lbl_song.grid(row=0, column=1, sticky="w")

btn_song = tk.Button(
    master=frm_entry,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=showSongResults
)

frm_entry.grid(row=0, column=0, padx=10)
btn_song.grid(row=0, column=2, pady=10)

ent_artist = tk.Entry(master=frm_entry, width=10)
lbl_artist = tk.Label(master=frm_entry, text="Artist")

ent_artist.grid(row=1, column=0, sticky="w", pady=10)
lbl_artist.grid(row=1, column=1, sticky="w", pady=10)

btn_artist = tk.Button(
    master=frm_entry,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=showArtistResults
)

btn_artist.grid(row=1, column=2, pady=10)

lbl_result = tk.Label(master=window, text="Results")

lbl_result.grid(row=2, column=0, padx=10, sticky="w")

window.mainloop()
