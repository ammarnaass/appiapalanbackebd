"use client";

import { useEffect, useState } from 'react';
import api from '@/lib/api';
import { Plus, Edit, Trash2, Globe, Lock } from 'lucide-react';
import Link from 'next/link';

interface Content {
    id: number;
    title: string;
    type_key: string;
    data: Record<string, unknown>;
    is_published: boolean;
    created_at: string;
}

export default function ContentListPage() {
    const [contents, setContents] = useState<Content[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    // For this demo, let's assume we are viewing 'home_banners' type
    // In a real app, this would be dynamic via a dropdown or route params
    const typeKey = 'home_banners';

    useEffect(() => {
        async function fetchContent() {
            try {
                const { data } = await api.get(`/content/${typeKey}`);
                setContents(data);
            } catch {
                setError('Failed to load content');
            } finally {
                setLoading(false);
            }
        }
        fetchContent();
    }, [typeKey]);

    return (
        <div className="bg-white rounded-lg shadow-sm border p-6">
            <div className="flex justify-between items-center mb-6">
                <div>
                    <h1 className="text-2xl font-bold text-gray-800">Content Management</h1>
                    <p className="text-gray-500 text-sm">Managing type: <span className="font-mono text-indigo-600">{typeKey}</span></p>
                </div>
                <Link
                    href={`/dashboard/content/new?type=${typeKey}`}
                    className="flex items-center px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 transition"
                >
                    <Plus size={18} className="mr-2" /> New Entry
                </Link>
            </div>

            {loading ? (
                <div className="text-center py-10 text-gray-400">Loading contents...</div>
            ) : error ? (
                <div className="text-center py-10 text-red-500">{error}</div>
            ) : contents.length === 0 ? (
                <div className="text-center py-10 text-gray-400 border-2 border-dashed rounded-lg">
                    No content found for this type. Start by creating one.
                </div>
            ) : (
                <div className="overflow-x-auto">
                    <table className="min-w-full leading-normal">
                        <thead>
                            <tr>
                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Title
                                </th>
                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Status
                                </th>
                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Created At
                                </th>
                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-right text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Actions
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            {contents.map((item) => (
                                <tr key={item.id}>
                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                                        <p className="text-gray-900 whitespace-no-wrap font-medium">{item.title}</p>
                                    </td>
                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                                        <span className={`relative inline-block px-3 py-1 font-semibold leading-tight ${item.is_published ? 'text-green-900' : 'text-orange-900'
                                            }`}>
                                            <span aria-hidden className={`absolute inset-0 opacity-50 rounded-full ${item.is_published ? 'bg-green-200' : 'bg-orange-200'
                                                }`}></span>
                                            <span className="relative flex items-center gap-1">
                                                {item.is_published ? <Globe size={12} /> : <Lock size={12} />}
                                                {item.is_published ? 'Published' : 'Draft'}
                                            </span>
                                        </span>
                                    </td>
                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm">
                                        <p className="text-gray-900 whitespace-no-wrap">
                                            {new Date(item.created_at).toLocaleDateString()}
                                        </p>
                                    </td>
                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-sm text-right">
                                        <div className="flex justify-end gap-2">
                                            <button className="text-indigo-600 hover:text-indigo-900 p-1">
                                                <Edit size={18} />
                                            </button>
                                            <button className="text-red-600 hover:text-red-900 p-1">
                                                <Trash2 size={18} />
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}
