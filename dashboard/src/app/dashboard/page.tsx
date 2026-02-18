"use client";

import {
    Sprout,
    ShieldAlert,
    FileText,
    Users,
    Activity,
    Clock
} from 'lucide-react';

export default function DashboardPage() {
    const stats = [
        { name: 'Total Plants', value: '12', icon: Sprout, color: 'bg-green-500' },
        { name: 'Active Diseases', value: '48', icon: ShieldAlert, color: 'bg-red-500' },
        { name: 'App Content', value: '24', icon: FileText, color: 'bg-blue-500' },
        { name: 'Total Users', value: '1,050', icon: Users, color: 'bg-indigo-500' },
    ];

    return (
        <div className="space-y-6">
            <header>
                <h1 className="text-2xl font-bold text-gray-800">Agricultural Insights</h1>
                <p className="text-gray-500">Overview of your plant disease detection ecosystem</p>
            </header>

            <div className="grid grid-cols-1 gap-6 mb-6 lg:grid-cols-4 sm:grid-cols-2">
                {stats.map((stat) => (
                    <div key={stat.name} className="flex items-center p-4 bg-white rounded-xl shadow-sm border border-gray-100">
                        <div className={`p-3 mr-4 text-white ${stat.color} rounded-lg`}>
                            <stat.icon size={24} />
                        </div>
                        <div>
                            <p className="text-xs font-medium text-gray-500 uppercase tracking-wider">{stat.name}</p>
                            <p className="text-xl font-bold text-gray-800">{stat.value}</p>
                        </div>
                    </div>
                ))}
            </div>

            <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
                <div className="p-6 bg-white rounded-xl shadow-sm border border-gray-100">
                    <div className="flex items-center justify-between mb-4">
                        <h2 className="text-lg font-semibold text-gray-800 flex items-center gap-2">
                            <Activity size={20} className="text-indigo-500" /> Recent Predictions
                        </h2>
                    </div>
                    <div className="space-y-4">
                        {[1, 2, 3].map((i) => (
                            <div key={i} className="flex items-center justify-between py-2 border-b border-gray-50 last:border-0">
                                <div className="flex items-center gap-3">
                                    <div className="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center text-gray-500">
                                        <Sprout size={18} />
                                    </div>
                                    <div>
                                        <p className="text-sm font-medium text-gray-800">Tomato Early Blight</p>
                                        <p className="text-xs text-gray-500">Prediction Log #{1024 + i}</p>
                                    </div>
                                </div>
                                <span className="text-xs font-medium text-green-600 bg-green-50 px-2 py-1 rounded">98% Conf</span>
                            </div>
                        ))}
                    </div>
                </div>

                <div className="p-6 bg-white rounded-xl shadow-sm border border-gray-100">
                    <div className="flex items-center justify-between mb-4">
                        <h2 className="text-lg font-semibold text-gray-800 flex items-center gap-2">
                            <Clock size={20} className="text-orange-500" /> Content Updates
                        </h2>
                    </div>
                    <div className="space-y-4">
                        {[1, 2, 3].map((i) => (
                            <div key={i} className="flex items-center justify-between py-2 border-b border-gray-50 last:border-0">
                                <div>
                                    <p className="text-sm font-medium text-gray-800">New Crop Added: &quot;Pepper&quot;</p>
                                    <p className="text-xs text-gray-500">2 hours ago by Admin</p>
                                </div>
                                <FileText size={16} className="text-gray-300" />
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}
