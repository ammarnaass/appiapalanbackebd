"use client";

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import {
    LayoutDashboard,
    Users,
    Settings,
    LogOut,
    Sprout,
    ShieldAlert,
    ChevronRight,
    FileText
} from 'lucide-react';
import { useAuth } from '@/context/AuthContext';

const menuItems = [
    { name: 'Dashboard', href: '/dashboard', icon: LayoutDashboard },
    { name: 'Content', href: '/dashboard/content', icon: FileText },
    { name: 'Plants', href: '/dashboard/plants', icon: Sprout },
    { name: 'Diseases', href: '/dashboard/diseases', icon: ShieldAlert },
    { name: 'Users', href: '/dashboard/users', icon: Users },
    { name: 'Settings', href: '/dashboard/settings', icon: Settings },
];

export default function Sidebar() {
    const pathname = usePathname();
    const { logout } = useAuth();

    return (
        <div className="flex flex-col h-screen w-64 bg-gray-900 text-white transition-all duration-300">
            <div className="flex items-center justify-center h-20 shadow-md">
                <h1 className="text-2xl font-bold text-indigo-500 italic">AppiaPalan</h1>
            </div>
            <ul className="flex flex-col py-4 flex-grow">
                {menuItems.map((item) => {
                    const isActive = pathname === item.href || pathname.startsWith(item.href + '/');
                    return (
                        <li key={item.name}>
                            <Link
                                href={item.href}
                                className={`flex flex-row items-center h-12 transform hover:translate-x-2 transition-transform ease-in duration-200 text-gray-400 hover:text-white ${isActive ? 'bg-gray-800 text-indigo-400 border-r-4 border-indigo-500' : ''
                                    }`}
                            >
                                <span className="inline-flex items-center justify-center h-12 w-12 text-lg text-gray-400">
                                    <item.icon size={20} />
                                </span>
                                <span className="text-sm font-medium">{item.name}</span>
                                {isActive && <ChevronRight className="ml-auto mr-2" size={16} />}
                            </Link>
                        </li>
                    );
                })}
            </ul>
            <div className="p-4 border-t border-gray-800">
                <button
                    onClick={logout}
                    className="flex flex-row items-center h-12 w-full text-gray-400 hover:text-red-400 transition-colors duration-200"
                >
                    <span className="inline-flex items-center justify-center h-12 w-12 text-lg">
                        <LogOut size={20} />
                    </span>
                    <span className="text-sm font-medium">Logout</span>
                </button>
            </div>
        </div>
    );
}
