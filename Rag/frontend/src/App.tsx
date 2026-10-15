import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  
  // Connects to your FastAPI endpoint (e.g. http://127.0.0.1:8000/query/)
  const backendUrl = import.meta.env.VITE_BACKEND_URL || "http://127.0.0.1:8000/query/";

  const askQuestion = async () => {
    if (!question.trim() || loading) return;

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch(
        `${backendUrl}?question=${encodeURIComponent(question)}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        throw new Error(errData.detail || "Server error occurred.");
      }

      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      console.error(error);
      const errorMessage = error instanceof Error ? error.message : "Failed to fetch response.";
      setAnswer(`Error: ${errorMessage}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="header-badge">First RAG Application</div>

      <h1>Document Q&amp;A Assistant</h1>

      <p className="description">
        Querying knowledge from <code>sample.pdf</code> powered by{" "}
        <strong>FastAPI</strong> &amp; <strong>Google Gemini API</strong>.
      </p>

      <div className="input-section">
        <input
          type="text"
          placeholder="Ask a question about sample.pdf..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") askQuestion();
          }}
        />

        <button onClick={askQuestion} disabled={loading}>
          {loading ? "Thinking..." : "Ask"}
        </button>
      </div>

      {answer && (
        <div className="answer">
          <h2>Answer</h2>
          <p>{answer}</p>
        </div>
      )}

      <div className="tech-stack-footer">
        <span>FastAPI</span>
        <span>•</span>
        <span>sample.pdf</span>
        <span>•</span>
        <span>Google Gemini API</span>
      </div>
    </div>
  );
}

export default App;