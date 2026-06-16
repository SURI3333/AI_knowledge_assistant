import React, { useState } from "react";
import API from "../services/api";
import { motion } from "framer-motion";


function Upload() {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await API.post("/documents/upload", formData);

    setMsg(res.data.message);
  };

  return (
    <motion.div
      className="upload"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      <h2>Upload Document</h2>

      <input onChange={(e) => setFile(e.target.files[0])} type="file" />
      <button onClick={handleUpload}>Upload</button>

      <p>{msg}</p>
    </motion.div>
  );
}

export default Upload;