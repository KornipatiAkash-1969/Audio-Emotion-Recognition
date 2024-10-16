Audio Emotion Recognition


Description
This project aims to recognize emotions from audio inputs using deep learning techniques. It employs the TESS Toronto emotional speech set dataset and utilizes libraries such as TensorFlow and librosa for audio processing and model training. The application features a user-friendly GUI built with Tkinter, allowing users to upload audio files and receive emotion predictions.


Required Libraries
To run this project, you need to install the following Python libraries:
librosa: For audio analysis and feature extraction.
numpy: For numerical operations.
scikit-learn: For machine learning utilities, including model evaluation and data preprocessing.
tensorflow: For building and training the deep learning model.
keras: For creating the neural network model.
tkinter: For the graphical user interface.
pydub: For handling audio files.
sounddevice: For playing audio files.
PIL (Pillow): For image processing and displaying emojis.


You can install these libraries using pip:
pip install librosa numpy scikit-learn tensorflow keras tkinter pydub sounddevice pillow


Dataset
The project uses the TESS Toronto emotional speech set dataset, which contains various emotional speech recordings. Ensure that the dataset is properly organized in the specified directory.


Usage Instructions
Set Up Environment:
Ensure you have Python installed (preferably Python 3.6 or later).
Install the required libraries as mentioned above.

Download Dataset:
Download the TESS dataset and extract it to the designated directory. Update the folder path in the code to point to the dataset location.

Run the Application:
Run the audio_emotion_recognition.py script to start the application:
python audio_emotion_recognition.py
The application will display the home page with options to predict emotions from audio files or view prediction history.

Upload Audio File:
Click on the "Audio Prediction" button to upload a .wav audio file.
The predicted emotion will be displayed along with an emoji representing the emotion.

View Prediction History:
Click on the "Prediction History" button to view previously processed audio files and their corresponding predicted emotions.

About The App:
Click on the "About The App" button for more information about the software.

Note
Ensure all audio files you want to test with are in the .wav format.