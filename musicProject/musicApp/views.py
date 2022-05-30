from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.
def index(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='d08de6e4053846fca522bcbd507aca93',client_secret='f2ea7d13cbb2472588b5415f18e0e19f',))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks'][:5]
        return render(request,'index.html',{"results":final_result})
    else:
      return render(request,'index.html',)