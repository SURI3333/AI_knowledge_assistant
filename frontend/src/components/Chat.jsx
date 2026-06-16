import React, { useState } from "react";
import API from "../services/api";

function Chat() {
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!question.trim()) return;

    // ✅ add user message first
    const newMessages = [
      ...messages,
      { type: "user", text: question }
    ];
    setMessages(newMessages);

    setLoading(true);

    try {
      const res = await API.post("/chat/ask", {
        question: question,
      });

      console.log("API RESPONSE:", res.data);  // ✅ DEBUG

      const botMsg = {
        type: "bot",
        text: res.data.answer || "⚠️ No response from backend",
      };

      // ✅ IMPORTANT FIX: use newMessages
      setMessages([...newMessages, botMsg]);

    } catch (err) {
      console.error("ERROR:", err);

      setMessages([
        ...newMessages,
        { type: "bot", text: "❌ Backend error" }
      ]);
    }

    setQuestion("");
    setLoading(false);
  };

  return (
    <div style={{ padding: "20px" }}>

      {/* ✅ Chat Messages */}
      <div style={{ minHeight: "300px" }}>
        {messages.map((msg, i) => (
          <div key={i}
            style={{
              textAlign: msg.type === "user" ? "right" : "left",
              margin: "10px"
            }}>
            <b>{msg.type === "user" ? "You:" : "Bot:"}</b> {msg.text}
          </div>
        ))}

        {loading && <div>Bot is typing...</div>}
      </div>

      {/* ✅ Input */}
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
        style={{ padding: "10px", width: "250px" }}
      />

      <button onClick={sendMessage} style={{ marginLeft: "10px" }}>
        Send
      </button>

    </div>
  );
}

export default Chat;