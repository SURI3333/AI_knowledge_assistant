import React from "react";
import { motion } from "framer-motion";
import "./Dashboard.css";

function Dashboard() {
  const stats = [
    { title: "Documents", value: 12 },
    { title: "Questions Asked", value: 45 },
    { title: "Active Users", value: 5 },
  ];

  const recent = [
    "What is leave policy?",
    "Explain onboarding process",
    "Notice period details",
  ];

  return (
    <div className="dashboard">

      {/* ✅ Header */}
      <h1 className="title">📊 Dashboard</h1>

      {/* ✅ Stats Cards */}
      <div className="cards">
        {stats.map((item, index) => (
          <motion.div
            key={index}
            className="card"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.2 }}
          >
            <h3>{item.title}</h3>
            <h2>{item.value}</h2>
          </motion.div>
        ))}
      </div>

      {/* ✅ Recent Activity */}
      <motion.div
        className="recent"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
      >
        <h2>Recent Questions</h2>

        {recent.map((q, i) => (
          <div key={i} className="recent-item">
            {q}
          </div>
        ))}
      </motion.div>

    </div>
  );
}

export default Dashboard;