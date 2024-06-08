import asyncio
import websockets

async def send_audio_for_transcription(audio_bytes):
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to WebSocket server")
            # Send the audio bytes
            await websocket.send(audio_bytes)
            print("Audio data sent to server")

            # Receive the transcription
            transcript = await websocket.recv()
            print("Received transcription from server")
            return transcript
    except websockets.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
