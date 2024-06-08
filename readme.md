Real-time Transcription with OpenAI Whisper

This project provides a real-time transcription service using OpenAI's Whisper API. The system consists of a WebSocket server to handle audio data and a Streamlit application for the user interface.

Prerequisites:
- Python 3.11 or later
- pip (Python package installer)
- OpenAI API key

Installation:
1. Clone the repository:
   git clone https://github.com/your-username/live-transcribe-backend.git
   cd live-transcribe-backend

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
   pip install -r requirements.txt

4. Set up environment variables:
   Create a .env file in the project root and add your OpenAI API key:
   OPENAI_API_KEY=your_openai_api_key_here

Running the Servers:
Step 1: Start the WebSocket Server
1. Navigate to the project directory:
   cd /path/to/live-transcribe-backend

2. Activate the virtual environment:
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Run the WebSocket server:
   python server.py

Step 2: Start the Streamlit Application
1. Open a new terminal window and navigate to the project directory:
   cd /path/to/live-transcribe-backend

2. Activate the virtual environment:
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Run the Streamlit application:
   streamlit run app.py

4. Access the application:
   Open your web browser and navigate to http://localhost:8501

Usage:
1. Click the "Click to record" button to start recording your audio.
2. Speak clearly into your microphone.
3. The recorded audio will be sent to the server for transcription.
4. The transcribed text will be displayed in the application.

Troubleshooting:
- Ensure that your OpenAI API key is correctly set in the .env file.
- Make sure the WebSocket server is running before starting the Streamlit application.
- If you encounter issues with the audio recorder component, try resizing the browser window or refreshing the page.

