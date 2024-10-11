"use client";

import { Bar } from "react-chartjs-2";
import type { ChartOptions } from "chart.js";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const options: ChartOptions<"bar"> = {
  responsive: true,
  plugins: {
    legend: {
      position: "top", // Position of the legend
    },
  },
  scales: {
    y: {
      beginAtZero: true, // Start Y-axis from 0
    },
  },
};

export default function BarChart({ data }: any) {
  return <Bar data={data} options={options} />;
}
