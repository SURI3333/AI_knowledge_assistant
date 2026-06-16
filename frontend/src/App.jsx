import React, { useState } from "react";
import Chat from "./components/Chat.jsx";
import Upload from "./components/Upload.jsx";
import Sidebar from "./components/Sidebar.jsx";
import "./App.css";

function App() {
  const [page, setPage] = useState("chat");

  return (
    <div className="app">
      <Sidebar setPage={setPage} />

      <div className="main">
        {page === "chat" && <Chat />}
        {page === "upload" && <Upload />}
      </div>
    </div>
  );
}

export default App;
