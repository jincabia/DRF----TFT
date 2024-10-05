'use client';
import { useState } from "react";
import Image from "next/image";
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import { Accordion, AccordionSummary, AccordionDetails, Typography,  Box } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

import { purple, red,blueGrey, blue, grey } from '@mui/material/colors';

// const accent = purple.A200; // #e040fb (alternative method)


export default function MostUsedTactician({ name, path, placement, gameCount }) {

  return(
    <main className="bg-slate-900 p-4 rounded-md w-max ">

    <header className="flex items-center justify-center space-x-2 pb-1 border-b-2 border-slate-700 mb-3">
      <AccessTimeIcon className="align-text-bottom" fontSize="xs" />
      <h1 className="uppercase font-medium text-sm text-slate-300 ">
        Most Played Tactician
      </h1>
    </header>

            {/* Grid Layout */}
      <div className="grid grid-row-1 grid-flow-row ">

        

    {/* Tactician Image */}
<div className="row-span-3 flex justify-center pb-2">
  <Image
    src={`/img/tft-tactician/${path}`}
    width={200}
    height={200}
    alt="Picture of Tactician"
    className="shadow-lg rounded-md object-cover w-[200px] h-[150px]"
  />
</div>

      {/* Tactician Name */}
      {/* <div className=" col-span-1 bg-slate-800 rounded-b-md">
        <header className="flex mb-2 border-b-2 border-slate-800 ">
          <h1 className="uppercase px-2 py-1 w-11/12 mx-auto text-slate-400 font-semibold text-xs border-b-2 border-slate-700">
            NAME
          </h1>
        </header>
        <p className="px-4 mb-2 uppercase text-xs text-slate-300 font-semibold">{name}</p>
      </div> */}

      {/* Game Count and Average Placement beside each other */}
      {/* <div className="col-span-2 grid grid-cols-2 gap-4">

        {/* Average Placement */}
        {/* <div className="bg-slate-800 rounded-md">
          <header className="flex mb-2 align-text-top border-b-2 border-slate-800">
            <h1 className="uppercase px-2 py-1 w-11/12 mx-auto text-slate-400 font-semibold text-xs border-b-2 border-slate-700">
              AVERAGE PLACEMENT
            </h1>
          </header>
          <p className="px-4 mb-2 uppercase text-xs text-slate-300 font-semibold">{placement}</p>
        </div> */}

        {/* Number of Games */}
        {/* <div className="bg-slate-800 rounded-md">
          <header className="flex mb-2 align-text-top border-b-2 border-slate-800">
            <h1 className="uppercase px-2 py-1 w-11/12 mx-auto text-slate-400 font-semibold text-xs border-b-2 border-slate-700">
              # OF GAMES
            </h1>
          </header>
          <p className="px-4 mb-2 uppercase text-xs text-slate-300 font-semibold">{gameCount}</p>
        </div> */}

      {/* </div> */} 
      
      <div>

        <Accordion sx={{ bgcolor:  '#1e293b' }}>
          <AccordionSummary sx={{flex:1,justifyContent:'center',textAlign:'center'}} expandIcon={<ExpandMoreIcon sx={{ color: 'white',flex:'1', justifyContent:'center', textAlign: 'center'}} />}>
            {/* <Typography sx={{ color: '#cbd5e1', fontWeight: 'semibold', fontSize: 14 }}>Details</Typography> */}
            <h1 className="text-slate-300 text-sm font-semibold uppercase w-full">
              Details
            </h1>
          </AccordionSummary>
          <AccordionDetails sx={{bgcolor:'#334155'}} className=" rounded-b-sm h-max">
            <div className="flex flex-col justify-center justify-items-center text-center">

            <h1 className="text-slate-500 border-b-2 border-slate-600 font-semibold text-xs uppercase mx-auto w-1/2 ">
                  Name
                  </h1>
                  <p className=" text-slate-300 w-max mx-auto text-md mb-4">
                    {name}
                  </p>


              <h1 className="text-slate-500 border-b-2 border-slate-600 font-semibold text-xs uppercase mx-auto  ">
                Avg Placement
                </h1>
                <p className=" text-slate-300 w-max mx-auto text-md mb-4">
                  {placement}
                </p>
              <h1  className="text-slate-500 border-b-2 border-slate-600 font-semibold text-xs uppercase mx-auto  ">Games Played</h1>
              <p className=" text-slate-300 w-max mx-auto text-md">
                  {gameCount}
                </p>

            </div>


            {/* <Typography variant="body2" sx={{ mb: 1 ,color:'#cbd5e1'}}>Placement: {placement}</Typography> */}
            {/* <Typography variant="body2">Games Played: {gameCount}</Typography> */}
          </AccordionDetails>
        </Accordion>

      </div>


      {/* End of Grid Layout */}
      </div>




    </main>


  )
  
  return (
    <Box sx={{ maxWidth: 300, p: 2, bgcolor: '#0f172a', borderRadius: 2 }}>
      {/* Header */}
      <Box display="flex" alignItems="center" justifyContent="center" mb={2} borderBottom={1} borderColor="#1f3940" padding={1}>
        <AccessTimeIcon sx={{ color: 'white', mr: 1 }} fontSize="xs" />
        <Typography variant="body2" sx={{ color: '#8a90a9', fontWeight: 'medium', textTransform: 'uppercase' }}>
          Most played Tactician
        </Typography>
      </Box>

      {/* Tactician Image */}
      <Box sx={{ display: 'flex', justifyContent: 'center' }}>
        <Image
          src={`/img/tft-tactician/${path}`}
          width={200}
          height={200}
          alt="Tactician"
          className="shadow-lg rounded-t-lg"
        />
      </Box>

      {/* Tactician Name */}

     

      <Box sx={{ bgcolor: '#1f3940', py: 1, borderRadius: 1, textAlign: 'center', width:'full' }}>
        <Typography variant="body2" sx={{ color: '#ced4f0', fontWeight: 'bold', textTransform: 'uppercase' }}>
          {name}
        </Typography>
      </Box>

      {/* Dropdown for Placement and Game Count */}
      <Accordion sx={{ mt: 2, bgcolor: 'primary.light' }}>
        <AccordionSummary expandIcon={<ExpandMoreIcon sx={{ color: 'text.secondary' }} />}>
          <Typography sx={{ color: 'text.secondary', fontWeight: 'bold', fontSize: 14 }}>Details</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography variant="body2" sx={{ mb: 1 }}>Placement: {placement}</Typography>
          <Typography variant="body2">Games Played: {gameCount}</Typography>
        </AccordionDetails>
      </Accordion>
    </Box>
  );
}
