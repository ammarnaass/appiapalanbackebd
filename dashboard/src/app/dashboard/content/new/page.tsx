"use client";

import axios from 'axios';
import { useState } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import api from '@/lib/api';
import { Save, ArrowLeft } from 'lucide-react';
import Link from 'next/link';

export default function NewContentPage() {
    const router = useRouter();
    const searchParams = useSearchParams();
    const typeKey = searchParams.get('type') || 'home_banners';

    const [title, setTitle] = useState('');
    const [data, setData] = useState('{}'); // JSON string for simplicity in demo
    const [isPublished, setIsPublished] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const jsonData = JSON.parse(data);
            await api.post('/content/', {
                title,
                type_key: typeKey,
                data: jsonData,
                is_published: isPublished
            });
            router.push('/dashboard/content');
        } catch (err: unknown) {
            console.error(err);
            if (axios.isAxiosError(err)) {
                setError(err.response?.data?.detail || err.message || 'Failed to create content.');
            } else {
                setError('Failed to create content. Ensure JSON is valid.');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-white rounded-lg shadow-sm border p-6 max-w-2xl mx-auto">
            <div className="flex items-center gap-4 mb-6">
                <Link href="/dashboard/content" className="text-gray-500 hover:text-gray-700">
                    <ArrowLeft size={20} />
                </Link>
                <h1 className="text-2xl font-bold text-gray-800">New {typeKey} Entry</h1>
            </div>

            <form onSubmit={handleSubmit} className="space-y-6">
                {error && (
                    <div className="bg-red-50 text-red-500 p-3 rounded text-sm text-center">
                        {error}
                    </div>
                )}

                <div>
                    <label className="block text-sm font-medium text-gray-700">Title</label>
                    <input
                        type="text"
                        required
                        className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700">Data (JSON)</label>
                    <textarea
                        required
                        rows={10}
                        className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm font-mono text-sm focus:ring-indigo-500 focus:border-indigo-500"
                        value={data}
                        onChange={(e) => setData(e.target.value)}
                        placeholder='{ "image_url": "...", "link": "..." }'
                    />
                </div>

                <div className="flex items-center">
                    <input
                        id="publish"
                        type="checkbox"
                        className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                        checked={isPublished}
                        onChange={(e) => setIsPublished(e.target.checked)}
                    />
                    <label htmlFor="publish" className="ml-2 block text-sm text-gray-900">
                        Publish immediately
                    </label>
                </div>

                <div className="flex justify-end pt-4">
                    <button
                        type="submit"
                        disabled={loading}
                        className="flex items-center px-6 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 transition disabled:bg-indigo-300"
                    >
                        <Save size={18} className="mr-2" />
                        {loading ? 'Saving...' : 'Save Content'}
                    </button>
                </div>
            </form>
        </div>
    );
}
