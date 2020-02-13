"""
Module defines operation functions
"""

# constants naming indexes in sublist of album list

ARTIST = 0
TITLE = 1
YEAR = 2
GENRE = 3
LENGHT = 4


# supportive functions

def convert_time_to_seconds(time: str) -> int:
    """
    Converts time given in minutes:seconds
    to seconds
    :param str time: in format mm:ss
    :returns: time in seconds
    :rtype: int
    :raises: ValueError if given time format is incorrect
    """

    if ':' in time:
        time = time.split(':')

        try:
            minutes = int(time[0])
            seconds = int(time[1])

            time = minutes * 60 + seconds
            return time

        except TypeError:
            raise ValueError('Invalid time format')
    else:
        raise ValueError('Invalid time format')


def convert_seconds_to_minutes(seconds: int) -> float:
    """
    Converts time in seconds to minutes:seconds format
    :param int seconds: seconds
    :returns: time in minutes.seconds rounded to 2 decimal places
    :rtype: float
    """

    minutes = seconds // 60
    seconds = seconds % 60

    return round(minutes + seconds * 0.01, 2)


# main functions

def get_albums_by_genre(albums, genre):
    """
        Get albums by genre
        :param list albums: albums' data
        :param str genre: genre to filter by
        :returns: all albums of given genre
        :rtype: list
        """

    selected_genre_list = []

    for album in albums:
        if album[GENRE] == genre:
            selected_genre_list.append(album)

    if selected_genre_list:
        return selected_genre_list
    else:
        raise ValueError('Wrong genre')


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """

    if albums:
        longest_album_length = convert_time_to_seconds(albums[0][LENGHT])
        longest_album = albums[0]
        for album in albums:
            if convert_time_to_seconds(album[LENGHT]) > longest_album_length:
                longest_album_length = convert_time_to_seconds(album[LENGHT])
                longest_album = album

        return longest_album


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    total_albums_lt_seconds = 0
    for album in albums:
        total_albums_lt_seconds += convert_time_to_seconds(album[LENGHT])

    return convert_seconds_to_minutes(total_albums_lt_seconds)


def delete_album(albums, album_index: int):
    """
    Deletes album
    :param list albums: albums' data
    :param album_index: album index
    :returns: dict keys as genre names, values genre stats
    :rtype: dict
    """

    try:
        albums.remove(albums[album_index - 1])
        message = 'album removed'
    except IndexError:
        message = 'wrong album number'
    finally:
        return albums, message


def add_album(albums, album):
    """
    Ads new album
    :param list albums: albums' data
    :param list album: single album data list
    :returns: dict keys as genre names, values genre stats
    :rtype: dict
    """

    if len(album) != 5 or (not album[YEAR].isdigit()) or \
            ((not album[LENGHT][-1:-3].isdigit()) or (not album[LENGHT][-4:0].isdigit()) \
             or (':' not in album[LENGHT])):
        message = 'Invalid album format'
    else:
        albums.append(album)
        message = ''

    return albums


def get_genre_stats(albums):
    """
    Gets genres statistics
    :param list albums: albums' data
    :returns: dict keys as genre names, values genre stats
    :rtype: dict
    """

    genres_stats = {}
    for album in albums:
        if album[GENRE] in genres_stats:
            genres_stats[album[GENRE]] += 1
        else:
            genres_stats[album[GENRE]] = 1

    return genres_stats


def get_last_oldest(albums):
    """
    Gets the oldest album
    :param list albums: albums' data
    :returns: the oldest album
    :rtype: list
    """

    oldest_album = albums[0]
    oldest_album_year = int(albums[0][YEAR])

    for album in albums:
        if int(album[YEAR]) <= oldest_album_year:
            oldest_album_year = int(album[YEAR])
            oldest_album = album

    return oldest_album


def get_last_oldest_of_genre(albums, genre):
    """
    Gets oldest album in selected genre
    :param list albums: albums' data
    :param str genre: name of genre
    :returns: the oldest album
    :rtype: list
    """

    selected_genre_albums_list = []
    for album in albums:
        if album[GENRE] == genre:
            selected_genre_albums_list.append(album)

    if selected_genre_albums_list:
        oldest_album = selected_genre_albums_list[0]
        oldest_album_year = int(selected_genre_albums_list[0][YEAR])

        for album in selected_genre_albums_list:
            if int(album[YEAR]) <= oldest_album_year:
                oldest_album_year = int(album[YEAR])
                oldest_album = album

        return oldest_album

    else:
        raise ValueError('No albums with selected genre')