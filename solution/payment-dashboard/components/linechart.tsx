"use client";

import { Line } from "react-chartjs-2";
import type { ChartOptions } from "chart.js";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const options: ChartOptions<"line"> = {
    responsive: true,
    scales: {},
    plugins: {
      tooltip: {},
      legend: {},
    },
  };

export default function LineChart({data}:any) {
  return <Line data={data} options={options} />;
}