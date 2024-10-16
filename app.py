import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class EmotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Prediction App",)

        title_font = ("Helvetica", 18)  
        
        self.root.option_add("*Font", title_font)
        
        self.root.configure(bg='grey')
        
        self.emotion_to_emoji = {
            "HAPPY": r"C:/Users/akash/Downloads/Speech_Emotion_Recognition/Emotion Emojis/happy.png",
            "SAD": r"C:/Users/akash/Downloads/Speech_Emotion_Recognition/Emotion Emojis/sad.png",
            "ANGRY": r"C:/Users/akash/Downloads/Speech_Emotion_Recognition/Emotion Emojis/angry.png",
            "SURPRISED": r"C:/Users/akash/Downloads/Speech_Emotion_Recognition/Emotion Emojis/surprised.png",
            "NEUTRAL": r"C:/Users/akash/Downloads/Speech_Emotion_Recognition/Emotion Emojis/neutral.png",
            "FEAR": r"C:/Users/akash/Downloads/Speech_Emotion_Recognition/Emotion Emojis/fear.png",
            "DISGUST": r"C:/Users/akash/Downloads/Speech_Emotion_Recognition/Emotion Emojis/disgust.png"
        }
        
        self.emoji_image = None  
        self.prediction_history = []  
        
        self.show_home_page()
        
    def show_home_page(self):
        self.clear_window()
        
        label = tk.Label(self.root, text=" Emotion Prediction App ", font=('Helvetica bold', 20))
        label.pack(pady=20)
        
        button = tk.Button(self.root, text="Audio Prediction", command=self.show_audio_page, bg='orange')
        button.pack()
        
        button_history = tk.Button(self.root, text="Prediction History", command=self.show_history_page, bg='lightgreen')
        button_history.pack(pady=10)
        
        about_button = tk.Button(self.root, text="About The App", command=self.show_about_page, bg='lightblue')
        about_button.pack(pady=10)
        
    def show_audio_page(self):
        self.clear_window()
        
        canvas = tk.Canvas(self.root, width=500, height=500, bg='skyblue')
        canvas.pack()
        
        label1 = tk.Label(self.root, text='SPEECH EMOTION', font=('Helvetica bold', 26))
        canvas.create_window(250, 50, window=label1)
        
        def upload_audio():
            file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
            if file_path:
                predicted_emotion = predict_emotion(file_path)
                label2.config(text=predicted_emotion)
                
                self.prediction_history.append((os.path.basename(file_path), predicted_emotion))
                
                emoji_image_path = self.emotion_to_emoji.get(predicted_emotion)
                if emoji_image_path:
                    emoji_image = Image.open(emoji_image_path)
                    emoji_image = emoji_image.resize((100, 100), Image.LANCZOS)
                    self.emoji_image = ImageTk.PhotoImage(emoji_image)
                    emoji_label.config(image=self.emoji_image)
                
        button1 = tk.Button(self.root, text='Upload Audio', command=upload_audio, bg='orange')
        canvas.create_window(250, 150, window=button1)
        
        label2 = tk.Label(self.root, text='Predicted Emotion Will Be Displayed Here')
        canvas.create_window(250, 200, window=label2)
        
        emoji_label = tk.Label(self.root, image=None)
        canvas.create_window(250, 300, window=emoji_label)
        
        back_button = tk.Button(self.root, text="Back to Home", command=self.show_home_page)
        canvas.create_window(250, 400, window=back_button)
        
    def show_history_page(self):
        self.clear_window()
        
        canvas = tk.Canvas(self.root, width=500, height=500, bg='lightgreen')
        canvas.pack()
        
        label = tk.Label(self.root, text="Prediction History", font=('Helvetica bold', 16))
        canvas.create_window(250, 50, window=label)
        
        if self.prediction_history:
            for index, (file_name, predicted_emotion) in enumerate(self.prediction_history, start=1):
                history_text = f"{index}. File: {file_name}, Emotion: {predicted_emotion}"
                history_label = tk.Label(self.root, text=history_text)
                canvas.create_window(250, 100 + index * 30, window=history_label)
        else:
            no_history_label = tk.Label(self.root, text="No prediction history available.")
            canvas.create_window(250, 150, window=no_history_label)
        
        back_button = tk.Button(self.root, text="Back to Home", command=self.show_home_page)
        canvas.create_window(250, 450, window=back_button)
        
    def show_about_page(self):
        self.clear_window()
        
        canvas = tk.Canvas(self.root, width=500, height=500, bg='skyblue')
        canvas.pack()
        
        label = tk.Label(self.root, text="About The Software", font=('Helvetica bold', 16))
        canvas.create_window(250, 50, window=label)
        
        about_text = ("Hello Everyone !! "
                      " Speech Emotion Recognition is a software that recognizes the emotion of the user."
                      " All of the audio files in this software should be inputted with '.wav' extension."
                      " A special thanks to the University of Toronto for the TESS data set and to all of my guiders"
                      " at clevered that guided me throughout the journey of making this software.")
        
        about_label = tk.Label(self.root, text=about_text, wraplength=400)
        canvas.create_window(250, 150, window=about_label)
        
        back_button = tk.Button(self.root, text="Back to Home", command=self.show_home_page)
        canvas.create_window(250, 400, window=back_button)
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionApp(root)
    root.mainloop()
