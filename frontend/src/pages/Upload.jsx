import { useState } from "react";
import api from "../services/api";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");
  const [docs, setDocs] = useState([]);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setStatus("Uploading...");

    try {
      const res = await api.post("/api/documents/upload", formData, {
  headers: { "Content-Type": "multipart/form-data" },
    });

      setStatus("Upload complete!");
      setDocs((prev) => [res.data, ...prev]);
    } catch (err) {
      setStatus("Upload failed.");
      console.error(err);
    }
  };

  return (

    <div className="max-w-2xl mx-auto mt-12 space-y-6 px-4">
      <h2 className="text-3xl font-bold text-gray-800">Upload Document</h2>

      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none"
      />

      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition"
      >
        Upload
      </button>

      <p className="text-sm text-gray-500">{status}</p>

      <hr className="my-6 border-gray-300" />

      <h3 className="text-xl font-semibold text-gray-800">Uploaded Files</h3>

      <ul className="space-y-3">
        {docs.map((doc) => (
          <li key={doc.id} className="p-4 border border-gray-300 rounded-lg shadow-sm bg-white">
            <p className="font-semibold text-gray-800">{doc.file_name}</p>
            <p className="text-gray-600">Status: {doc.status}</p>
            <p className="text-xs text-gray-500">Uploaded: {new Date(doc.created_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>

  );
}
