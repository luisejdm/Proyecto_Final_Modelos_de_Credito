import pandas as pd
import folium

# ── Carga y filtrado ─────────────────────────────────────────────────────────
df = pd.read_csv("denue_inegi_54_.csv", encoding="latin1", low_memory=False)

ZMG = {
    39:  "Guadalajara",
    120: "Zapopan",
    98:  "San Pedro Tlaquepaque",
    101: "Tonalá",
    97:  "Tlajomulco de Zúñiga",
    70:  "El Salto",
    51:  "Juanacatlán",
    44:  "Ixtlahuacán de los Membrillos",
}

mask = (df["cve_ent"] == 14) & (df["cve_mun"].isin(ZMG)) & (df["codigo_act"] == 541941)
df = df[mask].copy()

df["latitud"]  = pd.to_numeric(df["latitud"],  errors="coerce")
df["longitud"] = pd.to_numeric(df["longitud"], errors="coerce")
df = df.dropna(subset=["latitud", "longitud"])
df["municipio_zmg"] = df["cve_mun"].map(ZMG)

print(f"Establecimientos SCIAN 541941 en ZMG: {len(df)}")

nombre_act = df["nombre_act"].iloc[0] if "nombre_act" in df.columns else "Actividad 541941"

# ── Colores por municipio ────────────────────────────────────────────────────
COLORES = {
    "Guadalajara":                  "#2166ac",
    "Zapopan":                      "#d6604d",
    "San Pedro Tlaquepaque":        "#4dac26",
    "Tonalá":                       "#f4a582",
    "Tlajomulco de Zúñiga":         "#8c510a",
    "El Salto":                     "#762a83",
    "Juanacatlán":                  "#1b7837",
    "Ixtlahuacán de los Membrillos":"#e08214",
}

# ── Mapa ─────────────────────────────────────────────────────────────────────
mapa = folium.Map(location=[20.6534, -103.3475], zoom_start=11, tiles="CartoDB positron")

for _, row in df.iterrows():
    mun   = row["municipio_zmg"]
    nom   = row.get("nom_estab", "Sin nombre")
    colonia = row.get("nomb_asent", "N/D")
    per_ocu = row.get("per_ocu", "N/D")
    dir_parts = [
        str(row.get("tipo_vial", "")), str(row.get("nom_vial", "")),
        str(row.get("numero_ext", "")),
    ]
    direccion = " ".join(p for p in dir_parts if p and p != "nan")

    popup_html = f"""
    <div style="font-family:sans-serif;font-size:13px;min-width:210px">
      <b>{nom}</b><br>
      <span style="color:#555;font-size:12px">{nombre_act}</span><br><br>
      <b>Municipio:</b> {mun}<br>
      <b>Colonia:</b> {colonia}<br>
      <b>Personal:</b> {per_ocu}<br>
      <b>Dirección:</b> {direccion}
    </div>"""

    folium.CircleMarker(
        location=[row["latitud"], row["longitud"]],
        radius=6,
        color=COLORES[mun],
        fill=True,
        fill_color=COLORES[mun],
        fill_opacity=0.7,
        weight=1.2,
        popup=folium.Popup(popup_html, max_width=280),
        tooltip=f"{nom} · {mun}",
    ).add_to(mapa)

# ── Leyenda ──────────────────────────────────────────────────────────────────
filas = ""
for mun in sorted(ZMG.values()):
    cnt = len(df[df["municipio_zmg"] == mun])
    if cnt == 0:
        continue
    c = COLORES[mun]
    filas += (
        f'<div style="margin:3px 0">'
        f'<span style="display:inline-block;width:12px;height:12px;'
        f'background:{c};border-radius:50%;margin-right:7px;vertical-align:middle"></span>'
        f'{mun} <b>({cnt})</b></div>\n'
    )

leyenda = f"""
<div style="
    position:fixed;bottom:40px;left:40px;z-index:1000;
    background:white;padding:14px 18px;border-radius:8px;
    box-shadow:2px 2px 8px rgba(0,0,0,.25);font-family:sans-serif;font-size:15px;
    max-width:270px">
  <b style="font-size:14px">SCIAN 541941</b><br>
  <span style="color:#555;font-size:15px">{f'{nombre_act}.'}</span><br><br>
  <span style="color:#555;font-size:15px">Zona Metropolitana de Guadalajara.</span>
  <hr style="margin:8px 0">
  {filas}
  <hr style="margin:8px 0">
  <b>Total: {len(df)} establecimientos</b>
</div>"""

mapa.get_root().html.add_child(folium.Element(leyenda))

output = "mapa_zmg_541941.html"
mapa.save(output)
print(f"Mapa guardado: {output}")
