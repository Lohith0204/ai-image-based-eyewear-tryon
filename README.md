# AI Image-Based Virtual Eyewear Try-On

## Live Demo
Try out the deployed application here:

🚀 **Streamlit App** → https://ai-image-based-eyewear-tryon.streamlit.app/

## Overview
AI Image-Based Virtual Eyewear Try-On is a Python-based computer vision application that allows users to virtually try on sunglasses using a single image. The system detects the user’s face and eyes, calculates accurate positioning, and overlays eyewear naturally onto the face.

The project focuses on building a simple, modular, and beginner-friendly pipeline using classical computer vision techniques without training custom deep learning models.

## Features
- Upload a single image for virtual try-on
- Face and eye detection using OpenCV
- Accurate eyewear positioning based on eye distance
- Transparent PNG overlay support
- Real-time preview via Streamlit UI
- Modular and extensible project structure
- Beginner-friendly implementation

## Tech Stack
- Python
- Streamlit
- mediapipe
- Pillow
- OpenCV
- NumPy

## Project Structure

```text
AI IMAGE-BASED VIRTUAL EYEWEAR TRY-ON/
│
├── app.py                   # Streamlit application entry point
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
├── gitignore.txt            # Ignore files
│
├── ai_engine/
│   ├── face_detection.py    # Face and eye detection logic
│   └── overlay.py           # Glasses positioning and overlay logic
│   
│
├── assets/
│   ├── PASSPORT SIZE PHOTO.jpg   # Sample input image
│   └── sunglasses.png            # Transparent eyewear asset
│
└── screenshots/             # Application screenshots

```

## Screenshots

### Application Interface
![Application Interface](<screenshots/Screenshot 2025-12-27 171538.png>)

### Images Input
![Images Input](<screenshots/Screenshot 2025-12-27 171622.png>)

### Try-On Image Output
![Tryon Output](<screenshots/Screenshot 2025-12-27 171702.png>)


## How It Works
1. The user uploads an image through the Streamlit interface.
2. The system detects the face and eyes using Haar Cascade classifiers.
3. The distance between the eyes is calculated to determine correct scaling.
4. Sunglasses are resized and positioned based on eye coordinates.
5. The eyewear image is blended onto the face using alpha transparency.
6. The final try-on image is displayed instantly.

## Installation & Setup
1. Open your IDE (VS Code is recommended).
2. Clone or download the project files to your local system.
3. Create a virtual environment to avoid dependency conflicts:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt
5. Run the application:
    streamlit run app.py

## Usage
This application can be used to virtually try on eyewear using a single image. Users upload a photo, and the system automatically detects facial features and overlays sunglasses in a realistic position. This can be useful for e-commerce previews, computer vision demos, and learning face-based image processing concepts.

## Future Improvements
Support for multiple eyewear styles
Automatic face alignment and rotation handling
Deep learning–based face landmark detection
Support for live webcam try-on
UI enhancements and styling options

## Learning Outcomes
This project helped me understand how image-based virtual try-on systems work in real-world applications.
I learned how to detect facial features, calculate geometric relationships between eyes, and overlay transparent assets accurately. The project strengthened my skills in OpenCV, Python modular design, and Streamlit-based UI development, while building a solid foundation for advanced AR and AI applications.
