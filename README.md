# 🚗 Smart Car Parking Detection System

A real-time, computer vision-based web application designed to automatically detect and monitor available parking spaces from video feeds or camera streams. 

Built with **Python, OpenCV, and Flask-SocketIO**, this system accurately identifies occupied and vacant parking spots by analyzing the pixel density within predefined parking regions. It features a modern, responsive web interface that allows users to upload video footage and monitor parking lot capacity in real time.

---

## ✨ Key Features
- **Real-Time Detection:** Processes video frames continuously to detect the occupancy status of every parking space.
- **Live WebSocket Streaming:** Streams processed video frames and live statistics directly to the web dashboard with minimal latency using Socket.IO.
- **Space Mapping Tool:** Includes a companion script (`ParkingSpacePicker.py`) to easily click and map out bounding boxes for parking spaces on any static image of a lot.
- **Dynamic Dashboard:** A beautifully designed frontend that displays live metrics (Total Spaces, Free, Occupied) and visual indicators (Green = Free, Red = Occupied).

## 🛠️ Technology Stack
- **Backend:** Python, Flask, Flask-SocketIO, Eventlet
- **Computer Vision:** OpenCV (`cv2`), `cvzone`, NumPy
- **Frontend:** HTML5, CSS3, Vanilla JavaScript, Socket.IO Client

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/car-parking-detection.git
   cd car-parking-detection
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python3 run.py
   ```

5. **Access the Web Interface:**
   Open your browser and navigate to: `http://localhost:5000`

---

## 🎯 How to Use

1. **Map Your Parking Spaces (Optional/Setup phase):**
   Run `python3 ParkingSpacePicker.py` to open a static image of your parking lot (`carParkImg.png`). 
   - Left-click to draw boxes over parking spaces.
   - Right-click inside a box to delete it.
   - This automatically generates a `CarParkPos` coordinate file.

2. **Start Monitoring:**
   - On the web interface, click **Choose Video File** and upload your parking lot footage (e.g. `carPark.mp4`).
   - The system will immediately begin processing the video, highlighting free spaces in green and occupied spaces in red.
   - Keep track of overall availability via the dynamic live counters.

---

## 📸 Screenshots

*(You can add screenshots of your application here after pushing to GitHub. For example:)*
- `![Dashboard](docs/dashboard.png)`
- `![Live Detection](docs/detection.png)`

---

## 🧠 How it Works (Under the Hood)
For a detailed look at the system architecture, backend streaming logic, and image processing pipeline, please check out the [Architecture Documentation](ARCHITECTURE.md).

---

## 📄 License
This project is open-source and available under the MIT License.
