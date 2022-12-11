#Your goal in this question is to create a playlist (that is, a list of songs) by your friend's favorite artists.
#
#Write a function called playlist. playlist should have two parameters. The first parameter is a dictionary, where the keys are band names and the values are song names. The second parameter is a list of strings, where each string is an artist.
#
#playlist should return a list of all songs by the bands listed in the second parameter, sorted alphabetically. If there are no matching artists, return "I guess I don't mind ads on the radio that much"
#
#For example:
#artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"],\
#                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
#                     ["Sign of the Times", "Adore You", "Falling"], "AC/DC":\
#                     ["TNT", "It's a long way to the top", "Thunderstruck"]}
#friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
#playlist(artists_and_songs, friends_artists) -> ["It's a long way to the top", "Memories", "Payphone", "Sugar", "TNT", "Thunderstruck"]


#Write your code here!
def playlist(my_dict, artists):
    res_list = []
    for artist in artists:
        if artist in my_dict.keys():
            res_list += my_dict[artist]
    res_list.sort()
    if res_list == []:
        return "I guess I don't mind ads on the radio that much"
    return res_list
    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ["It's a long way to the top", "Memories", "Payphone", "Sugar", "TNT", "Thunderstruck"]
artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"],\
                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
                     ["Sign of the Times", "Adore You", "Falling"], "AC/DC":\
                     ["TNT", "It's a long way to the top", "Thunderstruck"]}
friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
print(playlist(artists_and_songs, friends_artists))

