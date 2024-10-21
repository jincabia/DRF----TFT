'use client';
import { useState,useEffect } from "react";
import Image from "next/image";
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import { Accordion, AccordionSummary, AccordionDetails, Typography,  Box } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { LineChart } from '@mui/x-charts/LineChart';
import { lineElementClasses } from "@mui/x-charts/LineChart";
import { axisClasses } from "@mui/x-charts";

// Get data from backend to populate 
export default function PlacementLineChart({placements,games})


{
  const [colorX, setColorX] = useState('None');
  const [colorY, setColorY] = useState('piecewise');

  const [itemData,setItemData] = useState([])
  const [axisData,setAxisData] = useState([])

  const [gameInfo,setGameInfo] = useState()



  const colors = ['#006BD6', '#EC407A'];
  const placementData = placements.slice(0, 10);
  const gamesData = games.slice(0,10)

  const avgPlacement = array => array.reduce((a, b) => a + b) / array.length;


  
  async function fetchGame(game)
  {
    const response = await fetch (`http://127.0.0.1:8000/api/find-game/${game}`)
    if (!response.ok)
    {
      throw new Error(`HTTP Error, Status: ${response.status}`);
    }
    const data = await response.json();

    // checks if fetch was successful 
    // if (data) setTacticianFetch(true)
    

    // if successful populate variables
    setGameInfo(data[0].game_info.game_info.metadata.participants)
    console.log(data)
    
    
  }

  
  useEffect(()=>
    {

    },[])
      
  
 

  return (
    <div>
       {gameInfo && <p className="bg-red-500">
            {gameInfo} hi
            </p>}
      {/* <h1> {avgPlacement(placementData)}</h1> */}
      <p>

        <button onClick={()=> console.log(gameInfo)}>
          Click me
        </button>

        {/* {type, seriesId, dataIndex} */}
        {/* {itemData.seriesId} */}

        {/* {dataIndex, axisValue, seriesValues}
        {axisData && <>{axisData.seriesValues}</>} */}

        {/* TODO using the axisData Values find a game and display info */}

        {axisData.seriesValues && <>
        
        {/* This is the Game ID that we'll use to find Game */}
        {axisData.seriesValues.Game} 
         
        </>}
      </p>

      <LineChart 
      slotProps={{ legend: { hidden: true } }}

      onAreaClick={(event, d) => setItemData(d)}
          onMarkClick={(event, d) => setItemData(d)}
          onLineClick={(event, d) => setItemData(d)}
          // onAxisClick={(event, d) => setAxisData(d)}
          onAxisClick={(event,d) => fetchGame(d.seriesValues.Game)}
  
      margin={{bottom:80}}
      
      sx={(theme) => ({
       
        // changes the axis colors
        [`.${axisClasses.root}`]: {
          [`.${axisClasses.tick}, .${axisClasses.line}`]: {
            stroke: '#262638',
            strokeWidth: 3,
          },
          [`.${axisClasses.tickLabel}`]: {
            fill: '#DDDDDD',
          },
        },
      })}
  
  
  
  
      xAxis={[{data:[1,2,3,4,5,6,7,8,9,10],
        
  
        // label: { style: 'white' } // Set the label color to white
  
  
      }]}
      yAxis={[
        {
          min: 0, // Minimum value of the yAxis
          max: 9, // Maximum value of the yAxis
          ticks: [0,1,2,3,4,5,6,7,8], // Define the tick intervals
          
          colorMap:
           
          // If between 4 & 8 == red else green
            (colorY === 'piecewise' && {
              type: 'piecewise',
              thresholds: [4, 8],
              colors: ['green', 'red'],
            }) ||

            (colorY === 'piecewise' && {
              type: 'piecewise',
              thresholds: [0],
              colors: ['pink', 'blue'],
            }) ||
            undefined,
  
  
            data:[1,2,3,5,6,7,8],
            color: '#bab0ab',
  
        },
  
        
      ]}
        series={[
          {
            data: placementData,  // Use the counts for each placement
            // area: true,
            showMark: ({ index }) => index % 2 === 0,
            id: 'Placement',
            label: 'Placement',
            color: '#bab0ab',

            

            highlightScope: {
              highlight: 'Placement',
            },

          },

          {
            data: gamesData,  // Use the counts for each placement
            // area: true,
            showMark: ({ index }) => index % 1 === 0,
            id: 'Game',
            label: 'Game',
            // color: '#bab0ab',
          },

        ]}
        width={500}
        height={300}
      />
    </div>
  );
}