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
    setTacticianName(data[5]['tactician__name'])
    setTacticianPath(data[5]['tactician__path'])
    setTacticianPlacement(data[5]['avg_placement'])  
    setTacticianGameCount(data[5]['game_count'])
    
  }
      

  async function fetchUnits()
  {
    const response = await fetch ('http://127.0.0.1:8000/api/popular-units/')
    if (!response.ok)
      {
        throw new Error(`HTTP Error, Status: ${response.status}`);
      }
      const data = await response.json();
      console.log(data[0])

      if (data) setUnitFetch(true)

      setUnitName(data[0]['unit__character_id'])
      setUnitPlacement(data[0]['avg_placement'])




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
    <>
    {/* {mostPlayedUnits['unit__character_id'].replace(' ','')} */}
    </>
    :
    <>
      LOADING / PROBLEM FETCHING
    </>
    }

      
    </main>
  )


}