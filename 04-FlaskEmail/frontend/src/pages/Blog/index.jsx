import React, { useEffect, useState } from 'react';
import { HeaderComponent, PostComponent } from '../../components';
import { fetchPosts } from '../../services/blogService';

const Blog = () => {
  const [posts, setPosts] = useState([]); // Estado para almacenar la lista de posts

  useEffect(() => {
    // Función comun de como hacer un fetch sin usar un servicio
    const fetchPosts = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/posts'); // Cambia esto a la URL de tu API
        if (!response.ok) {
          throw new Error('Error al obtener los datos');
        }
        return await response.json();
      } catch (error) {
        console.error('Error:', error);
      }
    };

    // Metodo usando un servicio
    const getPosts = async () => {
      try {
        const data = await fetchPosts();
        setPosts(data);
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    };

    getPosts();
  }, []);

  return (
    <div>
      <HeaderComponent />
      <div className='w-full flex pl-[10%] pr-[10%] pt-9 flex-col'>
        <h2 className='text-center w-full font-bold text-4xl text-yellow-600'>Lista de Blogs</h2>
        {/* Listado de los Blogs */}
        <div className='grid grid-cols-3 gap-4 mt-9'>
          {posts?.map((post) => (
            <PostComponent key={post.id} post={post} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Blog;
