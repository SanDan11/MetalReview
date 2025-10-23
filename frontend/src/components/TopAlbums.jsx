import { useEffect, useState } from "react"

export default function TopAlbums() {
  const [albums, setAlbums] = useState([])
  const [selectedYear, setSelectedYear] = useState("")
  const [years, setYears] = useState([])

  // Build dropdown years (last 10)
  useEffect(() => {
    const currentYear = new Date().getFullYear()
    const generatedYears = Array.from({ length: 10 }, (_, i) => currentYear - i)
    setYears(generatedYears)
  }, [])

  // Fetch albums for the selected year
  useEffect(() => {
    const url = selectedYear
      ? `http://127.0.0.1:8000/albums/top5?year=${selectedYear}`
      : `http://127.0.0.1:8000/albums/top5`

    fetch(url)
      .then((res) => res.json())
      .then((data) => setAlbums(data))
  }, [selectedYear])

  return (
    <section className="p-6 bg-gray-900 text-white rounded-2xl shadow-lg w-full max-w-5xl mx-auto mb-10">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-3xl font-bold text-yellow-400">🏆 Top 5 Albums</h2>

        <select
          className="bg-gray-800 text-white p-2 rounded-md border border-gray-700"
          value={selectedYear}
          onChange={(e) => setSelectedYear(e.target.value)}
        >
          <option value="">All Years</option>
          {years.map((year) => (
            <option key={year} value={year}>
              {year}
            </option>
          ))}
        </select>
      </div>

      <ul className="space-y-3">
        {albums.map((album, index) => (
          <li
            key={album.id}
            className="flex justify-between border-b border-gray-700 pb-2 hover:bg-gray-800 rounded-md transition"
          >
            <span>
              {index + 1}. {album.title} – {album.artist} ({album.year})
            </span>
            <span className="font-semibold text-green-400">{album.rating}/10</span>
          </li>
        ))}
      </ul>
    </section>
  )
}
