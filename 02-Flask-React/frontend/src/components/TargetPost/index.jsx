import { Link } from 'react-router-dom';
import PostImg from "../../assets/post_bg.jpg"

const TargetPost = ({ post }) => {
  return (
    <div>
      <img src={PostImg} alt={post.title} className="rounded-lg mb-4" />
      <h2 className='text-3xl font-bold mb-3'>{post.titulo}</h2>
      <h3 className='text-2xl font-bold text-yellow-600 mb-3'>Fecha: {post.fecha}</h3>
      <p className='line-clamp-3 text-xl'>{post.contenido}</p>
      <Link to={`/blog/${post.id}`}>
        <button type="button" className="w-full mt-3 text-white bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-full text-base px-5 py-2.5 me-2 mb-2 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700">
          Ver más
        </button>
      </Link>
    </div>
  );
};

export default TargetPost;