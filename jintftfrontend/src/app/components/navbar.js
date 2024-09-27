'use client'
import HomeIcon from '@mui/icons-material/Home';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import SmartToyIcon from '@mui/icons-material/SmartToy';
import SportsEsportsIcon from '@mui/icons-material/SportsEsports';
import { usePathname } from 'next/navigation'

export default function VerticalNavbar() {
  const pathname = usePathname();

  const items = [
    { text: 'Home', icon: <HomeIcon />, link: '/' },
    { text: 'Stats', icon: <TrendingUpIcon />, link: '/stats' },
    { text: 'Tacticians', icon: <SmartToyIcon />, link: '/tacticians' },
  ];

  return (
    <div className="h-screen w-44 bg-slate-900 text-white flex flex-col shadow-lg ">
      {/* Logo or Header */}
      <div className="p-4  text-xl flex items-center border-b border-gray-700 w-full justify-center">
        <SportsEsportsIcon fontSize="large" className="mr-2" />
        {/* <span className="font-bold">Game Stats</span> */}
      </div>
      
      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto ">
        <ul className="space-y-4 py-2  ">
          {items.map((item, index) => (
            <li key={index} className={`flex items-center hover:bg-slate-600 cursor-pointer py-3 w-2/2 pl-5 transition ease-in-out duration-300 
            ${pathname === item.link ? 'bg-gradient-to-r from-slate-500 border-l-2 border-gray-300 rounded-none' : ''}`}>
              <span className="mr-3 align-text-top flex">{item.icon}</span>
              <span>{item.text}</span>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
} 
