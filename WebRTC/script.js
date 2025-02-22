async function init() {
  try {
    const tokenResponse = await fetch("http://localhost:3000/session");
    const data = await tokenResponse.json();
    const EPHEMERAL_KEY = data.client_secret.value;

    if (!EPHEMERAL_KEY) {
      throw new Error("Failed to get ephemeral key");
    }

    const pc = new RTCPeerConnection();

    const audioEl = document.createElement("audio");
    audioEl.autoplay = true;
    document.body.appendChild(audioEl);

    pc.ontrack = e => {
      audioEl.srcObject = e.streams[0];
    };

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    pc.addTrack(stream.getTracks()[0]);

    const dc = pc.createDataChannel("oai-events");
    dc.addEventListener("message", (e) => {
      console.log("Received message:", e.data);
    });


    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);

    const baseUrl = "https://api.openai.com/v1/realtime";
    const model = "gpt-4o-realtime-preview-2024-12-17";
    const sdpResponse = await fetch(`${baseUrl}?model=${model}`, {
      method: "POST",
      body: offer.sdp,
      headers: {
        Authorization: `Bearer ${EPHEMERAL_KEY}`,
        "Content-Type": "application/sdp"
      },
    });

    const answer = {
      type: "answer",
      sdp: await sdpResponse.text(),
    };

    await pc.setRemoteDescription(answer);

    console.log("WebRTC connection established");

    setTimeout(() => {
      const message = {
        type: "response.create",
        response: {
          modalities: ["text"],
          instructions: "プログラミングに関する面白いジョークを言って",
        },
      };
      dc.send(JSON.stringify(message));
      console.log("Sent message:", message);
    }, 2000);
  } catch (error) {
    console.error("Error in WebRTC connection:", error);
  }
}

init();
