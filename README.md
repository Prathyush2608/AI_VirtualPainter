# 🎨 AI Virtual Painter

A real-time gesture-based drawing application that allows users to draw on the screen using hand movements captured via a webcam. This project uses computer vision to create a touchless and interactive drawing experience.

---

## 🚀 Features

- ✋ Real-time hand tracking using MediaPipe  
- ☝️ Draw using index finger  
- ✌️ Selection mode for choosing colors  
- 🎨 Multiple drawing colors  
- 🧹 Eraser functionality  
- 🧽 Clear canvas using hand gesture  
- 💾 Save drawing using keyboard  
- ⚡ Smooth and responsive performance  

---

## 🧠 How It Works

1. Webcam captures live video  
2. MediaPipe detects hand landmarks (21 points)  
3. Finger positions are analyzed to detect gestures  
4. Based on gestures:
   - Draw on canvas  
   - Select colors  
   - Clear screen  
5. OpenCV renders the final output  

---

## 🛠️ Tech Stack

- **Python 3.11.9**
- **OpenCV (cv2)** – Video processing & drawing
- **MediaPipe 0.10.11** – Hand tracking
- **NumPy** – Canvas handling
- **OS & Time Modules** – File handling & gesture control

---

## 📁 Project Structure
