import { AuthProvider, useAuth } from './contexts/AuthContext'
import AdminDashboard from './pages/AdminDashboard'
import Login from './components/Login'

function AppContent() {
  const { isAuthenticated } = useAuth();
  
  return isAuthenticated ? <AdminDashboard /> : <Login />;
}

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}

export default App
