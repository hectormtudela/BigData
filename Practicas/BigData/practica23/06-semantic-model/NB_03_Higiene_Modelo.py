# Notebook NB_03_Higiene_Modelo (Fabric) - higiene 6.3 del modelo SM_Ventas con semantic-link-labs / TOM
# %pip install -q semantic-link-labs
from sempy_labs.tom import connect_semantic_model
cm = connect_semantic_model(dataset='SM_Ventas', workspace='WS-DP600-Lab-Hector', readonly=False)
tom = cm.__enter__()
import Microsoft.AnalysisServices.Tabular as TOM
m = tom.model
dd = m.Tables['Dim_Date']
dd.DataCategory = 'Time'                      # 23. marcar tabla de fecha
dd.Columns['FullDate'].IsKey = True
keys = ['DateKey','Product_SK','Customer_SK','Store_SK','OrderDateKey','ShipDateKey']
for t in m.Tables: [setattr(c,'IsHidden',True) for c in t.Columns if c.Name in keys or c.Name.startswith('Rec')]   # 24
for n in ['Quantity','GrossAmount','DiscountAmount','NetAmount']: m.Tables['Fact_Sales'].Columns[n].IsHidden = True  # 25
h = TOM.Hierarchy(); h.Name = 'Calendario'    # 26. jerarquía
for i,n in enumerate(['Year','QuarterName','MonthName','Day']): l = TOM.Level(); l.Name = n; l.Column = dd.Columns[n]; l.Ordinal = i; h.Levels.Add(l)
dd.Hierarchies.Add(h)
dd.Columns['MonthName'].SortByColumn = dd.Columns['Month']   # 27. ordenar meses
cm.__exit__(None, None, None)                 # guarda los cambios en el modelo
