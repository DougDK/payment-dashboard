"use client";

import { useState, useEffect } from "react";
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

const getSortFilteredData = (filter: (transaction: Transaction) => boolean) => {
  return transactions
    .sort((a: Transaction, b: Transaction) => {
      return (
        new Date(a.purchase_date).getTime() -
        new Date(b.purchase_date).getTime()
      );
    })
    .filter(filter);
};

export default function DataManager({ sendOrderedFilteredData }: any) {
  const sortedUniqueAges = Array.from(
    new Set(transactions.map((transaction: Transaction) => transaction.age))
  ).sort((a, b) => a - b);
  const [selectedAge, setSelectedAge] = useState(0);

  const sortedUniqueCustomer = Array.from(
    new Set(transactions.map((transaction: Transaction) => transaction.email))
  ).sort();
  const [selectedCustomer, setSelectedCustomer] = useState("");

  const [filterSelector, setFilterSelector] = useState("age");

  useEffect(() => {
    const fetchData = async () => {
      const filtered = getSortFilteredData(() => true);
      sendOrderedFilteredData(filtered);
    };

    fetchData();
  }, []);

  const onFilterChange = (e: any) => {
    const { name, value } = e.target;
    if (name == "age") {
      setSelectedAge(value);
      const filter =
        value == 0
          ? () => true
          : (transaction: Transaction) => transaction.age == value;
      const filtered = getSortFilteredData(filter);
      sendOrderedFilteredData(filtered);
    } else if (name == "customer") {
      setSelectedCustomer(value);
      const filter =
        value == 0
          ? () => true
          : (transaction: Transaction) => transaction.email == value;
      const filtered = getSortFilteredData(filter);
      sendOrderedFilteredData(filtered);
    }
  };

  const onFilterSelectorChange = (e: any) => {
    setFilterSelector(e.target.value)
    if (e.target.value == "age") {
      const filter =
        selectedAge == 0
          ? () => true
          : (transaction: Transaction) => transaction.age == selectedAge;
      const filtered = getSortFilteredData(filter);
      sendOrderedFilteredData(filtered);
    } else if (e.target.value == "customer") {
      const filter =
        selectedCustomer == ""
          ? () => true
          : (transaction: Transaction) => transaction.email == selectedCustomer;
      const filtered = getSortFilteredData(filter);
      sendOrderedFilteredData(filtered);
    }
  }

  return (
    <div className="flex gap-[16px] m-[16px]">
      <label className="">
        <div className="">Filter by:</div>
        <select
          name="filterSelector"
          value={filterSelector}
          onChange={(event) => onFilterSelectorChange(event)}
        >
          <option value="age">Age</option>
          <option value="customer">Customer</option>
        </select>
      </label>
      {filterSelector == "age" ? (
        <label className="">
          <div className="">Age:</div>
          <select
            name="age"
            value={selectedAge}
            onChange={(event) => onFilterChange(event)}
          >
            <option value={0}>All</option>
            {sortedUniqueAges.map((item, index) => (
              <option key={index} value={item}>
                {item}
              </option>
            ))}
          </select>
        </label>
      ) : (
        <></>
      )}
      {filterSelector == "customer" ? (
        <label className="">
          <div className="">Customer:</div>
          <select
            name="customer"
            value={selectedCustomer}
            onChange={(event) => onFilterChange(event)}
          >
            <option value={""}>All</option>
            {sortedUniqueCustomer.map((item, index) => (
              <option key={index} value={item}>
                {item}
              </option>
            ))}
          </select>
        </label>
      ) : (
        <></>
      )}
    </div>
  );
}
