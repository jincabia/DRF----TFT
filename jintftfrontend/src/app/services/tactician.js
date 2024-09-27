'use client'
import { useState, useEffect } from "react"


export async function getTactician()
{
  try {
    const res = await fetch(`http://127.0.0.1:8000/api/most-played-tactician/`)
    const data = await res.json();
    return data
  } catch (error) {
    console.error(error)
    return [] 
  }
}