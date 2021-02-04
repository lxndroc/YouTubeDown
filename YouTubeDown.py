"""
---------------------------------------------------
                   YouTubeDown v2020
                      by @lxndroc
---------------------------------------------------
        Downloads Selected YouTube Video Streams
        Requires Python 3 & the package pytube.
"""

from pytube import YouTube

class YouTubeDown:
    def __init__(self):
        self.url = ''
        self.path = '.'
        self.title = ''
        self.streams = None
        self.selected_streams_list = []
        self.main()

    def main(self):
        print('\n\t\t\t+ YouTube Downloader v2020 +',
              '\n\t\t\t\tby @lxndroc')
        self.run_menu()

    def read_url(self):
        self.url = input(' Enter YouTube URL Or Code To Download: ')
        # e.g. T_XE910ikbwv
        if 'https' not in self.url:
            self.url = f'https://www.youtube.com/watch?v={self.url}'
        self.set_title_and_streams()
        
    def set_title_and_streams(self):
        youtube_object = YouTube(self.url)
        self.title = youtube_object.title
        self.streams = youtube_object.streams

    def read_path(self):
        self.path = input(' Enter Folder To Save The Stream Files: ')

    def show_streams(self):
        if not self.url:
            print(' URL Not Set!')            
            return
        print(' Available Streams')
        streams_number = len(self.streams) if self.streams else 0
        for stream_no in range(1, streams_number + 1):
            print(f' {stream_no}. {" ".join(str(self.streams[stream_no - 1]).split()[2:-1])}')
        print(' Streams With Both Video & Audio Have progressive="True"')
        input(' Press Enter To Continue...')

    def select_streams(self):
        if not self.url:
            print(' URL Not Set!')
            return
        selected_streams = input(' Select Streams Separated By Space: ')
        self.selected_streams_list = selected_streams.split()

    def download_streams(self):
        if not self.url:
            print(' URL Not Set!')            
            return
        if not self.selected_streams_list:
            print(' Streams Not Selected!')            
            return            
        print(' Streams Download Started!')
        for selected_stream in self.selected_streams_list:
            filename = f'{self.streams[0].default_filename[:-4]}_{selected_stream}'
            self.streams[int(selected_stream) - 1].download(self.path, filename)
            print(f' Stream #{selected_stream} Download Completed! Saved To file: {path}/{filename}.mp4')
        print(' Streams Download Completed!')

    def read_menu_choice(self):
        return input(f"""
    1. Set URL Or Token
        Sets the YouTube video URL or token
        Current URL: {self.url if self.url else '-'}
        Current Title: {self.title if self.url else '-'}
    2. Set Path
        Sets the path to store the video
        Current: {self.path if self.path else '-'}
    3. Show Streams
        Shows the available video streams to download
        Current Number: {len(self.streams) if self.streams else 0}
    4. Select Streams
        Selects the video streams to download
        Current: {', '.join(self.selected_streams_list) if self.selected_streams_list else '-'}
    5. Download Streams
        Downloads the selected video streams
    0. Exit
        Exits the program
    Enter option: """)

    def run_menu(self):
        while True:
            choice = self.read_menu_choice()
            print()
            # 1. Set URL Or Token
            if choice == '1':
                self.read_url()
            # 2. Set Path
            elif choice == '2':
                self.read_path()
            # 3. Show Streams
            elif choice == '3':
                self.show_streams()
            # 4. Select Streams
            elif choice == '4':
                self.select_streams()
            # 5. Download Streams
            elif choice == '5':
                self.download_streams()
            # 0. Exit
            elif choice == '0':
                print(' Program Exited')
                break
            # Invalid option
            else:
                print(' Invalid Option, Retry')
                continue

YouTubeDown()
