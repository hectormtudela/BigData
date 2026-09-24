# Práctica 06 - Servicios de Azure para DB SQL y NoSQL

## Ejercicio 2: Exploración de Azure Storage (datos no relacionales)

**Referencia:** [DP-900 Lab - Explore Azure Storage](https://microsoftlearning.github.io/DP-900T00A-Azure-Data-Fundamentals/Instructions/Labs/dp900-02-storage-lab.html)

**Objetivo:** Crear una cuenta de Azure Storage y explorar sus servicios principales de datos no relacionales:
- **Blob storage**: almacenamiento de archivos (imágenes, documentos, JSON, etc.)
- **Data Lake Storage Gen2**: blob storage con carpetas reales (jerárquicas), orientado a analítica big data.
- **Azure Files**: recursos compartidos de archivos en la nube, tipo unidad de red.

---

## 1. Aprovisionar la cuenta de Azure Storage

Pasos:
1. Acceder al [Azure portal](https://portal.azure.com).
2. **+ Crear un recurso** → buscar `Storage account` → **Create**.
3. Pestaña **Basics**:
   - **Subscription**: mi suscripción.
   - **Resource group**: reutilizar/crear `dp900-lab-rg`.
   - **Storage account name**: nombre único, solo minúsculas y números.
   - **Region**: la más cercana disponible.
   - **Performance**: Standard
   - **Redundancy**: Locally-redundant storage (LRS)
![Captura Basics](image.png)
4. Pestaña **Advanced**: dejar **Enable hierarchical namespace** sin marcar (se activará más adelante).
![Captura advanced](image-1.png)
5. Pestaña **Data protection**: desmarcar las tres opciones de **Enable soft delete...**.
![Captura protección de datos](image-2.png)
6. Resto de pestañas: valores por defecto.
7. **Review + create** → **Create** → esperar despliegue → **Go to resource**.
![Captura review](image-3.png)
![Captura creacion](image-4.png)
---

## 2. Explorar Blob Storage

Pasos:
1. Descargar [product1.json](https://aka.ms/product1.json) al equipo.
2. En el storage account → **Data storage** → **Containers** → **+ Add container** → nombre `data` (acceso privado, no se puede cambiar por defecto).
![Data creado](image-5.png)
3. Ir a **Storage browser** → **Blob containers** → abrir `data` (vacío).
![Data vacío](image-6.png)
4. **+ Add Directory** → crear carpeta `products`.
5. Comprobar que al volver al contenedor `data`, la carpeta `products` **no existe realmente** (las carpetas en blob storage son virtuales, solo existen si contienen blobs).
6. **⤒ Upload** → subir `product1.json`, indicando en **Advanced → Upload to folder** el valor `product_data`.
7. Verificar que se ha creado la carpeta virtual `product_data` conteniendo `product1.json`.
![Comprobación de creación del blob](image-7.png)

---

## 3. Explorar Azure Data Lake Storage Gen2

*(Pendiente de completar)*

Pasos:
1. Descargar [product2.json](https://aka.ms/product2.json) en la misma carpeta local que `product1.json`.
2. En el storage account → **Settings** → **Data Lake Gen2 upgrade** → completar los 3 pasos (review, validate, upgrade) para activar el hierarchical namespace.
3. Volver a **Storage browser** → contenedor `data` → carpeta `product_data` (sigue conteniendo `product1.json`).
4. **⤒ Upload** → subir `product2.json` (sin indicar carpeta, ya que se sube dentro de `product_data`).
5. Verificar que `product_data` ahora contiene ambos archivos.
6. En **Containers** → carpeta `product_data` → **‧‧‧** → comprobar que ahora SÍ aparecen opciones de gestión: Properties, Rename, Copy URL, Generate SAS, **Manage ACL**, Delete.

**Capturas:**

*(pendiente)*

**Notas / incidencias:**

*(pendiente: diferencia observada en el menú contextual de la carpeta antes/después del upgrade a Gen2)*

---

## 4. Explorar Azure Files

*(Pendiente de completar)*

Pasos:
1. En el storage account → **Data storage** → **Classic file shares** → **+ Classic file share**.
2. Nombre: `files`, Access tier: Transaction optimized.
3. **Next: Backup >** → desmarcar **Enable backup** → **Review + create** → **Create**.
4. Abrir el share `files` creado → **Connect** → revisar las pestañas Windows / Linux / macOS con los scripts de conexión.

**Capturas:**

*(pendiente)*

**Notas / incidencias:**

*(pendiente)*

---

## 5. Limpieza de recursos

*(Pendiente de completar)*

1. Ir al grupo de recursos `dp900-lab-rg`.
2. **Delete resource group** → confirmar escribiendo el nombre → **Delete**.

**Captura:**

*(pendiente)*

---

## Conclusiones

*(pendiente: qué se ha aprendido — diferencia entre blob storage plano y Data Lake Gen2 con namespace jerárquico, carpetas virtuales vs reales, ACLs, Azure Files como recurso compartido tipo SMB/NFS)*