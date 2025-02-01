import { BrowserRouter, Routes, Route } from "react-router-dom";
import { BlogDetailPage, BlogPage, HomePage, NotFoundPage } from "../pages";

const CustomRouter = () => {
   return (
      <BrowserRouter>
         <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/blog" element={<BlogPage />} />
            <Route path="/blog/:id" element={<BlogDetailPage/>} />
            <Route path="*" element={<NotFoundPage />} />
         </Routes>
      </BrowserRouter>
   )
}

export default CustomRouter

