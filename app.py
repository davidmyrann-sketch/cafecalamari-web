#!/usr/bin/env python3
"""
Café Calamarí — cafecalamari.cafe
Flask + Railway + GitHub (standard stack)
"""
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# ── Config ────────────────────────────────────────────────────────────────────
SHOPIFY_STORE_URL = os.environ.get("SHOPIFY_STORE_URL", "")

# ── Oversettelser ──────────────────────────────────────────────────────────────
T = {
    "no": {
        "lang":          "no",
        "lang_label":    "Norsk",
        "nav_shop":      "Nettbutikk",
        "nav_story":     "Vår historie",
        "nav_contact":   "Kontakt",
        "nav_cta":       "Kjøp kaffe",

        "hero_tag":      "Direktehandel · Colombia · Oslo",
        "hero_h1":       "Kaffe med sjel fra Andesfjellene",
        "hero_sub":      "Håndplukket på 1 700 meters høyde i Santa Bárbara, Colombia. Bragt hjem til deg i Oslo.",
        "hero_cta1":     "Gå til nettbutikk →",
        "hero_cta2":     "Vår historie",

        "trust_1":       "Direktehandel med familiebonde",
        "trust_2":       "1 700 moh. — single origin",
        "trust_3":       "Ferskt ristet — ukentlig",
        "trust_4":       "Gratis frakt over 399 kr",

        "story_tag":     "Historien bak koppen",
        "story_h2":      "Vi strakk tentaklene til Colombia. Og ble forelsket.",
        "story_p1":      "Akkurat som blekkspruten utforsker verden med alle sine armer — reiste vi til Andesfjellene for å finne noe ekte. Vi fant det i Santa Bárbara: en familie som har dyrket kaffe i generasjoner, med hendene i jordsmonnet og hjertet i hver bønne.",
        "story_p2":      "Ingen mellommenn. Ingen kompromisser. Bønnene går fra gården i Colombia direkte til rosteriet i Oslo — og til deg.",
        "story_cta":     "Se produktene →",

        "shop_tag":      "Nettbutikk",
        "shop_h2":       "Velg din favoritt",
        "shop_sub":      "Alle bønner er ferskt ristet og klare for levering denne uken.",
        "shop_fomo":     "🔥 Begrenset parti — ny høst, kun mens lageret rekker",

        "why_tag":       "Hvorfor Calamarí",
        "why_h2":        "Du merker forskjellen fra første slurk",
        "why_1_h":       "Sporbar opprinnelse",
        "why_1_p":       "Du vet nøyaktig hvilken gård og hvilken høyde bønnene dine kommer fra.",
        "why_2_h":       "Fersk risting",
        "why_2_p":       "Vi rister ukentlig for å sikre maksimal ferskhet i hver kopp.",
        "why_3_h":       "Direkte støtte",
        "why_3_p":       "Bonden tjener mer. Du betaler ikke for mellomledd.",
        "why_4_h":       "Smak du husker",
        "why_4_p":       "Kunder som bytter til Calamarí, bytter ikke tilbake.",

        "social_tag":    "Følg reisen",
        "social_h2":     "Vi på Instagram",
        "social_sub":    "Se bak kulissene — fra gård til kopp.",
        "social_cta":    "Følg @cafecalamari.no →",

        "contact_tag":   "Kontakt",
        "contact_h2":    "Hola! Vi hører fra deg.",
        "contact_sub":   "Send oss en e-post — vi svarer innen 24 timer.",
        "contact_btn":   "Send oss en e-post →",

        "footer_copy":   "© 2026 Café Calamarí. Laget med ☕ i Oslo.",
        "footer_ig":     "Instagram",
        "footer_shop":   "Nettbutikk",
        "footer_mail":   "hola@cafecalamari.cafe",
    },
    "es": {
        "lang":          "es",
        "lang_label":    "Español",
        "nav_shop":      "Tienda",
        "nav_story":     "Nuestra historia",
        "nav_contact":   "Contacto",
        "nav_cta":       "Comprar café",

        "hero_tag":      "Comercio directo · Colombia · Oslo",
        "hero_h1":       "Café con alma de los Andes",
        "hero_sub":      "Recolectado a mano a 1 700 metros de altura en Santa Bárbara, Colombia. Traído a tu taza en Oslo.",
        "hero_cta1":     "Ver tienda →",
        "hero_cta2":     "Nuestra historia",

        "trust_1":       "Comercio directo con familia cafetera",
        "trust_2":       "1 700 msnm — single origin",
        "trust_3":       "Tostado fresco — cada semana",
        "trust_4":       "Envío gratis desde 399 kr",

        "story_tag":     "La historia detrás de la taza",
        "story_h2":      "Extendimos los tentáculos hasta Colombia. Y nos enamoramos.",
        "story_p1":      "Como el calamar que explora el mundo con todos sus brazos, nosotros viajamos a los Andes en busca de algo auténtico. Lo encontramos en Santa Bárbara: una familia que ha cultivado café por generaciones, con las manos en la tierra y el corazón en cada grano.",
        "story_p2":      "Sin intermediarios. Sin compromisos. Los granos van directamente de la finca en Colombia a la tostadora en Oslo — y a ti.",
        "story_cta":     "Ver productos →",

        "shop_tag":      "Tienda",
        "shop_h2":       "Elige tu favorito",
        "shop_sub":      "Todos los granos recién tostados y listos para envío esta semana.",
        "shop_fomo":     "🔥 Lote limitado — nueva cosecha, solo mientras dure el stock",

        "why_tag":       "Por qué Calamarí",
        "why_h2":        "La diferencia la notas desde el primer sorbo",
        "why_1_h":       "Origen trazable",
        "why_1_p":       "Sabes exactamente de qué finca y a qué altitud vienen tus granos.",
        "why_2_h":       "Tostado fresco",
        "why_2_p":       "Tostamos cada semana para garantizar la máxima frescura en cada taza.",
        "why_3_h":       "Apoyo directo",
        "why_3_p":       "El agricultor gana más. Tú no pagas intermediarios.",
        "why_4_h":       "Un sabor que recuerdas",
        "why_4_p":       "Quienes cambian a Calamarí, no vuelven atrás.",

        "social_tag":    "Síguenos",
        "social_h2":     "Nosotros en Instagram",
        "social_sub":    "Mira detrás de cámaras — de la finca a la taza.",
        "social_cta":    "Seguir @cafecalamari.no →",

        "contact_tag":   "Contacto",
        "contact_h2":    "¡Hola! Te escuchamos.",
        "contact_sub":   "Escríbenos — respondemos en 24 horas.",
        "contact_btn":   "Envíanos un correo →",

        "footer_copy":   "© 2026 Café Calamarí. Hecho con ☕ en Oslo.",
        "footer_ig":     "Instagram",
        "footer_shop":   "Tienda",
        "footer_mail":   "hola@cafecalamari.cafe",
    },
    "en": {
        "lang":          "en",
        "lang_label":    "English",
        "nav_shop":      "Shop",
        "nav_story":     "Our story",
        "nav_contact":   "Contact",
        "nav_cta":       "Buy coffee",

        "hero_tag":      "Direct trade · Colombia · Oslo",
        "hero_h1":       "Coffee with soul from the Andes",
        "hero_sub":      "Hand-picked at 1,700 metres above sea level in Santa Bárbara, Colombia. Brought home to you in Oslo.",
        "hero_cta1":     "Go to shop →",
        "hero_cta2":     "Our story",

        "trust_1":       "Direct trade with family farm",
        "trust_2":       "1,700 masl — single origin",
        "trust_3":       "Freshly roasted — weekly",
        "trust_4":       "Free shipping over 399 kr",

        "story_tag":     "The story behind the cup",
        "story_h2":      "We reached our tentacles to Colombia. And fell in love.",
        "story_p1":      "Just like the squid explores the world with all its arms — we travelled to the Andes to find something real. We found it in Santa Bárbara: a family that has grown coffee for generations, with hands in the soil and heart in every bean.",
        "story_p2":      "No middlemen. No compromises. Beans go directly from the farm in Colombia to the roastery in Oslo — and to you.",
        "story_cta":     "See products →",

        "shop_tag":      "Shop",
        "shop_h2":       "Find your favourite",
        "shop_sub":      "All beans freshly roasted and ready to ship this week.",
        "shop_fomo":     "🔥 Limited batch — new harvest, only while stocks last",

        "why_tag":       "Why Calamarí",
        "why_h2":        "You'll taste the difference from the very first sip",
        "why_1_h":       "Traceable origin",
        "why_1_p":       "You know exactly which farm and at what altitude your beans come from.",
        "why_2_h":       "Fresh roast",
        "why_2_p":       "We roast weekly to ensure maximum freshness in every cup.",
        "why_3_h":       "Direct support",
        "why_3_p":       "The farmer earns more. You don't pay for middlemen.",
        "why_4_h":       "A taste you remember",
        "why_4_p":       "Customers who switch to Calamarí don't switch back.",

        "social_tag":    "Follow the journey",
        "social_h2":     "Us on Instagram",
        "social_sub":    "See behind the scenes — from farm to cup.",
        "social_cta":    "Follow @cafecalamari.no →",

        "contact_tag":   "Contact",
        "contact_h2":    "Hola! We'd love to hear from you.",
        "contact_sub":   "Drop us an email — we reply within 24 hours.",
        "contact_btn":   "Send us an email →",

        "footer_copy":   "© 2026 Café Calamarí. Made with ☕ in Oslo.",
        "footer_ig":     "Instagram",
        "footer_shop":   "Shop",
        "footer_mail":   "hola@cafecalamari.cafe",
    },
}

def get_lang(req):
    lang = req.args.get("lang", "no")
    return lang if lang in T else "no"

# ── Ruter ──────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    lang = get_lang(request)
    return render_template("index.html", t=T[lang], lang=lang,
                           shopify_url=SHOPIFY_STORE_URL)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
