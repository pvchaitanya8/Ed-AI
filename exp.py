import streamlit as st
import streamlit.components.v1 as components

# Title

# HTML, CSS, and JavaScript code for live video, audio input, device selection, and live subtitles
html_code = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Mock Interview</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #242424;
        margin: 0;
        padding: 0;
      }
      #container {
        display: flex;
        justify-content: space-between;
        padding: 20px;
      }
      #videoColumn, #transcriptionColumn {
        flex: 1;
        margin: 0 20px;
      }
      #videoColumn {
        text-align: center;
      }
      select {
        margin-bottom: 10px;
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        border: 1px solid #ccc;
      }
      video {
        width: 100%;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      }
      #transcription {
        background-color: black;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        font-size: 18px;
        color: #9a8dfc;
        height: 300px;
        overflow-y: auto;
      }
      #subtitles {
        background-color: #7367cf;
        color: #beb5ff;
        font-size: 15px;
        padding: 10px;
        text-align: center;
        margin-top: 20px;
        border-radius: 1px;
      }
    </style>
  </head>
  <body>
    <div id="subtitles"></div>
    <div id="container">
      <!-- Left column: Video feed and device selection -->
      <div id="videoColumn">
        <div id="transcription">Transcription history will appear here...</div>
        <p id="status"></p>
        <select id="audioSource"></select>
        <select id="videoSource"></select>
      </div>

      <!-- Right column: Transcription history -->
      <div id="transcriptionColumn">
        <video id="video" autoplay muted></video>
      </div>
    </div>

    <script>
      const video = document.getElementById('video');
      const audioSelect = document.getElementById('audioSource');
      const videoSelect = document.getElementById('videoSource');
      const transcriptionDiv = document.getElementById('transcription');
      const subtitles = document.getElementById('subtitles');
      const status = document.getElementById('status');

      if (!('SpeechRecognition' in window || 'webkitSpeechRecognition' in window)) {
        status.textContent = 'Web Speech API is not supported in this browser. Try using Chrome.';
      }

      const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
      recognition.lang = 'en-US';
      recognition.continuous = true;
      recognition.interimResults = true;

      navigator.mediaDevices.enumerateDevices()
        .then(deviceInfos => {
          deviceInfos.forEach(deviceInfo => {
            const option = document.createElement('option');
            option.value = deviceInfo.deviceId;
            if (deviceInfo.kind === 'audioinput') {
              option.text = deviceInfo.label || `Microphone ${audioSelect.length + 1}`;
              audioSelect.appendChild(option);
            } else if (deviceInfo.kind === 'videoinput') {
              option.text = deviceInfo.label || `Camera ${videoSelect.length + 1}`;
              videoSelect.appendChild(option);
            }
          });
        })
        .catch(error => {
          console.error('Error listing devices:', error);
          status.textContent = 'Error accessing devices.';
        });

      function getStream() {
        if (window.stream) {
          window.stream.getTracks().forEach(track => track.stop());
        }
        const audioSource = audioSelect.value;
        const videoSource = videoSelect.value;
        const constraints = {
          audio: { deviceId: audioSource ? { exact: audioSource } : undefined },
          video: { deviceId: videoSource ? { exact: videoSource } : undefined }
        };
        navigator.mediaDevices.getUserMedia(constraints)
          .then(stream => {
            window.stream = stream;
            video.srcObject = stream;
          })
          .catch(error => {
            console.error('Error accessing media devices:', error);
            status.textContent = 'Error accessing media devices. Please allow camera and microphone access.';
          });
      }

      audioSelect.onchange = getStream;
      videoSelect.onchange = getStream;

      getStream();

      recognition.onresult = event => {
        let transcriptText = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
          transcriptText += event.results[i][0].transcript + ' ';
        }
        transcriptionDiv.textContent = transcriptText;
        subtitles.textContent = event.results[event.resultIndex][0].transcript;
      };

      recognition.onerror = event => {
        console.error('Speech Recognition error:', event.error);
        status.textContent = 'Speech recognition error: ' + event.error;
      };

      recognition.start();
    </script>
  </body>
</html>
"""

# Render the HTML, JavaScript, and CSS using Streamlit components
components.html(html_code, height=600)
