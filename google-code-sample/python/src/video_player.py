"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    flag = {}
    current = []
    all_playlists = {}

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def list_all_vids(self):
        all_vids = []
        with open("videos.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(" | ")
                all_vids += [line]
                if line[0] == 'Video about nothing':
                    line[1] = "nothing_video_id"
                    line += [""]
        all_vids = sorted(all_vids)
        return all_vids

    def show_all_videos(self):
        all_vids = VideoPlayer.list_all_vids(self)
        print("Here is a list of all available videos: ")
        for vid in all_vids:
            print("   " + vid[0], "("+vid[1]+")", "["+vid[2]+"]")

    def play_video(self, video_id, playing=False):
        global current
        try:
            if len(current)>0:
                playing = True
        except:
            pass
        def playing_vid():
            global current
            wrong_counter = 0
            all_vids = VideoPlayer.list_all_vids(self)
            for vid in all_vids:
                if video_id == vid[1]:
                    play_vid = vid
                    print("Playing video: " + play_vid[0])
                    current = play_vid
                    break
                else:
                    wrong_counter += 1
            if wrong_counter == len(all_vids):
                print("Cannot play video: Video does not exist")
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if playing == False:
            playing_vid()
        elif playing == True:
            VideoPlayer.stop_video(self)
            playing = False
            playing_vid()


    def stop_video(self):
        global current
        try:
            if len(current)>0:
                """Stops the current video."""
                print("Stopping video: " + current[0])
                current = ""
        except:
            print("Cannot stop video: No video is currently playing")




    def play_random_video(self):
        ran_vid=""
        ran_vid_id = ""
        all_ids = []
        all_vids = VideoPlayer.list_all_vids(self)
        for vid in all_vids:
            all_ids += [vid[1]]
        ran_vid_id = random.choice(all_ids)
        for vid in all_vids:
            if ran_vid_id in vid:
                ran_vid = vid
            #if len(flag[ran_vid[0]]) > 0:
                #print("No videos available")

        VideoPlayer.play_video(self, ran_vid_id)

    def pause_video(self, paused=0):
        try:
            global current
            """Pauses the current video."""
            if paused == 0:
                print("Pausing video: " + current[0] + " - PAUSED")
                paused = 1
            else:
                print("Cannot pause video: Video is not paused")
        except:
            print("Cannot pause video: no video is currently playing")

    def continue_video(self, cont=0):
        global current
        try:
            if len(current)==0:
                print("Cannot continue video: no video is currently continuing")
        except:
            if cont == 0:
                print("Continuing video: " + current[0])
            """Resumes playing the current video."""
            if cont == 1:
                print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        global current
        try:
            if len(current) > 0:
                print("Currently playing: " + current[0], "("+current[1]+")", "["+current[2]+"]")
        except:
            try:
                if len(current) == 0:
                    print("No video is currently playing")
            except:
                pass

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        global all_playlists
        for playlist in all_playlists:
            if playlist_name.lower() == playlist.lower():
                all_playlists[playlist_name] = []
                print("Successfully created new playlist: " + playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        wrong_counter = 0
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        global all_playlists
        all_vids = VideoPlayer.list_all_vids(self)
        if playlist_name in all_playlists:
            for vid in all_vids:
                if video_id in vid:
                    if vid in all_playlists[playlist_name]:
                        print("Cannot add video to " + playlist_name + ": Video is already added")
                    adding = vid
                    all_playlists[playlist_name] += [adding]
                    print("Added video to " + playlist_name + ": " + adding[0])
                else:
                    wrong_counter += 1
            if len(all_vids) == wrong_counter:
                print("Cannot add video to " + playlist_name + ": Video does not exist")
        else:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        try:
            global all_playlists
            if len(all_playlists) > 0:
                print("Showing all playlists:")
                for playlist in all_playlists:
                    print("   " + playlist)
        except:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        global all_playlists
        if playlist_name in all_playlists:
            print("Showing playlist: " + playlist_name)
            for vid in playlist_name:
                print(vid)
        elif playlist_name not in all_playlists:
            print("Cannot show" + playlist_name + "Playlist does not exist")
        elif len(all_playlists[playlist_name]) == 0:
            print("No videos here yet")

    def remove_from_playlist(self, playlist_name, video_id):
        removing = True
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        global all_playlists
        rem_vid = []
        all_vids = VideoPlayer.list_all_vids(self)
        for vid in all_vids:
            if video_id in vid:
                rem_vid = vid
                removing = True
                break
            else:
                removing = False
        if removing == True:
            if playlist_name in all_playlists:
                try:
                    all_playlists[playlist_name].remove(rem_vid)
                    print("Removed video from " + playlist_name + ": " + rem_vid[0])
                except:
                    print("Cannot remove video from " + playlist_name + ": Video is not in playlist")
            else:
                print("Cannot remove video from " + playlist_name + ": Playlist does not exist")
        else:
            print("Cannot remove video from " + playlist_name + ": Video does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        global all_playlists
        if playlist_name in all_playlists:
            all_playlists[playlist_name] = []
            print("Successfully removed all videos from " + playlist_name)
        else:
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        global all_playlists
        if playlist_name in all_playlists:
            del all_playlists[playlist_name]
            print("Deleted playlist " + playlist_name)
        else:
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")

    def search_videos(self, search_term):
        results = {}
        index = 1
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        lwr_search = search_term.lower()
        all_vids = VideoPlayer.list_all_vids(self)
        for vid in all_vids:
            if lwr_search in vid[0].lower() or lwr_search in vid[1].lower():
                results[str(index)] = [vid]
                index += 1
        index = 1
        if len(results) > 0:
            print("Here are the results for " + search_term)
            for result in results:
                print(str(index) + ")" + result)
        else:
            print("No search results for " + search_term)
        answer = input("Would you like to play any of the above? If yes, specify the number of the video. If your answer is not a valid number, we will assume it is a no.")
        try:
            answer = int(answer)
            if answer in results:
                VideoPlayer.play_video(self, results[str(answer)][1])
        except:
            pass

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        results = {}
        index = 1
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        lwr_search = video_tag.lower()
        all_vids = VideoPlayer.list_all_vids(self)
        for vid in all_vids:
            if lwr_search in vid[2].lower():
                results[str(index)] = [vid]
                index += 1
        index = 1
        if len(results) > 0:
            print("Here are the results for " + video_tag)
            for result in results:
                print(str(index) + ")" + result)
        else:
            print("No search results for " + video_tag)
        answer = input("Would you like to play any of the above? "
                       "If yes, specify the number of the video. "
                       "If your answer is not a valid number, we will assume it is a no.")
        try:
            answer = int(answer)
            if answer in results:
                VideoPlayer.play_video(self, results[str(answer)][1])
        except:
            pass

    def flag_video(self, video_id, flag_reason=""):
        global flag
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        all_vids = VideoPlayer.list_all_vids(self)
        for vid in all_vids:
            if video_id in vid:
                if vid[0] in flag:
                    print("Cannot flag video: Video is currently flagged (reason:"+ flag[vid[0]] +")")
                    break
                else:
                    print("Successfully flagged video: "+ vid[0] + "(reason: "+ flag_reason +")")
                    flag[vid[0]] = flag_reason
                    break
            else:
                print("Cannot flag video: Video does not exist")
                break



    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        global flag
        all_vids = VideoPlayer.list_all_vids(self)
        for vid in all_vids:
            if len(flag[vid[0]]) > 0:
                del flag[vid[0]]
                print("Successfully removed flag from video: " + vid[0])
                break
            elif len(flag[vid[0]]) == 0:
                print("Cannot remove flag from video: Video is not flagged")
            else:
                print("Cannot remove flag from video: Video does not exist")
