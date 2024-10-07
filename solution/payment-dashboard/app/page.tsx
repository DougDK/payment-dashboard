"use client";

import { useState } from "react";
import LineChart from "@/components/linechart";
import BarChart from "@/components/barchart";
import DataManager from "@/components/datamanager";

interface Product {
  product_id: number;
  product_name: string;
  category: string;
  quantity: number;
  price: number;
}

interface Transaction {
  transaction_id: string;
  customer_name: string;
  email: string;
  age: number;
  purchase_date: string;
  products: Product[];
  payment_method: string;
  currency: string;
  status: string;
  total_amount: number;
}

interface Reduced {
  [key: string]: {transactions: number, products: number}
}

// Transform a Transaction into Reduced which is easilly delt by the charts
const reduceTransaction = (
  transactions: Transaction[]
) => {
  const result = transactions
    .reduce((acc: Reduced, transaction: Transaction) => {
      const date = transaction.purchase_date;
      if (!acc[date]) {
        acc[date] = { transactions: 0, products: 0 };
      }
      acc[date] = {
        transactions: acc[date].transactions + 1,
        products: acc[date].products + transaction.products.length,
      };
      return acc;
    }, {});
  return result;
};

export default function Home() {
  const [lineData, setLineData] = useState({
    labels: [""],
    datasets: [
      {
        data: [0.0],
      },
    ],
  });
  const [barData, setBarData] = useState({
    labels: [""],
    datasets: [
      {
        data: [0.0],
      },
    ],
  });
  const [numberOfTransactions, setNumberOfTransactions] = useState(0);

  const handleData = (orderedFilteredData: Transaction[]) => {
    const resultData:Reduced = reduceTransaction(orderedFilteredData);
    setLineData({
      labels: Object.keys(resultData),
      datasets: [
        {
          data: Object.values(resultData).map(item => item.transactions),
        },
      ],
    });
    setBarData({
      labels: Object.keys(resultData),
      datasets: [
        {
          data: Object.values(resultData).map(item => item.transactions),
        },
      ],
    });
    setNumberOfTransactions(orderedFilteredData.length);
  };

  return (
    <>
      <div>Transactions: {numberOfTransactions}</div>
      <DataManager sendOrderedFilteredData={handleData} />
      <LineChart data={lineData} />
      <BarChart data={barData} />
    </>
  );
}
