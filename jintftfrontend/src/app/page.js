'use client'
import { useState, useEffect } from "react"
import Image from "next/image"


export default function Home(){

  // http://127.0.0.1:8000/api/games/NA1_5115648728

  const [tacticianName,setTacticianName] = useState('')
  const [tacticianPath,setTacticianPath] = useState('')
  const [tacticianAvgPlacement,setTacticianAvgPlacement] = useState('')


  async function fetchTactician()
  {
    const response = await fetch ('http://127.0.0.1:8000/api/most-played-tactician/')
    if (!response.ok)
    {
      throw new Error(`HTTP Error, Status: ${response.status}`);
    }
    const data = await response.json();
    setTacticianName(data['name'])
    setTacticianPath(data['path'])
    setTacticianAvgPlacement(data['placements'])
    
  }

  useEffect(()=>
  {
    fetchTactician()
  },[])


  return(
    <main>
      <h1>Jins TFT Stats</h1>
      {tacticianName}

      {tacticianPath ? 
        <div>
          <Image
          src="/profile.png"
          width={500}
          height={500}
          alt="Picture of the author"
        />
            

        </div>
      
      :

      <div>
        No path found
      </div>
    
    }

      {}



      
      
    </main>
  )


}