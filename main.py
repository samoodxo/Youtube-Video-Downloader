import customtkinter as ctk
import threading
import pytube as yt
from customtkinter import *
from pytube import *

#Define Window and Specifications
Window = ctk.CTk()
Window.title("Youtube Video Downloader")
Window.iconbitmap("logo.ico")
Window.geometry("800x600")
Window.maxsize(800,600)


#Data Requested From User
Program_Title = ctk.CTkLabel(Window,text="Youtube Video Downloader", font=("Helvetica",24,"bold"))
Program_Title.pack(pady=15)

Url_Label = ctk.CTkLabel(Window,text="Enter Url", font=("Helvetica",16,"bold"))
Url_Label.pack(pady=10)

Url_Textbox = ctk.CTkTextbox(Window,height=0,width=350)
Url_Textbox.pack()

#Download Button & Function
def download_video_thread():
    def download_video():
        if mp3var.get() == "on" and mp4var.get() == "on":
            try:
                link = yt.YouTube(Url_Textbox.get("1.0", "end-1c"))
                audio = link.streams.get_audio_only()
                audio.download("Downloaded Videos And Audios",filename=f"{link.title}.mp3")
                video = link.streams.get_highest_resolution()
                video.download("Downloaded Videos And Audios")
                Download_Status_Var.set("Download Status: Audio and Video Downloaded!")
            except:
                Download_Status_Var.set("Download Status: Error")
        elif mp4var.get() == "on":
            try:
                link = yt.YouTube(Url_Textbox.get("1.0", "end-1c"))
                vid = link.streams.get_highest_resolution()
                vid.download("Downloaded Videos And Audios")
                Download_Status_Var.set("Download Status: Video Downloaded!")
            except:
                Download_Status_Var.set("Download Status: Error")
        elif mp3var.get() == "on":
            try:
                link = yt.YouTube(Url_Textbox.get("1.0", "end-1c"))
                audio = link.streams.get_audio_only()
                audio.download("Downloaded Videos And Audios",filename=f"{link.title}.mp3")
                Download_Status_Var.set("Download Status: Audio Downloaded!")
            except:
                Download_Status_Var.set("Download Status: Error")
        

    download_thread = threading.Thread(target=download_video)
    download_thread.start()


def Clear_buttons():
    mpeg_3_checkbox.deselect()
    mpeg_4_checkbox.deselect()


#Filetypes
mp4var = ctk.StringVar(value="off")
mp3var = ctk.StringVar(value="off")

mpeg_3_checkbox = ctk.CTkCheckBox(Window,text="MP3",variable=mp3var,onvalue="on",offvalue="off",border_width=2,font=("inter",12))
mpeg_3_checkbox.pack(pady=15)

mpeg_4_checkbox = ctk.CTkCheckBox(Window,text="MP4",variable=mp4var,onvalue="on",offvalue="off",border_width=2,font=("inter",12))
mpeg_4_checkbox.pack(pady=10)

#Download Button
Download_Button = ctk.CTkButton(Window,text="Download Video",fg_color="red",hover=False,command=download_video_thread)
Download_Button.configure(cursor="hand2")
Download_Button.pack(pady=20)

#Clear Checkbox Button
Clear_Button = ctk.CTkButton(Window,text="Clear Checkbox",fg_color="red",hover=False,command=Clear_buttons)
Clear_Button.configure(cursor="hand2")
Clear_Button.pack(pady=2)


#Download Status
Download_Status_Var = ctk.StringVar()
Download_Status_Var.set("Download Status: ")
Download_Status_Label = ctk.CTkLabel(Window,textvariable=Download_Status_Var,font=("Inter",16,"bold"))
Download_Status_Label.pack(pady=10)


#Data Obtained and Shown in Program
Video_Information_Label = ctk.CTkLabel(Window,text="Video Information",font=("Helvetica",24,"bold"))
Video_Information_Label.pack(pady=25)


#Video Title Info and Retrive Title Info
Title_Var = ctk.StringVar()
Title_Var.set("Title: ")
Title_Label = ctk.CTkLabel(Window,textvariable = Title_Var)
Title_Label.pack()

def update_title(event=None):
    url = Url_Textbox.get("1.0", "end-1c")
    if url.startswith("https://www.youtube.com/watch?v=" or "https://youtu.be/" or "https://www.youtube.com/shorts/"):
        Download_Status_Var.set("Download Status: ")
        try:
            link = yt.YouTube(url)
            title = link.title
            Title_Var.set("Title: " + title)
        except:
            Title_Var.set("Error fetching title")
    else:
        Title_Var.set("Invalid YouTube URL")


#Retrive Channel Name
Channel_Name_Var = ctk.StringVar()
Channel_Name_Var.set("Channel: ")
Channel_Name_Label = ctk.CTkLabel(Window,textvariable = Channel_Name_Var)
Channel_Name_Label.pack()

def channel_name(event=None):
    url = Url_Textbox.get("1.0", "end-1c")
    if url.startswith("https://www.youtube.com/watch?v=" or "https://youtu.be/" or "https://www.youtube.com/shorts/"):
        try:
            link = yt.YouTube(url)
            channel = link.author
            Channel_Name_Var.set("Channel: " + channel)
        except:
            Channel_Name_Var.set("Error fetching channel")
    else:
        Channel_Name_Var.set("Error fetching channel")

#Retrieve Video Length
Video_Length_Var = ctk.StringVar()
Video_Length_Var.set("Video Length: ")
Video_Length_Label = ctk.CTkLabel(Window,textvariable = Video_Length_Var)
Video_Length_Label.pack()

def video_length(event=None):
    url = Url_Textbox.get("1.0", "end-1c")
    if url.startswith("https://www.youtube.com/watch?v=" or "https://youtu.be/" or "https://www.youtube.com/shorts/"):
        try:
            link = yt.YouTube(url)
            vid_len = link.length
            
            minutes = vid_len // 60
            seconds = vid_len % 60
            
            formatted_vid_len = f"{minutes:02}:{seconds:02}"
            Video_Length_Var.set(f"Video Length: {formatted_vid_len}")
        except:
            Video_Length_Var.set("Error fetching video")
    else:
        Video_Length_Var.set("Error fetching video")

#Update Title Function Bind
Url_Textbox.bind("<KeyRelease>", update_title)

#Creator Function Bind
Url_Textbox.bind("<KeyRelease>", channel_name)

#Video Length Function Bind
Url_Textbox.bind("<KeyRelease>", video_length)


Window.mainloop()