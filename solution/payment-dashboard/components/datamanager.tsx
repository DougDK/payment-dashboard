"use client";

import { useState } from "react";
import transactionsData from "../data/transactions.json";
const transactions: Transaction[] = transactionsData as Transaction[];

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

export default function DataManager({sendOrderedFilteredData}: any) {
  const sortedUniqueAges = Array.from(
    new Set(transactions.map((transaction: Transaction) => transaction.age))
  ).sort((a, b) => a - b);
  const [selectedAge, setSelectedAge] = useState(0);

  const sortedUniqueCustomer = Array.from(
    new Set(transactions.map((transaction: Transaction) => transaction.email))
  ).sort();
  const [selectedCustomer, setSelectedCustomer] = useState("");

  const onFilterChange = (e: any) => {
    const { name, value } = e.target;
    if(name=="age"){
      setSelectedAge(value);
    } else if(name=="customer"){
      setSelectedCustomer(value);
    }
    const filtered = transactions
      .sort((a: Transaction, b: Transaction) => {
        return (
          new Date(a.purchase_date).getTime() -
          new Date(b.purchase_date).getTime()
        );
      })
      .filter((transaction: Transaction) => transaction.age==selectedAge && transaction.email==selectedCustomer)
      sendOrderedFilteredData(filtered);
  };
  return (
    <>
      <label className="">
        <div className="">Age:</div>
        <select
          name="age"
          value={selectedAge}
          onChange={(event) => onFilterChange(event)}
        >
          <option value={0}>None</option>
          {sortedUniqueAges.map((item, index) => (
            <option key={index} value={item}>
              {item}
            </option>
          ))}
        </select>
      </label>
      <label className="">
        <div className="">Customer:</div>
        <select
          name="customer"
          value={selectedCustomer}
          onChange={(event) => onFilterChange(event)}
        >
          <option value={""}>None</option>
          {sortedUniqueCustomer.map((item, index) => (
            <option key={index} value={item}>
              {item}
            </option>
          ))}
        </select>
      </label>
    </>
  );
}
