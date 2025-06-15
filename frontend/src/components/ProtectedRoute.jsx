// import { Navigate } from "react-router-dom";
// import useAuthStore from "../store/auth";

// export default function ProtectedRoute({ children }) {
//   const token = useAuthStore((s) => s.token);
//   if (!token) return <Navigate to="/" replace />;
//   return children;
// }


import { Navigate } from "react-router-dom";

export default function ProtectedRoute({ token, children }) {
  if (!token) {
    return <Navigate to="/" replace />;
  }
  return children;
}
