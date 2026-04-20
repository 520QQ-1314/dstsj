"use client"
import { useState } from "react"

export default function Home() {
  const [prompt, setPrompt] = useState("")
  const [image, setImage] = useState("")

  const generate = async () => {
    const res = await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ prompt })
    })

    const data = await res.json()
    setImage(data.image_url)
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>AI Poster SaaS MVP</h1>

      <textarea
        style={{ width: 400, height: 100 }}
        onChange={(e)=>setPrompt(e.target.value)}
      />

      <br />

      <button onClick={generate}>
        Generate
      </button>

      {image && (
        <div>
          <img src={image} width={400} />
        </div>
      )}
    </div>
  )
}
