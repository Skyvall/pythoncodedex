import functools


# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]


def under_5(list_of_songs):
    """Filter songs with duration under 5 minutes."""
    return list(filter(lambda song: song[1] < 5, list_of_songs))


under_5_songs = under_5(playlist)
print(under_5_songs)
