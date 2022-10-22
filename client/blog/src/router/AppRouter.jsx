import React from 'react'
import {BrowserRouter,Routes,Route } from 'react-router-dom'
import NavBar from '../components/Navbar'
import Home from '../pages/Home'
import Login from '../pages/Login'
import NewPost from '../pages/NewPost'
import Register from '../pages/Register'


const AppRouter = () => {
  return (
    <BrowserRouter>
     <NavBar/>
    <Routes>
        <Route path="/" element ={<Home/>}/>
        <Route path="/login" element ={<Login/>}/>
        <Route path="/register" element ={<Register/>}/>
        <Route path="/newpost" element ={<NewPost/>}/>

    </Routes>

    </BrowserRouter>
  )
}

export default AppRouter