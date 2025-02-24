import { useEffect, useState } from "react";
import { jwtDecode } from "jwt-decode";
import { Outlet, Navigate } from "react-router-dom";

export default function PrivateRoutes() {
   const [isAuthenticated, setIsAuthenticated] = useState(null); // null indica carga inicial

   const isTokenExpired = (token) => {
      try {
         const decoded = jwtDecode(token);
         return Date.now() / 1000 > decoded.exp;
      } catch (error) {
         return true;
      }
   };

   const refreshAccessToken = async () => {
      try {
         const refreshToken = localStorage.getItem("refreshToken");
         if (!refreshToken || isTokenExpired(refreshToken)) {
            throw new Error("Refresh token expirado o no disponible");
         }

         const response = await fetch("http://127.0.0.1:5000/api/v1/refresh", {
            method: "POST",
            headers: { 'Authorization': `Bearer ${refreshToken}` },
         });

         if (!response.ok) throw new Error("Error al refrescar el token");

         const data = await response.json();
         localStorage.setItem("accessToken", data.access_token);
         localStorage.setItem("refreshToken", data.refresh_token);
         setIsAuthenticated(true);
      } catch (error) {
         console.error("Error al refrescar el token:", error);
         localStorage.removeItem("accessToken");
         localStorage.removeItem("refreshToken");
         setIsAuthenticated(false);
      }
   };

   useEffect(() => {
      const token = localStorage.getItem("accessToken");

      if (!token || isTokenExpired(token)) {
         refreshAccessToken();
      } else {
         setIsAuthenticated(true);
      }
   }, []);

   if (isAuthenticated === null) return <div>Cargando...</div>; // Evita el redireccionamiento en carga

   return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
}
