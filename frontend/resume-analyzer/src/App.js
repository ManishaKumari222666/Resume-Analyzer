import { useState } from "react";
import "./App.css";

function App() {

  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");

  const uploadResume = async () => {

    const formData = new FormData();

    formData.append("file", file);

    const res = await fetch(
      "http://127.0.0.1:8000/analyze-resume",
      {
        method: "POST",
        body: formData,
      }
    );

    const data = await res.json();

    setResponse(data.analysis);
  };

  return (
    <div className="container">

      <h1  className="title">Python Resume Analyzer</h1>

      <input
        type="file"
        accept=".pdf"
        className="file-input"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button className="ai-button" onClick={uploadResume}>
        Analyze Resume
      </button>

      <div style={{ marginTop: "30px" }}>
        <h3>Analysis:</h3>

        <pre>{response}</pre>
      </div>

    </div>
  );
}

export default App;