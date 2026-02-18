"use client";

import { useState, useEffect } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import axios from 'axios';
import api from '@/lib/api';
import { Save, ArrowLeft, ShieldAlert } from 'lucide-react';
import Link from 'next/link';

interface Plant {
    id: number;
    name_en: string;
    name_ar: string;
}

export default function NewDiseasePage() {
    const router = useRouter();
    const searchParams = useSearchParams();
    const initialPlantId = searchParams.get('plant_id') || '';

    const [plants, setPlants] = useState<Plant[]>([]);
    const [plantId, setPlantId] = useState(initialPlantId);
    const [nameEn, setNameEn] = useState('');
    const [nameAr, setNameAr] = useState('');
    const [symptoms, setSymptoms] = useState('');
    const [treatment, setTreatment] = useState('');

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    useEffect(() => {
        async function fetchPlants() {
            try {
                const { data } = await api.get('/agri/plants');
                setPlants(data);
            } catch {
                console.error("Failed to load plants for dropdown");
            }
        }
        fetchPlants();
    }, []);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            await api.post('/agri/diseases', {
                plant_id: parseInt(plantId),
                name_en: nameEn,
                name_ar: nameAr,
                symptoms,
                treatment
            });
            router.push(`/dashboard/diseases?plant_id=${plantId}`);
        } catch (err: unknown) {
            if (axios.isAxiosError(err)) {
                setError(err.response?.data?.detail || 'Failed to create disease');
            } else {
                setError('An unexpected error occurred');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-3xl mx-auto">
            <div className="flex items-center gap-4 mb-6">
                <Link href="/dashboard/diseases" className="p-2 hover:bg-gray-100 rounded-full transition">
                    <ArrowLeft size={20} className="text-gray-600" />
                </Link>
                <h1 className="text-2xl font-bold text-gray-800">New Disease Entry</h1>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-8">
                <form onSubmit={handleSubmit} className="space-y-6">
                    {error && (
                        <div className="bg-red-50 text-red-600 p-4 rounded-lg text-sm font-medium">
                            {error}
                        </div>
                    )}

                    <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-1">Host Plant</label>
                        <select
                            required
                            className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition bg-white"
                            value={plantId}
                            onChange={(e) => setPlantId(e.target.value)}
                        >
                            <option value="">Select a plant...</option>
                            {plants.map(p => (
                                <option key={p.id} value={p.id}>{p.name_en} ({p.name_ar})</option>
                            ))}
                        </select>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Disease Name (EN)</label>
                            <input
                                type="text"
                                required
                                placeholder="e.g. Late Blight"
                                className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition"
                                value={nameEn}
                                onChange={(e) => setNameEn(e.target.value)}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 mb-1 text-right">اسم المرض بالعربية</label>
                            <input
                                type="text"
                                required
                                dir="rtl"
                                placeholder="مثال: لفحة متأخرة"
                                className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition"
                                value={nameAr}
                                onChange={(e) => setNameAr(e.target.value)}
                            />
                        </div>
                    </div>

                    <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-1">Symptoms (Arabic & English)</label>
                        <textarea
                            rows={3}
                            required
                            placeholder="Yellowing of leaves, brown spots..."
                            className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition"
                            value={symptoms}
                            onChange={(e) => setSymptoms(e.target.value)}
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-semibold text-gray-700 mb-1">Treatment Protocol</label>
                        <textarea
                            rows={3}
                            required
                            placeholder="Recommended fungicide, pruning..."
                            className="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition"
                            value={treatment}
                            onChange={(e) => setTreatment(e.target.value)}
                        />
                    </div>

                    <div className="pt-4 flex items-center justify-between border-t border-gray-50">
                        <div className="flex items-center text-indigo-600 gap-2">
                            <ShieldAlert size={20} />
                            <span className="text-xs font-medium uppercase">Agronomy Intelligence</span>
                        </div>
                        <button
                            type="submit"
                            disabled={loading}
                            className="flex items-center px-8 py-2.5 bg-indigo-600 text-white font-bold rounded-lg hover:bg-indigo-700 transition disabled:bg-gray-300"
                        >
                            <Save size={18} className="mr-2" />
                            {loading ? 'Saving...' : 'Register Disease'}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}
