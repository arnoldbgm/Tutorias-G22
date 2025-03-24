// Importacion de express
import express from "express";
import { api as clientesRouter } from "./routes/clientes.routes.js";

// Inicializacion de la instancia de express
const app = express()
// Escogemos el puerto donde se levantara express
const port = 3000

app.use(express.json()); 
// Aqui es donde puedo usar las rutas de mis archivos de barril
// http://localhost:3000/api/v1/clientes
app.use("/api/v1", clientesRouter)

// Aqui ira la ejecución de mi backend
try {
   app.listen(port, () => {
      console.log(`Mi Backend esta funcionando 🔥🎉🦾 `);
      console.log(`http://localhost:${port}/`);
   })
} catch (error) {
   console.log(error)
}