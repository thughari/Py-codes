from moviepy.editor import VideoFileClip, AudioFileClip

def merge_audio_and_video(video_path, audio_path, output_path):
    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Load audio clip
    audio_clip = AudioFileClip(audio_path)

    # Set video clip's audio to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)

    # Write the merged video with audio to a file
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)

if __name__ == "__main__":
    # Replace these paths with your video, audio, and desired output paths
    video_path = r"C:\Users\harib\Documents\Udemy downloader\udemy-downloader\out_dir\tableau-data-visualization-starttech\02 - Installation and getting started\002 About the data.encrypted.mp4"
    audio_path = r"C:\Users\harib\Documents\Udemy downloader\udemy-downloader\out_dir\tableau-data-visualization-starttech\02 - Installation and getting started\002 About the data.encrypted.m4a"
    output_path = r"C:\Users\harib\Documents\Udemy downloader\udemy-downloader\out_dir\tableau-data-visualization-starttech\02 - Installation and getting started\002 About the data.mp4"

    merge_audio_and_video(video_path, audio_path, output_path)
