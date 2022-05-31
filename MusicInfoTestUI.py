import os

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

import tkinter as tk
import json
import http.client

def showSongResults():
    """Get the necessary song info using the Deezer API and show it on the Results label.
    Use the Search endpoint and get the first song that appears in the search results."""
    box_contents = ent_song.get()
    #if the Song Title entry box is empty, don't do anything
    if not any(char.isalpha() for char in box_contents):
        return

    #use the Deezer API's Search endpoint w/ the track connection
    conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com")
    headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': str(API_KEY)
    }
    conn.request("GET", ('/search?q=track:"' + box_contents.replace(" ","%20") + '"'), headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    #if there are no items in "data", then ask the user to check their spelling
    if len(data['data']) < 1:
        results_text.configure(state='normal')
        results_text.delete("1.0","end")
        results_text.insert('end',"Sorry, we couldn't find any matching results. Try checking your spelling.")
        results_text.configure(state='disabled')
        return
    
    #get the first song's title
    title = data['data'][0]['title']
    #get the artist's name
    artist = data['data'][0]['artist']['name']
    #get the album name
    album = data['data'][0]['album']['title']
    #get the song's duration
    duration = data['data'][0]['duration']

    #get the information for the album that includes the song
    album_id = data['data'][0]['album']['id']
    #use the Album endpoint
    conn.request("GET", ('/album/' + str(album_id) + ''), headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    #get the release date
    release_date = data['release_date']
    #get the song's genre
    genre = data['genres']['data'][0]['name']
    #get the record label
    label = data['label']

    #print the resulting information
    results_text.configure(state='normal')
    results_text.delete("1.0","end")
    results_text.insert('end',f"\"{title}\"\n{artist}\n{album}\nReleased {release_date}\n{genre}\n{duration} seconds long\n{label}")
    results_text.configure(state='disabled')

def showArtistResults():
    """Get the necessary artist info using the Deezer API and show it on the Results label.
    Use the Search endpoint and get the artist of the first song that appears in the search results."""
    box_contents = ent_artist.get()
    #if the Artist Name entry box is empty, don't do anything
    if not any(char.isalpha() for char in box_contents):
        return

    #use the Deezer API's Search endpoint w/ the artist connection
    conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com")
    headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "39a9bbd0f9msh1a6baf4688fe92dp1358c1jsn0c083022c4a5"
    }
    conn.request("GET", ('/search?q=artist:"' + box_contents.replace(" ","%20") + '"'), headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    
    #get the artist's Deezer ID from the first song that appears in the search results
    artist_id = data['data'][0]['artist']['id']
    #get the artist's top track on Deezer
    top_song = data['data'][0]['title']

    #use the ID to get an artist object
    conn.request("GET", ('/artist/' + str(artist_id)), headers=headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))

    #get the artist's name
    name = data['name']
    #get the number of albums that the artist has released
    num_albums = data['nb_album']

    #print the resulting information
    results_text.configure(state='normal')
    results_text.delete("1.0","end")
    results_text.insert('end',f"{name}\n{num_albums} releases available on Deezer\nTop track on Deezer: \"{top_song}\"")
    results_text.configure(state='disabled')

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
lbl_artist = tk.Label(master=frm_entry, text="Artist Name")

ent_artist.grid(row=1, column=0, sticky="w", pady=10)
lbl_artist.grid(row=1, column=1, sticky="w", pady=10)

btn_artist = tk.Button(
    master=frm_entry,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=showArtistResults
)

btn_artist.grid(row=1, column=2, pady=10)

lbl_result = tk.Label(master=window, text="Results", anchor='w')

lbl_result.grid(row=2, column=0, padx=10, sticky="w")

#Here is the text area where the results will be displayed.
results_text = tk.Text(master=window, height=8, width=52, state='disabled')

results_text.grid(row=3, column=0, padx=10, sticky="w")

window.mainloop()
