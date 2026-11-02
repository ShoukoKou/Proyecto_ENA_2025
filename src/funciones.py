import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# LIMPIEZA
def filtrar_departamentos(df, departamentos):
    df = df.copy()
    df["NOMBREDD"] = df["NOMBREDD"].astype("string").str.strip().str.upper()
    df = df[df["NOMBREDD"].isin(departamentos)].copy()
    return df


# UNIDADES AGROPECUARIAS
def contar_ua(df, llave_ua):
    return df[llave_ua].dropna().drop_duplicates().shape[0]


# RESUMEN POR DEPARTAMENTO
def resumen_departamentos(df, columna):
    tabla = df.groupby("NOMBREDD").agg(
        registros=("UA", "size"),
        valores_distintos=(columna, "nunique")
    ).reset_index()
    return tabla


# FRECUENCIA DE DOS VARIABLES
def tabla_frecuencia_doble(df, columna1, columna2):
    tabla = pd.crosstab(df[columna1], df[columna2])
    return tabla


# RESUMEN ESTADISTICO
def tabla_resumen(df, grupo, variable):
    tabla = df.groupby(grupo)[variable].agg(
        ["count", "sum", "mean", "median", "min", "max"]
    ).reset_index()
    return tabla.round(2)


# GRAFICO DE BARRAS
def grafico_barras(tabla, x, y, titulo):
    tabla.plot(x=x, y=y, kind="bar", figsize=(10, 6), legend=False)
    plt.title(titulo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# GRAFICO DE BARRAS APILADAS
def grafico_barras_apiladas(tabla, titulo):
    tabla.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.title(titulo)
    plt.xlabel(tabla.index.name)
    plt.ylabel("Número de registros")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# GRAFICO BOXPLOT
def grafico_boxplot(df, grupo, variable, titulo):
    df.boxplot(column=variable, by=grupo, figsize=(10, 6))
    plt.title(titulo)
    plt.suptitle("")
    plt.xlabel(grupo)
    plt.ylabel(variable)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# GRAFICO DE DISPERSION
def grafico_dispersion(df, x, y, titulo):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x], df[y], alpha=0.3)
    plt.title(titulo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.show()

def filtrar_departamentos(df, departamentos):
    df = df.copy()
    df["NOMBREDD"] = df["NOMBREDD"].astype("string").str.strip().str.upper()
    df["NOMBREPV"] = df["NOMBREPV"].astype("string").str.strip().str.upper()
    df = df[df["NOMBREDD"].isin(departamentos)].copy()
    return df

def cargar_mapa_provincias(ruta_mapa, departamentos):
    gdf = gpd.read_file(ruta_mapa)
    gdf["NOMBDEP"] = gdf["NOMBDEP"].astype("string").str.strip().str.upper()
    gdf["NOMBPROV"] = gdf["NOMBPROV"].astype("string").str.strip().str.upper()
    gdf = gdf[gdf["NOMBDEP"].isin(departamentos)].copy()
    return gdf

def resumen_conteo_provincia(df):
    tabla = df.groupby(["NOMBREDD", "NOMBREPV"]).size().reset_index(name="cantidad")
    return tabla

def resumen_nunique_provincia(df, columna):
    tabla = df.groupby(["NOMBREDD", "NOMBREPV"])[columna].nunique().reset_index(name="cantidad")
    return tabla

def resumen_suma_provincia(df, columna):
    tabla = df.groupby(["NOMBREDD", "NOMBREPV"])[columna].sum().reset_index(name="cantidad")
    return tabla

def resumen_promedio_provincia(df, columna):
    tabla = df.groupby(["NOMBREDD", "NOMBREPV"])[columna].mean().reset_index(name="cantidad")
    tabla["cantidad"] = tabla["cantidad"].round(2)
    return tabla

def unir_mapa_con_datos(gdf, tabla):
    mapa = gdf.merge(tabla, left_on=["NOMBDEP", "NOMBPROV"], right_on=["NOMBREDD", "NOMBREPV"], how="left")
    return mapa

def graficar_mapa_coropletico(mapa, titulo):
    fig, ax = plt.subplots(figsize=(12, 10))
    mapa.plot(column="cantidad", cmap="OrRd", legend=True, edgecolor="black", linewidth=0.5, ax=ax)
    ax.set_title(titulo)
    ax.set_axis_off()
    plt.show()