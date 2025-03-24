// Para poder usar las rutas en express debemos de importar
import { Router } from "express";
import { createClients } from "../controllers/clientes.controller.js"


// Instancia de las rutas de express
export const api = Router();

api.post("/clientes", createClients)