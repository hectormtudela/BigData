## Pregunta  — 

**Enunciado:** 

```sql

```
**Resultado:**
![Resultado prueba](images/prueba.png)

**Comentario:**  


---

## Pregunta 1 — Catálogo comercial activo

**Enunciado:** Obtén los productos que no están descatalogados y cuyo precio unitario esté entre 10 y 50 euros, ambos incluidos. Muestra el nombre del producto y su precio redondeado a dos decimales, ordenado de mayor a menor precio.

```sql
-- Productos activos con precio entre 10 y 50, de mayor a menor precio
SELECT product_name AS producto, ROUND(unit_price::numeric, 2) AS precio
FROM products
WHERE discontinued = 0 AND unit_price BETWEEN 10 AND 50
ORDER BY precio DESC;
```
**Resultado:**
![Resultado ej1](images/ejercicio1.png)

**Comentario:** He usado ``::numeric`` porque unit_price no es un tipo de valor que pueda usarse en ROUND() y porque se pide en las especificaciones del proyecto. 


---

## Pregunta 2 — Concentración geográfica de la cartera



**Enunciado:** Dirección quiere saber en qué mercados está realmente concentrada la base de clientes antes de decidir dónde abrir delegación. Cuenta cuántos clientes hay en cada país y muestra únicamente aquellos países con **5 o más clientes**, ordenados de mayor a menor. Indica también cuántas ciudades distintas hay en cada uno de esos países.

```sql
-- Países con 5 o más clientes, con su número de ciudades distintas
SELECT country AS pais, COUNT(*) AS num_clientes, COUNT(DISTINCT city) AS num_ciudades
FROM customers
GROUP BY country
HAVING COUNT(*) >= 5
ORDER BY num_clientes DESC, pais;
```

**Resultado:**
![Resultado ej2](images/ejercicio2.png)

**Comentario:** Uso ``Having`` porque estoy filtrando filas después de haber agrupado los datos con ``GROUP BY``.

---

## Pregunta 3 — Alerta de reposición

**Enunciado:** Productos activos con stock inferior o igual a su nivel de reposición, con una columna que diga 'CRÍTICO' si el stock es 0 y 'AVISO' en el resto.

```sql
-- Productos activos con stock igual o inferior al nivel de reposición
SELECT product_name AS producto, units_in_stock AS stock, reorder_level AS nivel_reposicion,
       units_on_order AS pedido,
       CASE
           WHEN units_in_stock = 0 THEN 'CRÍTICO'
           ELSE 'AVISO'
       END AS situacion
FROM products
WHERE discontinued = 0
  AND units_in_stock <= reorder_level
ORDER BY units_in_stock, product_name;
```

**Resultado:**
![Resultado prueba](images/ejercicio3.png)

**Comentario:** Usé CASE WHEN para decidir el texto entre "Crítico" y "Aviso" 


---

## Pregunta 4  — Ficha completa de producto


**Enunciado:** Para los productos suministrados por empresas de Italia, Francia o España, muestra producto, categoría, proveedor, país y ciudad, ordenados por país y producto.


```sql
-- Productos de proveedores de Italia, Francia o España con categoría y proveedor
SELECT products.product_name AS producto,
       categories.category_name AS categoria,
       suppliers.company_name AS proveedor,
       suppliers.country AS pais,
       suppliers.city AS ciudad
FROM products 
INNER JOIN categories ON categories.category_id = products.category_id
INNER JOIN suppliers ON suppliers.supplier_id = products.supplier_id
WHERE suppliers.country IN ('Italy', 'France', 'Spain')
ORDER BY suppliers.country, products.product_name;
```
**Resultado:**
![Resultado prueba](images/ejercicio4.png)

**Comentario:** Unión de tablas mediante ``INNER JOIN`` para poder hacer ``IN`` sobre los países necesarios en la tabla ``suppliers``

---

## Pregunta 5 — Detalle valorizado de un pedido

**Enunciado:** Reconstruye la factura del pedido 10248 línea a línea: producto, precio, cantidad, descuento e importe, con el nombre del cliente y la fecha.

```sql
-- Detalles del pedido 10248
SELECT customers.company_name AS cliente, orders.order_date AS fecha_pedido,products.product_name AS producto,
       ROUND(order_details.unit_price::numeric, 2) AS precio_unitario, order_details.quantity AS cantidad,
       ROUND(order_details.discount::numeric, 2) AS descuento, ROUND((order_details.unit_price::numeric) * order_details.quantity * (1 - order_details.discount::numeric), 2) AS importe_linea
FROM orders
INNER JOIN order_details USING (order_id)
INNER JOIN products USING (product_id)
INNER JOIN customers USING (customer_id)
WHERE orders.order_id = 10248
ORDER BY products.product_name;
```
**Resultado:**
![Resultado prueba](images/ejercicio5.png)

**Comentario:** Uso de ``USING`` porque las tablas comparten el nombre de columna de sus ids y si no se usase aparecerían duplicadas.

---

## Pregunta 6 — Ranking de categorías por facturación

**Enunciado:** Facturacion totl por categoría, con número de líneas y de productos distintos vendidos. Solo las categorías con más de 100000 euros.


```sql
-- Facturación por categoría, solo las que superan 100.000 euros
SELECT categories.category_name AS categoria,
       COUNT(*) AS num_lineas,
       COUNT(DISTINCT products.product_id) AS num_productos,
       ROUND(SUM((order_details.unit_price::numeric) * order_details.quantity * (1 - order_details.discount::numeric)), 2) AS facturacion
FROM order_details
INNER JOIN products ON products.product_id = order_details.product_id
INNER JOIN categories ON categories.category_id = products.category_id
GROUP BY categories.category_name
HAVING SUM((order_details.unit_price::numeric) * order_details.quantity * (1 - order_details.discount::numeric)) > 100000
ORDER BY facturacion DESC;
```
**Resultado:**
![Resultado prueba](images/prueba.png)

**Comentario:** En el ``HAVING`` repito la expresión completa del ``SUM()`` porque no le puedo hacer llamada por su nombre


---


