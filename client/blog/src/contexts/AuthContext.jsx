import axios from "axios"
import { createContext } from "react"
import { useState } from "react";
import {toastSuccessNotify} from "../helper/ToastNotify"


//! Defining

export const AuthContext = createContext()



//! Provider
const AuthContextProvider = (props) => {
const url ="http://127.0.0.1:8000/"

const [currentUser,setCurrentUser] =useState(sessionStorage.getItem("username") || false)
const [key,setKey] =useState("")

//?************************REGİSTER*********************

const createUser =async(email,password,firstName,lastName,userName) =>{
    const response = await axios.post(`${url}users/register/`,{
            "username": userName,
            "first_name": firstName,
            "last_name": lastName,
            "email": email,
            "password": password,
            "password1": password,
    })
    if(response.data.token){
        setCurrentUser(response.data.username)
        sessionStorage.setItem("username",response.data.username)
        setKey(response.data.token)
        toastSuccessNotify("User registered succesfully")
    }
   
}

let values ={
    createUser,
    currentUser
}

  return (
    <AuthContext.Provider value={values} >{props.children}</AuthContext.Provider>
  )
}

export default AuthContextProvider