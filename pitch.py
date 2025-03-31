import yt_dlp
import os
import argparse

#Do give credits if you are re-using this code.

# Function to display an ASCII art logo
def display_ascii_art():
    ascii_art = '''
    \033[32m

    

    
██████╗ ██╗████████╗ ██████╗██╗  ██╗
██╔══██╗██║╚══██╔══╝██╔════╝██║  ██║
██████╔╝██║   ██║   ██║     ███████║
██╔═══╝ ██║   ██║   ██║     ██╔══██║
██║     ██║   ██║   ╚██████╗██║  ██║
╚═╝     ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝




    \033[0m
    '''
    print(ascii_art)

# function to download audio from YouTube
def download_audio(url: str, download_path: str):
    ydl_opts = {
        'format': 'bestaudio/best',  # downloading the best audio format available. you can even change to this your preffered quality.
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'), #output source
        'quiet': False,  # set to true to hide logs
        'noplaylist': True,  # disables playlist downloading by default.
    }

    # Download the audio using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Main function to handle arguments and download process
def main():
    # Display ASCII art
    display_ascii_art()

    while True:
        #Video url input
        video_url = input("Enter the YouTube URL: ")
        
        #Audio download path
        download_path = input("Enter the absolute-path to save the song: ")
        
        #Error handling by ensuring if the path exists.
        if not os.path.exists(download_path):
            print(f"Path '{download_path}' does not exist. Creating the directory...")
            os.makedirs(download_path)
        
        #Downloading to the preffered location by calling the download_audio function
        download_audio(video_url, download_path)
        print("Download complete!")
        
        #Asking user choice to download another song
        user_choice = input("Do you want to download another song? ((Y)es/(N)o): ").lower()
        if user_choice != 'yes' or 'y' or 'Yes':
            print("Goodbye! Enjoy listening!")
            break

if __name__ == "__main__":
    main()
