'use client'
import { useState, useEffect } from "react"
import Image from "next/image"


// use divider for the games
import Divider from '@mui/material/Divider';

// for analytics on my things
// https://mui.com/material-ui/react-table/


export default function Home(){

  // http://127.0.0.1:8000/api/games/NA1_5115648728

  const [tacticianName,setTacticianName] = useState('')
  const [tacticianPath,setTacticianPath] = useState('')
  // the tacticianPlacement is the list of all placements
  const [tacticianPlacement,setTacticianPlacement] = useState([])

  // the avg placement calculated from the tactician placement var
  const [avgPlacement,setAvgPlacement] = useState(0)


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
    setTacticianPlacement(data['placements'])


    

    
  }

  const calcAvgPlacement = (tacticianPlacement) =>
  {
    let avg = 0
    for (let i = 0; i < tacticianPlacement.length-1; i++) {
      // console.log(tacticianPlacement)
      avg += tacticianPlacement[i]
    }
    avg /= tacticianPlacement.length

    return(avg)
  }

  useEffect(()=>
  {
    fetchTactician()

      

  },[])


  return(
    <main>

      {/* <h1 className="font-bold text-2xl pb-4">Home</h1> */}

      {tacticianPath ? 
        <div className="w-max p-4 rounded-md bg-slate-900">

          <h1 className=" w-max mx-auto pb-2">Most played Tactician</h1>
          

        {/* TODO 
        */}
          <Image
          src= {`/img/tft-tactician/${tacticianPath}`}
          width={200}
          height={200}
          alt="Picture of Tactician"
          className="shadow-lg  rounded-md"
        />


          {/* This is a lsit of all the placements 1-8 */}

          {tacticianName}

          {/* {avgPlacement} */}

          <p>
            Avg Placement: {calcAvgPlacement(tacticianPlacement)}
          </p>


          {/* {tacticianPlacement.map((placement,index) => (
            <div key={index}>
              <p>{placement}</p>
            </div>
          ))} */}


          <p>
            


          </p>

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