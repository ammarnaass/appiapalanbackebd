"use client";

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import api from '@/lib/api';
import { useRouter } from 'next/navigation';

interface User {
    id: string;
    email: string;
    full_name?: string;
    role: string;
}

interface AuthContextType {
    user: User | null;
    loading: boolean;
    login: (token: string, userData: User) => void;
    logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);
    const router = useRouter();

    useEffect(() => {
        async function loadUser() {
            const token = localStorage.getItem('token');
            if (token) {
                try {
                    // Verify token or fetch user profile
                    const { data } = await api.post('/auth/test-token');
                    setUser(data);
                } catch (error) {
                    console.error("Failed to load user", error);
                    localStorage.removeItem('token');
                }
            }
            setLoading(false);
        }
        loadUser();
    }, []);

    const login = (token: string, userData: User) => {
        localStorage.setItem('token', token);
        setUser(userData);
        router.push('/dashboard');
    };

    const logout = () => {
        localStorage.removeItem('token');
        setUser(null);
        router.push('/login');
    };

    return (
        <AuthContext.Provider value={{ user, loading, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);
    if (context === undefined) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}
