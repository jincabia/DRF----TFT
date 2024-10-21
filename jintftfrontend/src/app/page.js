'use client'
import { useState, useEffect } from "react"
import Image from "next/image"
import MostUsedTactician from "./components/mostplayedtactician";
import MostUsedUnit from "./components/mostplayedunit";

// use divider for the games
import Divider from '@mui/material/Divider';
import MostUsedTrait from "./components/mostplayedtrait";
import PlacementLineChart from "./components/placementlinechart";
import EmojiEventsIcon from '@mui/icons-material/EmojiEvents';


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
  const [traitFetch,setTraitFetch] = useState(false)

  const [traitName,setTraitName] = useState('')
  const [traitPath,setTraitPath] = useState('')
  const [traitPlacement,setTraitPlacement] = useState('')
  const [traitGameCount,setTraitGameCount] = useState('')

 // ---------------TRAIT---------------------
 const [placementFetch,setPlacementFetch] = useState(false)

 const [placements,setPlacements] = useState([])
 const [games,setGames] = useState([])



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

  async function fetchTrait()
  {
    const response = await fetch ('http://127.0.0.1:8000/api/popular-traits/')
    if (!response.ok)
      {
        throw new Error(`HTTP Error, Status: ${response.status}`);
      }
      const data = await response.json();
      console.log(data[0])

      if (data) setTraitFetch(true)

      const name = data[0]['static_trait_details__trait_name'].replace(/([A-Z])/g,' $1'.trim())
      console.log('this is name', name)
      const avg_placement = data[0]['avg_placement']
      const game_count = data[0]['game_count']




      // s = s.replace(/([A-Z])/g, ' $1').trim()

      // Need to find the path towards the img

      setTraitName(name)
      setTraitPlacement(avg_placement)

      // Replace the spaces inside a string to allow it for the img
      const path = name.replace(/\s/g, '')
      console.log(path)
      setTraitPath(path)

      // setTraitPlacement(avg_placement)
      setTraitGameCount(game_count)
  }

  async function fetchPlacements()
  {
    const response = await fetch ('http://127.0.0.1:8000/api/view-placements/')
    if (!response.ok)
      {
        throw new Error(`HTTP Error, Status: ${response.status}`);
      }


      const data = await response.json();

      for (let i =0;i <10;i++)
      {
        // console.log(data[i].game)
        setPlacements((prevPlacements) => [...prevPlacements, data[i].placement]);
        setGames((prevGames)=> [...prevGames, data[i].game])
      }
      // console.log(data)


      // setPlacements(data)

      if (data) setPlacementFetch(true)

      // console.log(placements)

      




      // s = s.replace(/([A-Z])/g, ' $1').trim()

      // Need to find the path towards the img

      
  }

  
  
  useEffect(()=>
  {
    fetchTactician()
    fetchUnits()
    fetchTrait()
    fetchPlacements()


      

  },[])


  return(
    <main>

    
      {/* <h1 className="font-bold text-2xl pb-4">Home</h1> */}


      <div className="flex justify-around">

        {/* <button onClick={()=> console.log(placements)}>
          Click me
        </button> */}

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

{ traitFetch ?
      <div>

        <MostUsedTrait name={traitName} path={traitPath} placement={traitPlacement} gameCount={traitGameCount}/>
      </div>
      :
      <>
        LOADING / PROBLEM FETCHING
      </>
      }
      
      </div>


    {placementFetch && 
    <div className="bg-slate-900 w-max p-2 mt-5 rounded-md">

    <header className="flex items-center justify-center space-x-2 pb-1 border-b-2 border-slate-700 mb-3">
          <EmojiEventsIcon className="align-text-bottom" fontSize="xs" />
          <h1 className="uppercase font-medium text-sm text-slate-300 ">
            recent placements
          </h1>
        </header>

      <div className="bg-slate-700 m-4 rounded-md   ">

        <PlacementLineChart placements={placements} games={games}/>

        

      </div>
    
    
    </div>}

      


      
    </main>
  )


}