'use client'
import { useState, useEffect } from "react"

export default async function GetMatches()
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
