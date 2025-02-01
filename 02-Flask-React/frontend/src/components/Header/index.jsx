import React from 'react'
import logo from "../../assets/logo.svg"
import { Link } from 'react-router-dom'
import { HomePage } from '../../pages'

const Header = () => {
   return (
      <header
         className="w-full h-64 bg-cover bg-center px-4 sm:px-12 md:px-16 lg:px-28 xl:px-32"
         style={{
            backgroundImage:
               "linear-gradient(90deg, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.7)), url('/src/assets/header_bg.jpg')",
         }}
      >
         <div className='flex h-full justify-between items-center'>
            <img src={logo} className="w-96" />
            <div className='flex gap-4'>
               <Link to="/nosotros" className='text-xl font-bold text-white'>Nostros</Link>
               <Link to="/blog" className='text-xl font-bold text-white'>Blog</Link>
               <Link to="/contactanos" className='text-xl font-bold text-white'>Contactanos</Link>
            </div>
         </div>
      </header>
   )
}

export default Header