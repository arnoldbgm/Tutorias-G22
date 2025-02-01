import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { HeaderComponent } from '../../components';
import PostImg from "../../assets/post_bg.jpg"

const BlogDetailPage = () => {
   const { id } = useParams();
   const [post, setPost] = useState(null);

   useEffect(() => {
      const fetchPost = async () => {
         try {
            const response = await fetch(`http://127.0.0.1:5000/api/v1/posts/${id}`); // Cambia esto a la URL de tu API
            if (!response.ok) {
               throw new Error('Error al obtener los datos');
            }
            const data = await response.json();
            setPost(data); // Guarda el post en el estado
         } catch (error) {
            console.error('Error:', error);
         }
      };

      fetchPost(); // Llama a la función para obtener el post
   }, [id]);


   return (
      !post ? (
         <>
            <HeaderComponent />
            <p className='mt-28 text-4xl  font-extralight flex justify-center'>Cargando ...</p>
         </>
      ) : (
         <div>
            <HeaderComponent />
            <div className='w-full flex pl-[10%] pr-[10%] pt-9 flex-col'>
               <img src={PostImg} alt={post.titulo} className="rounded-lg mb-4 w-96 flex m-auto" />
               <h2 className='text-center w-full font-bold text-4xl text-yellow-600'>{post.titulo}</h2>
               <h3 className='text-2xl font-bold text-black mb-3'>Fecha: {post.fecha}</h3>
               <p className='text-xl'>{post.contenido}</p>
            </div>
         </div>
      )
   );

};

export default BlogDetailPage;
