# hand-sign
A repository for hand gesture recognition and data collection scripts using OpenCV and a pre-trained model for real-time classification.
# Hand Gesture Recognition and Data Collection

This project consists of two Python scripts for collecting hand gesture images and testing a pre-trained model using OpenCV and cvzone libraries.

## Overview

This repository includes two main scripts:

1. `dataCollection.py`: Run this script to collect hand gesture images for training. It allows you to label and save images in different folders corresponding to different gestures or words.

2. `test.py`: After collecting and training a model using an external service, you can run this script to test the trained model in real-time.

## Usage

### Step 1: Data Collection (dataCollection.py)

1. Run the `dataCollection.py` script. This script captures hand gestures using your camera.

2. While the script is running, press the keys 'a', 'b', or 'c' to label and save images in the respective folders ('A', 'B', or 'C').

3. Repeat this process to create a dataset for training.

### Step 2: Train the Model on Teachable Machine

1. Visit [Teachable Machine](https://teachablemachine.withgoogle.com/train) in your web browser.

2. Follow the instructions on Teachable Machine to train your model using the dataset you collected. Make sure to choose 'Image Project' and label the classes as 'A,' 'B,' and 'C.'

3. After the training is complete, you can test the model on the Teachable Machine website to ensure it performs well.

4. Once you are satisfied with the model's performance, proceed to the next step.

### Step 3: Download the Trained Model

1. Download the trained model from Teachable Machine.

2. Save the downloaded model file in the 'Model' folder of this repository.

### Step 4: Test the Model (test.py)

1. Run the `test.py` script. This script captures real-time hand gestures using your camera.

2. The script will use the pre-trained model located in the 'Model' directory to classify the gestures as 'A,' 'B,' or 'C.'

3. The classification result will be displayed on the screen.

## Requirements

- Python 3.x
- OpenCV
- cvzone library

## Contributing

Contributions are welcome. You can open issues and pull requests to improve the project.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify the README content further or customize it as needed. Be sure to provide detailed information on each step to help users understand how to use your project effectively.
