import React, { useState } from "react";
import axios from "axios";

function UploadForm({ setResult }) {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");

  const handleUpload = async () => {
    if (!file || !jobDesc) return alert("Upload file and enter job description");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const uploadRes = await axios.post("http://127.0.0.1:8000/upload-cv", formData);
      const fileId = uploadRes.data.file_id;

      const analyzeRes = await axios.post("http://127.0.0.1:8000/analyze", {
        file_id: fileId,
        job_description: jobDesc
      });

      setResult(analyzeRes.data);
    } catch (err) {
      console.error(err);
      alert("Error uploading or analyzing CV");
    }
  };

  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <textarea
        placeholder="Job description..."
        value={jobDesc}
        onChange={(e) => setJobDesc(e.target.value)}
      />
      <button onClick={handleUpload}>Upload & Analyze</button>
    </div>
  );
}

export default UploadForm;

