import React, { useState } from "react";
import axios from "axios";

const Query = () => {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const handleQuery = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:8000/query", { question });
            setAnswer(response.data.answer);
        } catch (error) {
            console.error("Error querying", error);
        }
    };

    return (
        <div>
            <h2>Ask a Question</h2>
            <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} />
            <button onClick={handleQuery}>Submit</button>
            <p><strong>Answer:</strong> {answer}</p>
        </div>
    );
};

export default Query;
