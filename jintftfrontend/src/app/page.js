'use client'
import { useState, useEffect } from "react"
import Image from "next/image"
import MostUsedTactician from "./components/mostplayedtactician";
import MostUsedUnit from "./components/mostplayedunit";

// use divider for the games
import Divider from '@mui/material/Divider';

// for analytics on my things
// https://mui.com/material-ui/react-table/


export default function Home(){

  // http://127.0.0.1:8000/api/games/NA1_5115648728



  // Things useState variables are for the Most played Tactician,Unit and Trait
  // ---------------TACTICIAN--------------
  const [tacticianFetch,setTacticianFetch] = useState(false)

  const [tacticianName,setTacticianName] = useState('')
  const [tacticianPath,setTacticianPath] = useState('')
  const [tacticianPlacement,setTacticianPlacement] = useState([])
  const [tacticianGameCount,setTacticianGameCount] = useState(0)

// ------------------UNIT---------------------
  const [unitFetch,setUnitFetch] = useState(false)


  const [mostPlayedUnits,setMostPlayedUnits] = useState([])
  const [unitName,setUnitName] = useState('')
  const [unitPath,setUnitPath] = useState('')
  const [unitPlacement,setUnitPlacement] = useState('')
  const [unitGameCount,setUnitGameCount] = useState('')
  const [allUnits,setAllUnits] = useState([])

  // ---------------TRAIT---------------------





  async function fetchTactician()
  {
    const response = await fetch ('http://127.0.0.1:8000/api/most-played-tactician/')
    if (!response.ok)
    {
      throw new Error(`HTTP Error, Status: ${response.status}`);
    }
    const data = await response.json();

    // checks if fetch was successful 
    if (data) setTacticianFetch(true)
    

    // if successful populate variables
    setTacticianName(data[0]['tactician__name'])
    setTacticianPath(data[0]['tactician__path'])
    setTacticianPlacement(data[0]['avg_placement'])  
    setTacticianGameCount(data[0]['game_count'])
    
  }
      

  async function fetchUnits()
  {
    const response = await fetch ('http://127.0.0.1:8000/api/popular-units/')
    if (!response.ok)
      {
        throw new Error(`HTTP Error, Status: ${response.status}`);
      }
      const data = await response.json();
      // console.log(data[0])

      if (data) setUnitFetch(true)

      const name = data[0]['unit__character_id']

      const avg_placement = data[0]['avg_placement']

      const game_count = data[0]['game_count']

      setUnitName(name)
      setUnitPlacement(data[0]['avg_placement'])

      // Replace the spaces inside a string to allow it for the img
      const path = name.replace(/\s/g, '')
      setUnitPath(path)

      setUnitPlacement(avg_placement)
      setUnitGameCount(game_count)


      // avg_placement: 4.38
      // game_count: 26
      // unit__character_id: " Tahm Kench"

  }

  
  useEffect(()=>
  {
    fetchTactician()
    fetchUnits()

      

  },[])


  return(
    <main>

      {/* <h1 className="font-bold text-2xl pb-4">Home</h1> */}


      <div className="flex justify-around">

        {tacticianFetch ? 
          <div>
            <MostUsedTactician name={tacticianName} path={tacticianPath} placement={tacticianPlacement} gameCount={tacticianGameCount}/>
          </div>
        :
        <div>
        LOADING / PROBLEM FETCHING
        </div>
      
      }
        {}

      { unitFetch ?
      <div>

        <MostUsedUnit name={unitName} path={unitPath} placement={unitPlacement} gameCount={unitGameCount}/>
      </div>
      :
      <>
        LOADING / PROBLEM FETCHING
      </>
      }
      
      </div>


      
    </main>
  )


}