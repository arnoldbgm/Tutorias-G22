import { BrowserRouter, Routes, Route } from "react-router-dom";
import { LoginPage, RegisterPage, NotFoundPage, HomePage } from "../pages";
import PrivateRoutes from "../utils/PrivateRoutes";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route>
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="*" element={<NotFoundPage />} />
          <Route element={<PrivateRoutes />}>
            <Route path="/home" element={<HomePage />} />
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
