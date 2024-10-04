'use client'
import { useState, useEffect } from "react"
import Image from "next/image"
import AccessTimeIcon from '@mui/icons-material/AccessTime';


export default function MostUsedUnit({name,path,placement,gameCount})
/**
 * Display the Most used Unit
 * 
 * Param
 * ---------
 * Name, Path, Placement
 */
{
  return(
    <main className="w-max p-4 rounded-md bg-slate-900 h-screen">
        <h1 className="uppercase w-max mx-auto pb-2 ">MOST PLAYED UNIT {AccessTimeIcon}</h1>
        
          <Image
          src= {`/img/tft-tactician/${path}`}
          width={200}
          height={200}
          alt="Picture of Tactician"
          className="shadow-lg  rounded-md"
        />
        <h1>
          {name}
        </h1>
        <p>
          Avg Placement: {(placement)}
        </p>
        <p>
          {gameCount}
          </p>



    </main>
  )
}