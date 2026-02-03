import { createContext, useContext, useState, ReactNode } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => boolean;
  logout: () => void;
  isAuthenticated: boolean;
  isAdmin: boolean;
  users: User[];
  addUser: (user: Omit<User, 'id'>) => void;
  updateUser: (user: User) => void;
  deleteUser: (id: number) => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const [user, setUser] = useState<User | null>(null);
  const [users, setUsers] = useState<User[]>([
    { id: 1, name: 'Admin User', email: 'admin@example.com', role: 'admin' },
    { id: 2, name: 'John Doe', email: 'john@example.com', role: 'user' },
    { id: 3, name: 'Jane Smith', email: 'jane@example.com', role: 'user' },
    { id: 4, name: 'Kenneth Kosgei', email: 'kennethkosgei38@gmail.com', role: 'admin' },
  ]);

  const login = (email: string, password: string): boolean => {
    // Special admin credentials
    if (email === 'kennethkosgei38@gmail.com' && password === 'admin1234') {
      const adminUser = users.find(u => u.email === 'kennethkosgei38@gmail.com');
      if (adminUser) {
        setUser(adminUser);
        return true;
      }
    }
    
    // Regular users with password123
    const foundUser = users.find(u => u.email === email);
    if (foundUser && foundUser.email !== 'kennethkosgei38@gmail.com' && password === 'password123') {
      setUser(foundUser);
      return true;
    }
    
    return false;
  };

  const logout = () => {
    setUser(null);
  };

  const addUser = (newUser: Omit<User, 'id'>) => {
    const user: User = {
      ...newUser,
      id: Math.max(...users.map(u => u.id)) + 1
    };
    setUsers([...users, user]);
  };

  const updateUser = (updatedUser: User) => {
    setUsers(users.map(u => u.id === updatedUser.id ? updatedUser : u));
  };

  const deleteUser = (id: number) => {
    setUsers(users.filter(u => u.id !== id));
  };

  const value = {
    user,
    login,
    logout,
    isAuthenticated: !!user,
    isAdmin: user?.role === 'admin',
    users,
    addUser,
    updateUser,
    deleteUser
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};