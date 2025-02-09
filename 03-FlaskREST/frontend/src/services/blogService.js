// Obtener todos los posts
export const fetchPosts = async () => {
   try {
     const response = await fetch('http://127.0.0.1:5000/api/v1/get-posts');
     if (!response.ok) {
       throw new Error('Error al obtener los datos');
     }
     const data = await response.json();
     return data;
   } catch (error) {
     console.error('Error:', error);
     throw error;
   }
 };