import { useEffect, useState } from "react"
import { jwtDecode } from "jwt-decode"
import { Outlet, Navigate } from "react-router-dom"

// Creamos un componente llamado Rutas Privadas
export default function PrivateRoutes() {

   const [isAuthenticated, setIsAuthenticated] = useState(false);

   const isTokenExpired = (token) => {
      try {
         const decoded = jwtDecode(token);
         // Vamos a validar si caduco o no
         return Date.now() / 1000 > decoded.exp; // Si es true, que caduco mi token
      } catch (error) {
         return true;
      }
   }

   const refreshAccessToken = async () => {
      try {
         const refreshToken = localStorage.getItem("refreshToken");
         if (!refreshToken || isTokenExpired(refreshToken)) {
            throw new Error("Refresh token expirado o no disponible")
         }

         const response = await fetch("http://127.0.0.1:5000/api/v1/refresh", {
            method: "POST",
            headers: {
               "Content-Type": "application/json"
            },
            body: JSON.stringify({ refresh: refreshToken })
         })

         if (!response.ok) {
            throw new Error("Error al refrescar la token")
         }

         const data = await response.json()
         localStorage.setItem("accessToken", data.access_token);
         localStorage.setItem("refreshToken", data.refresh_token);
         setIsAuthenticated(true)
      } catch (error) {
         localStorage.removeItem("accessToken");
         localStorage.removeItem("refreshToken");
         setIsAuthenticated(false)
      }
   }

   useEffect(() => {
      //  Voy a buscar en localStorage si existe mi accesToken
      const token = localStorage.getItem("accessToken")
      if (!token || isTokenExpired(token)) {
         // Refrescame la token o generame una nueva token
         refreshAccessToken()
      } else {
         setIsAuthenticated(true)
      }
   }, [])


   return isAuthenticated ? <Outlet /> : <Navigate to="/login" />
}
