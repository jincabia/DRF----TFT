'use client'
import { useState, useEffect } from "react"

export async function getMatches()
{

  try {
    const res = await fetch('http://localhost:8000/api/games/')
    const data = await res.json();
    console.log(data)
    return(data)
  } catch (error) {
    console.error(error)
    return [] 
  }
}

export async function getMatchInfo(game_id)
{
  try {
    const res = await fetch(`http://localhost:8000/api/recent/${game_id}/`)
    const data = await res.json();
    return data
  } catch (error) {
    console.error(error)
    return [] 
  }
}



export default function Home(){

  const [games,setGames] = useState([])
  const [gameInfo,setGameInfo] = useState([])
  useEffect(
    ()=>
    {
      async function fetchData() {
        const data = await getMatches();  // Await the promise
        setGames(data);  // Set the resolved data to state
      }
  
      fetchData();
    },[]
  )

  async function fetchGameInfo(game_id)
  {
    const data = await getMatchInfo(game_id)


    

    setGameInfo(data['info']['gameId'])
  }

  const whenGameClicked = (game_id) =>
  {
    fetchGameInfo(game_id)
  } 
  





  return(
    <main>
      {/* {games} */}

      {gameInfo}

      {games.length > 0  ? (


        <div>
          {games.map((game,index) =>
          (
            <button key={index} onClick={()=>whenGameClicked(game.game_id)}>
              {game.game_id} ,
            </button>
          )
        )}
        </div>
      ) : 
      (
        <div>
          bruh
        </div>
      )
    }
      
    </main>
  )


}