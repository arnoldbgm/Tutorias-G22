import { useState } from "react";
import { useEffect } from "react";
import { jwtDecode } from "jwt-decode";

const HomePage = () => {

  const [usuario, setUsuario] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("accessToken");
    const decoded = jwtDecode(token)
    console.log(decoded)
    setUsuario(decoded)

  }, [])


  const imageUrl = "https://cataas.com/cat?type=square";

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 text-gray-800">
      <h1 className="text-9xl font-extrabold tracking-widest text-gray-900">
        HOME PAGE
      </h1>
      <h2>{usuario.role == "admin" 
                    ? "Hola eres un admin"
                    : "Tu rol es de un usuario"}</h2>
      <img src={imageUrl} alt="Cat" className="mt-4 rounded-xl" />
    </div>
  );
};

export default HomePage;
