"use client";

import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import Sidebar from '@/components/Sidebar';

export default function DashboardLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    const { user, loading } = useAuth();
    const router = useRouter();

    useEffect(() => {
        if (!loading && !user) {
            router.push('/login');
        }
    }, [user, loading, router]);

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-screen bg-gray-100">
                <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-indigo-500"></div>
            </div>
        );
    }

    if (!user) {
        return null;
    }

    return (
        <div className="flex h-screen bg-gray-100">
            <Sidebar />
            <div className="flex flex-col flex-1 overflow-hidden">
                <header className="flex items-center justify-between px-6 py-4 bg-white border-b-4 border-indigo-600">
                    <div className="flex items-center">
                        <h2 className="text-xl font-semibold text-gray-800">
                            Welcome back, <span className="text-indigo-600">{user.full_name || user.email}</span>
                        </h2>
                    </div>
                    <div className="flex items-center">
                        <div className="relative inline-block text-left">
                            <span className="bg-indigo-100 text-indigo-800 text-xs font-semibold px-2.5 py-0.5 rounded uppercase">
                                {user.role}
                            </span>
                        </div>
                    </div>
                </header>

                <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-200 p-6">
                    {children}
                </main>
            </div>
        </div>
    );
}
