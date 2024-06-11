/**
 * Creating a stocking and stockout engine.
 * With Redis.
 */

import { createClient } from 'redis';
import { promisify } from 'util';
import pkg from 'express';
const express = pkg;

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById (id) {
  const newList = listProducts.filter((obj) => obj.id === id);
  if (newList.length === 0) { return; }
  return newList[0];
}

const app = express();

app.get('/list_products', (req, res) => {
  const availableProducts = listProducts.map((obj) => {
    return { itemId: obj.id, itemName: obj.name, price: obj.price, initialAvailableQuantity: obj.stock };
  });
  res.json(availableProducts);
});

const client = createClient();

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

function reserveStockById (itemId, stock) {
  setAsync(`item.${itemId}`, stock)
    .then((data) => console.log(data));
}

reserveStockById(1, 4);
reserveStockById(2, 10);
reserveStockById(3, 2);
reserveStockById(4, 5);

async function getCurrentReservedStockById (itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(Number(req.params.itemId));
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  const reservedStock = await getCurrentReservedStockById(req.params.itemId);
  const availableProducts = [item].map((obj) => {
    return { itemId: obj.id, itemName: obj.name, price: obj.price, initialAvailableQuantity: obj.stock };
  });
  const availableProduct = availableProducts[0];
  availableProduct.currentQuantity = reservedStock;
  res.json(availableProduct);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(Number(req.params.itemId));
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  const stockAvailable = await getCurrentReservedStockById(item.id);
  if (stockAvailable < 1) {
    res.json({ status: 'Not enough stock available', itemId: item.id });
    return;
  }
  reserveStockById(item.id, stockAvailable - 1);
  res.json({ status: 'Reservation confirmed', itemId: item.id });
});

app.listen(1245, () => {
  console.log('running express server.');
});

// console.log(getItemById(1));
// console.log(getItemById(4));
// console.log("Expecting Nothing", getItemById(5));

// module.exports = { getItemById };
