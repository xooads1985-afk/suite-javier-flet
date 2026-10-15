import flet as ft

def main(page: ft.Page):
    page.title = "🚨 JAVIER IMPERIO ANALÍTICO v1.0 🚨"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B0C10"  
    page.padding = 15
    page.scroll = ft.ScrollMode.AUTO

    if not hasattr(page, "mundo_activo"):
        page.mundo_activo = 0

    mundos_config = {
        0: {"nombre": "⚽ FÚTBOL TRADICIONAL", "desc": "Estrategia de Duplicación (Máximo 2 Equipos por Jugada)", "info": "🌍 Sistema de Cajas Libres Activo: Válido para CUALQUIER equipo de CUALQUIER liga, copa o torneo del planeta."},
        1: {"nombre": "🏈 PLAYER PROPS NFL", "desc": "Límites fijados: QB 300 Yds / RB 100 Yds", "info": "📊 Modo de puros verdes con semáforo inteligente y atletas libres."},
        2: {"nombre": "🏀 NBA BÁSQUETBOL", "desc": "Calibrador de Spreads alternos de 1.5 en 1.5 pts", "info": "🏀 Tableros de Novibet y Playdoit ready al ras de la pared."},
        3: {"nombre": "🏒 NHL HOCKEY HIELO", "desc": "Filtro: Análisis de Goaltenders y Flujo Sharp", "info": "🏒 Parlays dobles acorazados para duplicar capital base."},
        4: {"nombre": "⚾ MLB BÉISBOL", "desc": "Mapeo quirúrgico de abridores y volumen Sharp", "info": "🛑 Alerta: Escéptico con Austin Wells (frecuencia de strikeouts)."},
        5: {"nombre": "🏈 NCAA FOOTBALL", "desc": "Próxima integración del sistema de datos colegiales", "info": "📂 Mantener ligas separadas de forma estricta por ticket."},
        6: {"nombre": "🇲🇽 LIGA MX SOCCER", "desc": "Análisis histórico de localías y tendencias", "info": "🦅 Tableros de rendimiento y automatización de boletas."},
        7: {"nombre": "🏆 CHAMPIONS LEAGUE", "desc": "Auditoría científica profunda en tiempo real", "info": "🇪🇸 Análisis automatizado por capturas e imágenes vivas."},
        8: {"nombre": "🥊 UFC / BOXEO", "desc": "Probabilidades de finalización y control de riesgo", "info": "🥊 Rangos de momios seguros activos en Novibet."},
        9: {"nombre": "🎾 EL MUNDO DEL TENIS", "desc": "Seguimiento de Circuitos ATP / WTA y Grand Slams", "info": "🎾 Análisis de superficies, quiebres de servicio y valor Sharp."}
    }

    contenedor_contenido = ft.Container(
        bgcolor="#1F2833",
        padding=20,
        border_radius=15,
        alignment=ft.alignment.center
    )

    def refrescar_pantalla_mundo():
        m = mundos_config[page.mundo_activo]
        contenedor_contenido.content = ft.Column([
            ft.Text(m["nombre"], size=22, color="#66FCF1", weight=ft.FontWeight.BOLD),
            ft.Text(m["desc"], size=14, color="#45A29E"),
            ft.Divider(color="#0B0C10"),
            ft.Text(m["info"], size=15, color="#FFFFFF")
        ], spacing=10)
        page.update()

    def seleccionar_mundo(e):
        page.mundo_activo = int(e.control.data)
        refrescar_pantalla_mundo()

    lista_botones_mundos = ft.Row(
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.ElevatedButton(
                text=f"Mundo {i+1}", 
                bgcolor="#1F2833" if i != page.mundo_activo else "#45A29E",
                color="#66FCF1" if i != page.mundo_activo else "#0B0C10",
                data=i,
                on_click=seleccionar_mundo
            ) for i in range(10)
        ]
    )

    refrescar_pantalla_mundo()
    
    page.add(
        ft.Text("🚨 JAVIER APP TOTAL - 10 MUNDOS UNIFICADOS 🚨", size=14, color="#66FCF1", weight=ft.FontWeight.W_600),
        ft.Text("Desliza horizontalmente para cambiar de Mundo con tu dedo:", size=12, color="#45A29E"),
        lista_botones_mundos,
        ft.Divider(color="#1F2833"),
        contenedor_contenido
    )

ft.app(main)
