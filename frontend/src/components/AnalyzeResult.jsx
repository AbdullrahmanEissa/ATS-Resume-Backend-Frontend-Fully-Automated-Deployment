import React from "react";

function AnalyzeResult({ result }) {
  return (
    <div>
      <h2>Result</h2>
      <p><strong>Filename:</strong> {result.filename}</p>
      <p><strong>Score:</strong> {result.score}%</p>
      <p><strong>Matched Keywords:</strong> {result.matched_keywords.join(", ")}</p>
      <p><strong>Preview:</strong> {result.extracted_text_preview}</p>
    </div>
  );
}

export default AnalyzeResult;

