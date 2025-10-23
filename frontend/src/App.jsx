import { useState, useEffect } from "react";
import axios from "axios";
import TopAlbums from "./components/TopAlbums";

function App() {
  const [albums, setAlbums] = useState([]);
  const [search, setSearch] = useState("");
  const [genre, setGenre] = useState("");
  const [minRating, setMinRating] = useState("");

  const fetchAlbums = async () => {
    try {
      const params = {};
      if (search) params.search = search;
      if (genre) params.genre = genre;
      if (minRating) params.min_rating = minRating;

      const res = await axios.get("http://127.0.0.1:8000/albums", { params });
      setAlbums(res.data);
    } catch (err) {
      console.error("Error fetching albums:", err);
    }
  };

  useEffect(() => {
    fetchAlbums();
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <h1 className="text-4xl font-bold text-red-500 mb-6 text-center">
        🔥 Metal Review Library 🔥
      </h1>

      {/* 🏆 Top 5 Albums Section */}
      <TopAlbums />

      {/* 🔍 Search and Filters */}
      <div className="flex flex-col sm:flex-row justify-center gap-4 mb-8 bg-gray-800 p-4 rounded-xl shadow-md">
        {/* your existing inputs and buttons here */}
      </div>

      {/* 🧱 Album Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {albums.length > 0 ? (
          albums.map((album) => (
            <div
              key={album.id}
              className="bg-gray-800 p-4 rounded-xl shadow-md hover:scale-105 transition"
            >
              <h2 className="text-xl font-semibold text-white">
                {album.title}
              </h2>
              <p className="text-gray-400">{album.artist}</p>
              <p className="text-sm italic text-gray-500">{album.genre}</p>
              <p className="mt-2 font-bold text-yellow-400">
                ⭐ {album.rating}
              </p>
              <button
                onClick={() => window.open(`/album/${album.id}`, "_self")}
                className="mt-3 bg-red-600 hover:bg-red-700 px-3 py-1 rounded"
              >
                View Review
              </button>
            </div>
          ))
        ) : (
          <p className="text-center text-gray-400 col-span-3">
            No albums found.
          </p>
        )}
      </div>
    </div>
  );
}

export default App;
