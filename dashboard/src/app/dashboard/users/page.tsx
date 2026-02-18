"use client";

import { Users, ShieldAlert } from 'lucide-react';

export default function UserManagementPage() {
    return (
        <div className="bg-white rounded-lg shadow-sm border p-6">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
                    <Users size={24} className="text-indigo-600" /> User Management
                </h1>
            </div>

            <div className="flex flex-col items-center justify-center py-20 bg-gray-50 rounded-lg border-2 border-dashed">
                <ShieldAlert size={48} className="text-gray-300 mb-4" />
                <p className="text-gray-500 font-medium">RBAC & User Management is restricted</p>
                <p className="text-gray-400 text-sm mt-1">Only Super Admins can manage internal accounts and permissions.</p>
                <button className="mt-6 px-4 py-2 bg-gray-200 text-gray-700 rounded cursor-not-allowed text-sm">
                    Request Access
                </button>
            </div>

            <div className="mt-8">
                <h3 className="text-lg font-semibold text-gray-700 mb-4">Internal Staff</h3>
                <ul className="space-y-4">
                    <li className="flex items-center justify-between p-4 bg-white border rounded">
                        <div className="flex items-center gap-3">
                            <div className="h-10 w-10 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 font-bold">A</div>
                            <div>
                                <p className="font-medium text-gray-900">Admin User</p>
                                <p className="text-xs text-gray-500">admin@example.com</p>
                            </div>
                        </div>
                        <span className="bg-indigo-100 text-indigo-800 text-xs px-2 py-1 rounded">SUPER_ADMIN</span>
                    </li>
                </ul>
            </div>
        </div>
    );
}
