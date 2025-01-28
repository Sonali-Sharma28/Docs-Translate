import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Upload from "./components/Upload";
import Query from "./components/Query";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/upload" element={<Upload />} />
                <Route path="/query" element={<Query />} />
            </Routes>
        </Router>
    );
}

export default App;
