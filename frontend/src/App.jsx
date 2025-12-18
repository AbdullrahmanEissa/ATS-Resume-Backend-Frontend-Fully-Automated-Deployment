import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import AnalyzeResult from "./components/AnalyzeResult";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="App">
      <h1>ATS CV Scanner</h1>
      <UploadForm setResult={setResult} />
      {result && <AnalyzeResult result={result} />}
    </div>
  );
}

export default App;

