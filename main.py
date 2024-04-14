from pytube import YouTube
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

session = PromptSession()
console = Console()
style = Style.from_dict({
    '': 'bold bg:#7c7878 #000000', # Input field with light grey background and black text
    'prompt': 'bold #ffffff bg:#8B0000', # Prompt with green background and white text
})


text_title = Text("TubeTaker\nfast video downloader", style="bold white", justify="center")
panel = Panel(text_title, style="bold white on #8B0000", expand=True)

def main():
    with open("/home/lurbaby/dev_lurbaby/TubeTaker/video_counter.txt", "r") as count_videos:
        i = int(count_videos.read())+1

    while True:
        url = session.prompt("Video URL: ", style=style)

        if str(url) == "exit" or len(url) == 0:
            final_msg = Text(f"Thanks for use!", justify="center")
            final_panel = Panel(final_msg, style="bold blue on blue", expand=True)
            console.print(final_panel)
            break

        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download(output_path='/home/lurbaby/Downloads/dw_videos')
        except:
            final_msg = Text(f"Something went wrong!", justify="center")
            final_panel = Panel(final_msg, style="bold white on #FFA500", expand=True)
            console.print(final_panel)
            continue

        url_panel = Panel(f"SUCCESS!", style="bold black on green", expand=True)

        console.print(url_panel)


if __name__ == "__main__":
    console.print(panel)
    main()
