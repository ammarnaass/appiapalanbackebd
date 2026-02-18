"use client";

import { useEffect, useState } from 'react';
import api from '@/lib/api';
import { Plus, Edit, Trash2, ShieldAlert } from 'lucide-react';
import Link from 'next/link';
import { useSearchParams } from 'next/navigation';

interface Disease {
    id: number;
    name_en: string;
    name_ar: string;
    symptoms: string;
    treatment: string;
}

export default function DiseasesPage() {
    const searchParams = useSearchParams();
    const plantId = searchParams.get('plant_id');

    const [diseases, setDiseases] = useState<Disease[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        async function fetchDiseases() {
            try {
                const url = plantId ? `/agri/diseases?plant_id=${plantId}` : '/agri/diseases';
                const { data } = await api.get(url);
                setDiseases(data);
            } catch {
                setError('Failed to load diseases');
            } finally {
                setLoading(false);
            }
        }
        fetchDiseases();
    }, [plantId]);

    return (
        <div className="bg-white rounded-lg shadow-sm border p-6">
            <div className="flex justify-between items-center mb-6">
                <div>
                    <h1 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
                        <ShieldAlert className="text-red-600" /> Disease Encyclopedia
                    </h1>
                    <p className="text-gray-500 text-sm">Managing diagnosis and treatments</p>
                </div>
                <Link
                    href={`/dashboard/diseases/new${plantId ? `?plant_id=${plantId}` : ''}`}
                    className="flex items-center px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700 transition"
                >
                    <Plus size={18} className="mr-2" /> Add Disease
                </Link>
            </div>

            {loading ? (
                <div className="text-center py-10 text-gray-400">Loading diseases...</div>
            ) : error ? (
                <div className="text-center py-10 text-red-500">{error}</div>
            ) : diseases.length === 0 ? (
                <div className="text-center py-10 text-gray-400 border-2 border-dashed rounded-lg">
                    No diseases found.
                </div>
            ) : (
                <div className="space-y-4">
                    {diseases.map((disease) => (
                        <div key={disease.id} className="border rounded-lg p-5 hover:bg-gray-50 transition">
                            <div className="flex justify-between items-start mb-3">
                                <div>
                                    <h3 className="text-xl font-bold text-gray-900">{disease.name_en}</h3>
                                    <p className="text-sm text-red-600 font-bold">{disease.name_ar}</p>
                                </div>
                                <div className="flex gap-2">
                                    <button className="bg-white border rounded p-2 text-gray-600 hover:text-indigo-600"><Edit size={18} /></button>
                                    <button className="bg-white border rounded p-2 text-gray-600 hover:text-red-600"><Trash2 size={18} /></button>
                                </div>
                            </div>

                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 text-sm">
                                <div className="bg-orange-50 p-3 rounded-md">
                                    <h4 className="font-bold text-orange-800 mb-1">Symptoms (الأعراض)</h4>
                                    <p className="text-orange-900">{disease.symptoms || 'N/A'}</p>
                                </div>
                                <div className="bg-green-50 p-3 rounded-md">
                                    <h4 className="font-bold text-green-800 mb-1">Treatment (العلاج)</h4>
                                    <p className="text-green-900">{disease.treatment || 'N/A'}</p>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}
