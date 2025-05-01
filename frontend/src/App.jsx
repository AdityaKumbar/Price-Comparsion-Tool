import { useState } from 'react';
import './App.css';

const categories = ["Electronics", "Fashion", "Food Delivery", "Groceries", "Travel"];

function App() {
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("Electronics");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const response = await fetch("http://127.0.0.1:8000/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query, category })
    });
    const data = await response.json();
    setResults(data.data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Price Comparison App</h1>
      
      <select value={category} onChange={(e) => setCategory(e.target.value)}>
        {categories.map(cat => (
          <option key={cat} value={cat}>{cat}</option>
        ))}
      </select>

      <input
        type="text"
        placeholder="Search product..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>

      <div>
        {results.map((item, index) => (
          <div key={index} style={{ border: "1px solid #ccc", margin: 10, padding: 10 }}>
            <h3>{item.platform}</h3>
            <p>Price: ₹{item.price}</p>
            <p>Rating: {item.rating}</p>
            <p>Delivery: {item.delivery}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
