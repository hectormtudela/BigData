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


