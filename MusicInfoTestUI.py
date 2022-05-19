import tkinter as tk
import json
import http.client

def showSongResults():
    """Get the necessary song info using the Deezer API and show it on the Results label.
    Use the Search endpoint and get the first song that appears in the search results."""
    #use the Deezer API's Search endpoint w/ the track connection
    conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com")
    headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "39a9bbd0f9msh1a6baf4688fe92dp1358c1jsn0c083022c4a5"
    }
    conn.request("GET", ('/search?q=track:"' + (ent_song.get()).replace(" ","%20") + '"'), headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    
    #get the first song's title
    title = data['data'][0]['title']
    #get the artist's name
    artist = data['data'][0]['artist']['name']
    #get the album name
    album = data['data'][0]['album']['title']
    #get the release date
    #release_date =
    #get the recording date
    #recording_date =
    #get the studio's name
    #studio =
    #get the song's genre
    #genre =
    #get the song's duration
    duration = data['data'][0]['duration']
    #get the record label
    #label =
    #get the songwriter(s)
    #songwriter =
    #get the producer(s)
    #producer =

    #print the resulting information
    lbl_result["text"] = "\"" + title + "\"\n" + artist + "\n" + album + "\n" + str(duration) + " seconds long"

def showArtistResults():
    """Get the necessary artist info using the Deezer API and show it on the Results label.
    Use the Search endpoint and get the artist of the first song that appears in the search results."""
    #use the Deezer API's Search endpoint w/ the artist connection
    conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com")
    headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "39a9bbd0f9msh1a6baf4688fe92dp1358c1jsn0c083022c4a5"
    }
    conn.request("GET", ('/search?q=artist:"' + (ent_artist.get()).replace(" ","%20") + '"'), headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    #TEST: print the duration (in seconds) of the first song that appears in the search results
    lbl_result["text"] = data['data'][0]['duration']

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
