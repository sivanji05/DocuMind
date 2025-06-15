import { useEffect, useState } from "react";
import api from "../services/api";

export default function Chat() {
  const [documents, setDocuments] = useState([]);
  const [selectedDocId, setSelectedDocId] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  // Fetch uploaded documents
 useEffect(() => {
  const fetchDocs = async () => {
    try {
      const res = await api.get("/api/documents/list");
      setDocuments(res.data);
    } catch (err) {
      console.error("Failed to fetch docs:", err);
    }
  };
  fetchDocs();
}, []);

 const handleAsk = async () => {
  if (!question || !selectedDocId) return;

  setLoading(true);
  setAnswer("");

  try {
    const res = await api.post("/api/documents/ask", {
      question,
      document_id: selectedDocId,
    }); 
    setAnswer(res.data.answer);
  } catch (err) {
    setAnswer("Error: Could not get answer.");
    console.error(err);
  } finally {
    setLoading(false);
  }
};


  return(

  <div className="max-w-3xl mx-auto mt-10 space-y-6 px-4">
    <h2 className="text-3xl font-bold text-gray-800">Ask Questions About Your Document</h2>

    <select
      value={selectedDocId}
      onChange={(e) => setSelectedDocId(e.target.value)}
      className="w-full border border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
    >
      <option value="">Select a Document</option>
      {documents.map((doc) => (
        <option key={doc.id} value={doc.id}>
          {doc.file_name}
        </option>
      ))}
    </select>

    <textarea
      rows="4"
      className="w-full border border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
      placeholder="Ask your question..."
      value={question}
      onChange={(e) => setQuestion(e.target.value)}
    />

    <button
      onClick={handleAsk}
      disabled={loading}
      className="bg-indigo-600 text-white px-6 py-3 rounded-lg shadow hover:bg-indigo-700 transition disabled:opacity-50"
    >
      {loading ? "Thinking..." : "Ask"}
    </button>

    {answer && (
      <div className="mt-6 p-4 bg-gray-100 border rounded-lg">
        <strong className="text-gray-800">Answer:</strong>
        <p className="mt-2 text-gray-700">{answer}</p>
      </div>
    )}
  </div>

  );
}
