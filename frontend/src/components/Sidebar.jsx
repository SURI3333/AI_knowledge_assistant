import React from "react";

function Sidebar({ setPage }) {
  return (
    <div className="sidebar">
      <h2>AI Assistant</h2>

      <button onClick={() => setPage("chat")}>💬 Chat</button>
      <button onClick={() => setPage("upload")}>📁 Upload</button>
    </div>
  );
}

export default Sidebar;