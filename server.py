import asyncio
import websockets
import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Ensure you have set your OpenAI API key in your environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

async def transcribe(websocket, path):
    try:
        async for message in websocket:
            print("Received audio data")
            # Save the received audio bytes to a file
            file_path = "received_audio.mp3"
            with open(file_path, "wb") as f:
                f.write(message)

            # Transcribe the audio using OpenAI's Whisper API
            with open(file_path, "rb") as audio_file:
                try:
                    response = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file
                    )
                    print("Transcription successful")
                    # Send the transcription back to the client
                    await websocket.send(response.text)
                except Exception as e:
                    print(f"Error during transcription: {e}")
                    await websocket.send(f"Error during transcription: {e}")
    except websockets.ConnectionClosed:
        print("Connection closed by client")

# Start the WebSocket server
async def main():
    async with websockets.serve(transcribe, "localhost", 8765, max_size=10**8):  # Set max_size to 100 MB
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user")
