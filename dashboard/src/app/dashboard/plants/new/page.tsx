"use client";

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import axios from 'axios';
import api from '@/lib/api';
import { Save, ArrowLeft, Sprout } from 'lucide-react';
import Link from 'next/link';

export default function NewPlantPage() {
    const router = useRouter();
    const [nameEn, setNameEn] = useState('');
    const [nameAr, setNameAr] = useState('');
    const [scientificName, setScientificName] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            await api.post('/agri/plants', {
                name_en: nameEn,
                name_ar: nameAr,
                scientific_name: scientificName
            });
            router.push('/dashboard/plants');
        } catch (err: unknown) {
            if (axios.isAxiosError(err)) {
                setError(err.response?.data?.detail || 'Failed to create plant');
            } else {
                setError('An unexpected error occurred');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-2xl mx-auto">
            <div className="flex items-center gap-4 mb-6">
                <Link href="/dashboard/plants" className="p-2 hover:bg-gray-100 rounded-full transition">
                    <ArrowLeft size={20} className="text-gray-600" />
                </Link>
                <h1 className="text-2xl font-bold text-gray-800">Add New Plant Species</h1>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-8">
                <form onSubmit={handleSubmit} className="space-y-6">
                    {error && (
                        <div className="bg-red-50 text-red-600 p-4 rounded-lg text-sm font-medium">
                            {error}
                        </div>
                    )}

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 mb-1">English Name</label>
                            <input
                                type="text"
                                required
                                placeholder="e.g. Tomato"
                                className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none transition"
                                value={nameEn}
                                onChange={(e) => setNameEn(e.target.value)}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 mb-1 text-right">الاسم بالعربية</label>
                            <input
                                type="text"
                                required
                                dir="rtl"
                                placeholder="مثال: طماطم"
                                className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none transition"
                                value={nameAr}
                                onChange={(e) => setNameAr(e.target.value)}
                            />
                        </div>
                    </div>

                    <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-1">Scientific Name (Optional)</label>
                        <input
                            type="text"
                            placeholder="e.g. Solanum lycopersicum"
                            className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none transition italic font-serif"
                            value={scientificName}
                            onChange={(e) => setScientificName(e.target.value)}
                        />
                    </div>

                    <div className="pt-4 flex items-center justify-between border-t border-gray-50">
                        <div className="flex items-center text-green-600 gap-2">
                            <Sprout size={20} />
                            <span className="text-xs font-medium uppercase">Agriculture Asset</span>
                        </div>
                        <button
                            type="submit"
                            disabled={loading}
                            className="flex items-center px-8 py-2.5 bg-green-600 text-white font-bold rounded-lg hover:bg-green-700 transition disabled:bg-gray-300 shadow-sm shadow-green-200"
                        >
                            <Save size={18} className="mr-2" />
                            {loading ? 'Creating...' : 'Register Plant'}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}
