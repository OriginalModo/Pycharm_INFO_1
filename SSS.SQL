Таблицы:
users (пользователи):
	id (INT, PRIMARY KEY)
	name (VARCHAR)
	email (VARCHAR)
	registration_date (DATE)

products (продукты):
	id (INT, PRIMARY KEY)
	name (VARCHAR)
	category (VARCHAR)
	price (DECIMAL)

orders (заказы):
	id (INT, PRIMARY KEY)
	user_id (INT, FOREIGN KEY на users.id)
	product_id (INT, FOREIGN KEY на products.id)
	order_date (DATE)
	quantity (INT)


select u.name from users as u
left join products as p on u.if = p.id


