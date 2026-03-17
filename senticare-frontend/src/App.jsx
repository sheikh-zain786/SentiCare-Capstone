import React, { useState } from "react";

const API_URL = "http://localhost:5000/chat";

function App() {

  const [sessionId] = useState(() => crypto.randomUUID());

  const [messages, setMessages] = useState([]);

  const [input, setInput] = useState("");

  const [questions, setQuestions] = useState(null);


  const sendMessage = async (payload) => {

    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        session_id: sessionId,
        input: payload
      })
    });

    const data = await res.json();

    handleResponse(data);
  };


  const handleResponse = (data) => {

    if (data.stage === "features") {

      setQuestions(data.questions);

      setMessages(prev => [
        ...prev,
        { sender: "bot", text: "Please answer the following questions." }
      ]);

    }

    else if (data.stage === "therapy") {

      const therapy = data.therapy;

      setMessages(prev => [
        ...prev,
        { sender: "bot", text: therapy.validation },
        { sender: "bot", text: therapy.grounding_statement },
        { sender: "bot", text: therapy.next_question }
      ]);

    }

    else if (data.message) {

      setMessages(prev => [
        ...prev,
        { sender: "bot", text: data.message }
      ]);

    }
  };


  const handleSubmit = (e) => {

    e.preventDefault();

    if (!input.trim()) return;

    setMessages(prev => [
      ...prev,
      { sender: "user", text: input }
    ]);

    sendMessage(input);

    setInput("");
  };


  return (

    <div style={{ maxWidth: "600px", margin: "40px auto", fontFamily: "Arial" }}>

      <h2>SentiCare</h2>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "15px",
          height: "400px",
          overflowY: "auto",
          marginBottom: "10px"
        }}
      >

        {messages.map((msg, i) => (
          <div key={i} style={{
            textAlign: msg.sender === "user" ? "right" : "left",
            margin: "8px 0"
          }}>
            <b>{msg.sender === "user" ? "You" : "Bot"}:</b> {msg.text}
          </div>
        ))}

      </div>


      <form onSubmit={handleSubmit}>

        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{
            width: "80%",
            padding: "10px"
          }}
        />

        <button
          type="submit"
          style={{
            padding: "10px 15px",
            marginLeft: "5px"
          }}
        >
          Send
        </button>

      </form>

    </div>
  );
}

export default App;