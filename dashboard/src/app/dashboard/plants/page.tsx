"use client";

import { useEffect, useState } from 'react';
import api from '@/lib/api';
import { Plus, Edit, Trash2, Sprout } from 'lucide-react';
import Link from 'next/link';

interface Plant {
    id: number;
    name_en: string;
    name_ar: string;
    scientific_name?: string;
}

export default function PlantsPage() {
    const [plants, setPlants] = useState<Plant[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        async function fetchPlants() {
            try {
                const { data } = await api.get('/agri/plants');
                setPlants(data);
            } catch {
                setError('Failed to load plants');
            } finally {
                setLoading(false);
            }
        }
        fetchPlants();
    }, []);

    return (
        <div className="bg-white rounded-lg shadow-sm border p-6">
            <div className="flex justify-between items-center mb-6">
                <div>
                    <h1 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
                        <Sprout className="text-green-600" /> Plants Catalog
                    </h1>
                    <p className="text-gray-500 text-sm">Managing supported crop species</p>
                </div>
                <Link
                    href="/dashboard/plants/new"
                    className="flex items-center px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700 transition"
                >
                    <Plus size={18} className="mr-2" /> Add Plant
                </Link>
            </div>

            {loading ? (
                <div className="text-center py-10 text-gray-400">Loading plants...</div>
            ) : error ? (
                <div className="text-center py-10 text-red-500">{error}</div>
            ) : plants.length === 0 ? (
                <div className="text-center py-10 text-gray-400 border-2 border-dashed rounded-lg">
                    No plants found.
                </div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {plants.map((plant) => (
                        <div key={plant.id} className="border rounded-lg p-4 hover:shadow-md transition">
                            <div className="flex justify-between items-start mb-2">
                                <div>
                                    <h3 className="text-lg font-bold text-gray-900">{plant.name_en}</h3>
                                    <p className="text-sm text-green-600 font-medium">{plant.name_ar}</p>
                                </div>
                                <div className="flex gap-1">
                                    <button className="text-gray-400 hover:text-indigo-600 p-1"><Edit size={16} /></button>
                                    <button className="text-gray-400 hover:text-red-600 p-1"><Trash2 size={16} /></button>
                                </div>
                            </div>
                            <p className="text-xs text-gray-500 italic mt-2">{plant.scientific_name}</p>
                            <div className="mt-4 pt-4 border-t flex justify-between items-center">
                                <Link href={`/dashboard/diseases?plant_id=${plant.id}`} className="text-xs text-indigo-600 hover:underline">
                                    View Diseases
                                </Link>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}
