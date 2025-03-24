import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();
const API_TOKEN = "";

/**
 * Función para obtener datos de la API según el tipo de documento.
 */
const fetchDataFromAPI = async (tipo, numero) => {
   const url = tipo === "dni"
      ? `https://api.apis.net.pe/v2/reniec/dni?numero=${numero}`
      : `https://api.apis.net.pe/v2/sunat/ruc/full?numero=${numero}`;

   try {
      const response = await fetch(url, {
         method: "GET",
         headers: {
            "Authorization": `Bearer ${API_TOKEN}`,
            "Content-Type": "application/json"
         }
      });

      if (!response.ok) {
         throw new Error(`Error en API: ${response.statusText}`);
      }

      return await response.json();
   } catch (error) {
      console.error(`Error al obtener datos de API (${tipo}):`, error);
      return null;
   }
};

/**
 * Controlador para crear clientes.
 */
export const createClients = async (req, res) => {
   try {
      const { documento, numero } = req.body;

      if (!documento || !numero) {
         return res.status(400).json({ error: "Faltan datos requeridos" });
      }

      // Verificar si ya existe el cliente
      const clienteExistente = await prisma.clientes.findFirst({
         where: { numeroDocumento: numero }
      });

      if (clienteExistente) {
         return res.status(200).json(clienteExistente);
      }

      // Obtener datos de la API según el tipo de documento
      const apiData = await fetchDataFromAPI(documento, numero);

      if (!apiData) {
         return res.status(500).json({ error: "No se pudieron obtener datos del cliente" });
      }

      let clienteNuevo;

      if (documento === "dni") {
         clienteNuevo = await prisma.clientes.create({
            data: {
               tipoDocumento: "DNI",
               numeroDocumento: apiData.numeroDocumento,
               nombre: `${apiData.apellidoPaterno} ${apiData.apellidoMaterno}, ${apiData.nombres}`
            }
         });
      } else if (documento === "ruc") {
         clienteNuevo = await prisma.clientes.create({
            data: {
               tipoDocumento: "RUC",
               numeroDocumento: apiData.numero,
               nombre: apiData.nombre_o_razon_social
            }
         });
      } else {
         return res.status(400).json({ error: "Tipo de documento no válido" });
      }

      return res.status(201).json(clienteNuevo);
   } catch (error) {
      console.error("Error en createClients:", error);
      return res.status(500).json({ error: "Error interno del servidor" });
   }
};
