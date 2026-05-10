import pandas as pd
import folium
from pathlib import Path

BASE = Path(__file__).parent

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

CAPAS = [
    {
        "csv":       BASE / "denue_inegi_54_.csv",
        "actividad": 541941,
        "label":     "Veterinarias",
        "color":     "#2166ac",
    },
    {
        "csv":       BASE / "denue_inegi_81_1.csv",
        "actividad": 812990,
        "label":     "Estéticas caninas",
        "color":     "#56c08b",
    },
]

mapa = folium.Map(location=[20.6534, -103.3475], zoom_start=11, tiles="CartoDB positron")

totales = {}
for capa in CAPAS:
    df = pd.read_csv(capa["csv"], encoding="latin1", low_memory=False)
    mask = (df["cve_ent"] == 14) & (df["cve_mun"].isin(ZMG)) & (df["codigo_act"] == capa["actividad"])
    df = df[mask].copy()
    df["latitud"]  = pd.to_numeric(df["latitud"],  errors="coerce")
    df["longitud"] = pd.to_numeric(df["longitud"], errors="coerce")
    df = df.dropna(subset=["latitud", "longitud"])
    df["municipio_zmg"] = df["cve_mun"].map(ZMG)

    totales[capa["label"]] = len(df)
    print(f"{capa['label']} (SCIAN {capa['actividad']}): {len(df)} establecimientos")

    for _, row in df.iterrows():
        nom     = row.get("nom_estab", "Sin nombre")
        mun     = row["municipio_zmg"]
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
          <span style="color:{capa['color']};font-weight:bold;font-size:12px">{capa['label']}</span>
          <span style="color:#555;font-size:12px"> · SCIAN {capa['actividad']}</span><br><br>
          <b>Municipio:</b> {mun}<br>
          <b>Colonia:</b> {colonia}<br>
          <b>Personal:</b> {per_ocu}<br>
          <b>Dirección:</b> {direccion}
        </div>"""

        folium.CircleMarker(
            location=[row["latitud"], row["longitud"]],
            radius=6,
            color=capa["color"],
            fill=True,
            fill_color=capa["color"],
            fill_opacity=0.75,
            weight=1.2,
            popup=folium.Popup(popup_html, max_width=280),
            tooltip=f"{nom} · {capa['label']}",
        ).add_to(mapa)

# ── Leyenda ──────────────────────────────────────────────────────────────────
filas = ""
for capa in CAPAS:
    cnt = totales[capa["label"]]
    filas += (
        f'<div style="margin:4px 0">'
        f'<span style="display:inline-block;width:12px;height:12px;'
        f'background:{capa["color"]};border-radius:50%;margin-right:7px;vertical-align:middle"></span>'
        f'{capa["label"]} <b>({cnt})</b></div>\n'
    )

total = sum(totales.values())
leyenda = f"""
<div style="
    position:fixed;bottom:40px;left:40px;z-index:1000;
    background:white;padding:14px 18px;border-radius:8px;
    box-shadow:2px 2px 8px rgba(0,0,0,.25);font-family:sans-serif;font-size:15px;
    max-width:260px">
  <b style="font-size:15px">Servicios para mascotas</b><br>
  <span style="color:#555;font-size:15px">Zona Metropolitana de Guadalajara</span>
  <hr style="margin:8px 0">
  {filas}
  <hr style="margin:8px 0">
  <b>Total: {total} establecimientos</b>
</div>"""

mapa.get_root().html.add_child(folium.Element(leyenda))

output = "mapa_zmg_combinado.html"
mapa.save(output)
print(f"Mapa guardado: {output}")
