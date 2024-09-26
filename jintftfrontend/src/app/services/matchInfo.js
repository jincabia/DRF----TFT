'use client'
import { useState, useEffect } from "react"


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