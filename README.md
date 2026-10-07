# Smart Inventory & Billing System

A Python and PostgreSQL-based inventory and billing management system designed to manage products, customers, inventory stock, and sales transactions.

## 🚀 Features

- Product management
- Customer management
- Inventory and stock tracking
- Sales management
- Billing and transaction management
- PostgreSQL database integration
- SQL-based data retrieval and management
- Python-PostgreSQL connectivity using psycopg2

## 🛠️ Tech Stack

- **Python**
- **PostgreSQL**
- **SQL**
- **psycopg2**
- **python-dotenv**

## 🗄️ Database Design

The system uses a relational PostgreSQL database named `ecommerce`.

### Main Tables

| Table | Description |
|---|---|
| `customers` | Stores customer information |
| `products` | Stores product details, pricing, and stock quantity |
| `sales` | Stores sales transactions |
| `sale_items` | Stores individual products included in each sale |

### Database Structure

```text
ecommerce
│
├── customers
│
├── products
│
├── sales
│
└── sale_items