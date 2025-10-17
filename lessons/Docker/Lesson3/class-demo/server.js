const express = require("express");
const app = express();

// middleware to parse JSON
app.use(express.json());

// in-memory food data
let foods = [
  { id: 1, name: "Pizza", price: 25 },
  { id: 2, name: "Burger", price: 18 },
  { id: 3, name: "Pasta", price: 20 },
];

// get all foods
app.get("/foods", (req, res) => {
  res.json(foods);
});

// get one food by id
app.get("/foods/:id", (req, res) => {
  const food = foods.find((f) => f.id === parseInt(req.params.id));
  if (!food) return res.status(404).json({ message: "Food not found" });
  res.json(food);
});

// add new food
app.post("/foods", (req, res) => {
  const { name, price } = req.body;
  if (!name || !price)
    return res.status(400).json({ message: "Name and price required" });

  const newFood = { id: foods.length + 1, name, price };
  foods.push(newFood);
  res.status(201).json(newFood);
});

// update food
app.put("/foods/:id", (req, res) => {
  const food = foods.find((f) => f.id === parseInt(req.params.id));
  if (!food) return res.status(404).json({ message: "Food not found" });

  const { name, price } = req.body;
  if (name) food.name = name;
  if (price) food.price = price;

  res.json(food);
});

// delete food
app.delete("/foods/:id", (req, res) => {
  const index = foods.findIndex((f) => f.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ message: "Food not found" });

  const deleted = foods.splice(index, 1);
  res.json(deleted[0]);
});

// start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`🍔 Food API running on port ${PORT}`));
