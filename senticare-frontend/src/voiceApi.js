// voiceApi.js

const BASE_URL = "http://localhost:5000";

export async function sendVoiceIntro(audioBlob, ext = "webm", sessionId, lang = "en") {
  const formData = new FormData();

  formData.append("audio",      audioBlob, `recording.${ext}`);
  formData.append("session_id", sessionId || "");
  formData.append("lang",       lang      || "en");

  const response = await fetch(`${BASE_URL}/voice-intro`, {               //sends audio to backend
    method: "POST",
    body:   formData,                   //bcz audio can't be sent as json , voice uses FormData
  });

  if (!response.ok) {
    let detail = `HTTP ${response.status}`;           //HTTP 500
    try {
      const err = await response.json();             
      detail = err.error || JSON.stringify(err);                //like Audio not detected
    } catch (_) { /* ignore */ }
    throw new Error(`Voice intro failed: ${detail}`);
  }

  const data = await response.json();              //anxious
  if (data.error) throw new Error(data.error);     //error like STT failed
  return data;
}

//Send a chat message to /chat.
//chat uses JSON  

export async function sendChatMessage({ sessionId, input, lang, policyMode = "default" }) {
  const response = await fetch(`${BASE_URL}/chat`,            //Calls backend API   like POST /chat
    {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      session_id:  sessionId,
      input,
      lang,
      policy_mode: policyMode,    // defines how an AI chatbot behaves whether safe,supportive,clinical but here is therpay by default
    }),
  });

  if (!response.ok) throw new Error(`Chat request failed: HTTP ${response.status}`);
  return response.json();
}